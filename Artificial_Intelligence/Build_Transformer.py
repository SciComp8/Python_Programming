# References: 
# Attention is all you need. https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
# https://pytorch.org/docs/stable/_modules/torch/nn/modules/transformer.html#Transformer
# A weighting scheme enables a *transformer* model to give varying degrees of attention to different segments of the input when generating an output.
# https://harvard-iacs.github.io/2021-CS109B/lectures/lecture24/
# https://harvard-iacs.github.io/2021-CS109B/lectures/lecture25/

# Set up the working environment
pip3 install torch torchvision torchaudio

# Import the libraries and modules
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import math
import copy

# Define Multi-head Attention
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        """
        MultiHeadAttention class serves as a container for the multi-head attention mechanism, a frequent component in transformer models. 
        Its responsibilities include dividing the input into multiple attention heads, applying attention individually to each head, and subsequently amalgamating the outcomes. 
        This process enhances the model's capability to discern diverse relationships within the input data at varying levels of granularity, ultimately enhancing the model's expressiveness.
        d_model: dimensionality of the input
        num_heads: the number of attention heads to split the input into.
        """
        super(MultiHeadAttention, self).__init__()

        # Check if d_model is divisible by num_heads
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")

        # Initialize dimensions
        self.d_model = d_model             # Model's dimension
        self.num_heads = num_heads         # Number of attention heads
        self.d_k = d_model // num_heads    # Dimension of each head's key, query, and value

        # Build linear layers for transforming inputs
        self.W_q = nn.Linear(d_model, d_model)  # Define the transformation weights for query
        self.W_k = nn.Linear(d_model, d_model)  # Define the transformation weights for key
        self.W_v = nn.Linear(d_model, d_model)  # Define the transformation weights for value
        self.W_o = nn.Linear(d_model, d_model)  # Define the transformation weights for output

    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        # Calculate attention scores
        attn_scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)
        
        # Apply mask if provided (typically used for masking out certain elements, like padding tokens)
        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask == 0, -1e9)
        
        # Use softmax to convert the attention scores into attention probabilities that sum to 1
        attn_probs = torch.softmax(attn_scores, dim=-1)
        
        # Compute the output by multiplying the attention weights by the values (V)
        output = torch.matmul(attn_probs, V)
        return output

    def split_heads(self, x):
        # Reshape the input x into the shape (batch_size, num_heads, seq_length, d_k)
        # Process multiple attention heads concurrently
        batch_size, seq_length, d_model = x.size()
        return x.view(batch_size, seq_length, self.num_heads, self.d_k).transpose(1, 2)
    
    def combine_heads(self, x):
        # Combine the results back into a single tensor of shape (batch_size, seq_length, d_model)
        batch_size, _, seq_length, d_k = x.size()
        return x.transpose(1, 2).contiguous().view(batch_size, seq_length, self.d_model)
    
    def forward(self, Q, K, V, mask=None):
        # Build linear layers for transforming inputs and split heads
        Q = self.split_heads(self.W_q(Q))
        K = self.split_heads(self.W_k(K))
        V = self.split_heads(self.W_v(V))
        
        # Conduct scaled dot-product attention on the split heads
        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)
        
        # Reassemble the multiple heads to restore the original shape and build linear layers for transforming the output
        output = self.W_o(self.combine_heads(attn_output))
        return output
    
# Define Position-Wise Feed-Forward Networks
class PositionWiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        """
        The PositionWiseFeedForward class represents a neural network designed for position-wise operations. 
        It comprises two linear layers separated by a ReLU activation function. 
        In the context of transformer models, this feed-forward network is individually and uniformly applied to each position. 
        Its primary function is to modify the features acquired from the transformer's attention mechanisms, serving as an additional processing step.
        d_model: dimensionality of the model's input and output
        d_ff: dimensionality of the inner layer in the feed-forward network
        self.fc1 and self.fc2: two fully connected (linear) layers with input and output dimensions as defined by d_model and d_ff
        self.relu: ReLU (Rectified Linear Unit) activation function, which introduces non-linearity between the two linear layers by replacing all negative values with zeros
        """
        super(PositionWiseFeedForward, self).__init__()

        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

# Define Positional Encoding
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_length):
        """
        The PositionalEncoding class incorporates positional information of tokens within a sequence. 
        Given that the transformer model lacks built-in awareness of token order, owing to its self-attention mechanism, this class aids the model in accounting for token positions within the sequence. 
        It employs sinusoidal functions selected to enable the model to effortlessly acquire the ability to attend to relative positions, yielding distinct and continuous encodings for each position in the sequence.
        d_model: the dimension of the model's input
        max_seq_length: the maximum length of the sequence for which positional encodings are pre-computed
        pe: a tensor filled with zeros, which will be populated with positional encodings
        position: a tensor containing the position indices for each position in the sequence
        div_term: a term used to scale the position indices in a specific way
        """
        super(PositionalEncoding, self).__init__()
        
        pe = torch.zeros(max_seq_length, d_model)
        position = torch.arange(0, max_seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        
        # The sine function is applied to the even indices and the cosine function to the odd indices of pe
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        # pe is registered as a buffer, which means it will be part of the module's state but will not be considered a trainable paramete
        self.register_buffer('pe', pe.unsqueeze(0))
        
    def forward(self, x):
        # Add the positional encodings to the input x
        return x + self.pe[:, :x.size(1)]

# Build the Encoder
class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        """
        The EncoderLayer class in a transformer defines one layer of the encoder. 
        It combines a multi-head self-attention mechanism with a position-wise feed-forward neural network, applying residual connections, layer normalization, and dropout as needed. 
        These elements enable the encoder to capture intricate relationships in the input data and convert them into a valuable representation for downstream tasks. 
        Typically, several encoder layers are stacked to create the full encoder in a transformer model.
        d_model: the dimensionality of the input
        num_heads: number of attention heads in the multi-head attention
        d_ff: the dimensionality of the inner layer in the position-wise feed-forward network
        dropout: the dropout rate used for regularization
        self.self_attn: multi-head attention mechanism
        self.feed_forward: position-wise feed-forward neural network
        self.norm1 and self.norm2: layer normalization, applied to smooth the layer's input
        self.dropout: dropout layer, used to prevent overfitting by randomly setting some activations to zero during training
        """
        super(EncoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, mask):
        """
        x: the input to the encoder layer
        mask: optional mask to ignore certain parts of the input
        """
        attn_output = self.self_attn(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_output))
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))
        return x

# Build the Decoder
class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout):
        """
        The DecoderLayer class in a transformer model defines a single decoder layer, which includes multi-head self-attention, multi-head cross-attention to the encoder's output, a position-wise feed-forward neural network, and utilizes residual connections, layer normalization, and dropout layers. 
        This combination allows the decoder to produce meaningful outputs by considering both the target and source sequences. 
        Similar to the encoder, multiple decoder layers are usually stacked to create the complete decoder component of a transformer model.
        d_model: the dimensionality of the input
        num_heads: the number of attention heads in the multi-head attention
        d_ff: the dimensionality of the inner layer in the feed-forward network
        dropout: the dropout rate for regularization
        self.self_attn: multi-head self-attention mechanism for the target sequence
        self.cross_attn: multi-head attention mechanism that attends to the encoder's output
        self.feed_forward: position-wise feed-forward neural network
        self.norm1, self.norm2, self.norm3: layer normalization components
        self.dropout: dropout layer for regularization
        """
        super(DecoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.cross_attn = MultiHeadAttention(d_model, num_heads)
        self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, enc_output, src_mask, tgt_mask):
        """
        x: the input to the decoder layer
        enc_output: the output from the corresponding encoder (used in the cross-attention step)
        src_mask: source mask to ignore certain parts of the encoder's output
        tgt_mask: target mask to ignore certain parts of the decoder's input
        """
        attn_output = self.self_attn(x, x, x, tgt_mask)
        x = self.norm1(x + self.dropout(attn_output))
        attn_output = self.cross_attn(x, enc_output, enc_output, src_mask)
        x = self.norm2(x + self.dropout(attn_output))
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))
        return x

# Combine the Encoder and Decoder layers
class Transformer(nn.Module):
    """
    The Transformer class consolidates all key components of a Transformer model, such as embeddings, positional encoding, encoder layers, and decoder layers. 
    It simplifies training and inference, handling intricate aspects like multi-head attention, feed-forward networks, and layer normalization.
    This implementation adheres to the standard Transformer architecture, making it well-suited for sequence-to-sequence tasks like machine translation and text summarization. 
    The use of masking ensures the model respects causal dependencies within sequences by ignoring padding tokens and preventing information leakage from future tokens.
    src_vocab_size: source vocabulary size
    tgt_vocab_size: target vocabulary size
    d_model: the dimensionality of the model's embeddings
    num_heads: number of attention heads in the multi-head attention mechanism
    num_layers: number of layers for both the encoder and the decoder
    d_ff: dimensionality of the inner layer in the feed-forward network
    max_seq_length: maximum sequence length for positional encoding
    dropout: dropout rate for regularization
    self.encoder_embedding: embedding layer for the source sequence
    self.decoder_embedding: embedding layer for the target sequence
    self.positional_encoding: positional encoding component
    self.encoder_layers: a list of encoder layers
    self.decoder_layers: a list of decoder layers
    self.fc: final fully connected (linear) layer mapping to target vocabulary size
    self.dropout: dropout layer
    """
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model, num_heads, num_layers, d_ff, max_seq_length, dropout):
        super(Transformer, self).__init__()
        self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)
        self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.positional_encoding = PositionalEncoding(d_model, max_seq_length)

        self.encoder_layers = nn.ModuleList([EncoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)])
        self.decoder_layers = nn.ModuleList([DecoderLayer(d_model, num_heads, d_ff, dropout) for _ in range(num_layers)])

        self.fc = nn.Linear(d_model, tgt_vocab_size)
        self.dropout = nn.Dropout(dropout)

    def generate_mask(self, src, tgt):
        src_mask = (src != 0).unsqueeze(1).unsqueeze(2)
        tgt_mask = (tgt != 0).unsqueeze(1).unsqueeze(3)
        seq_length = tgt.size(1)
        nopeak_mask = (1 - torch.triu(torch.ones(1, seq_length, seq_length), diagonal=1)).bool()
        tgt_mask = tgt_mask & nopeak_mask
        return src_mask, tgt_mask

    def forward(self, src, tgt):
        src_mask, tgt_mask = self.generate_mask(src, tgt)
        src_embedded = self.dropout(self.positional_encoding(self.encoder_embedding(src)))
        tgt_embedded = self.dropout(self.positional_encoding(self.decoder_embedding(tgt)))

        enc_output = src_embedded
        for enc_layer in self.encoder_layers:
            enc_output = enc_layer(enc_output, src_mask)

        dec_output = tgt_embedded
        for dec_layer in self.decoder_layers:
            dec_output = dec_layer(dec_output, enc_output, src_mask, tgt_mask)

        output = self.fc(dec_output)
        return output
