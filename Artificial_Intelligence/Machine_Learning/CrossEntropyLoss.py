# https://stackoverflow.com/questions/52946920/bool-value-of-tensor-with-more-than-one-value-is-ambiguous-in-pytorch
# https://discuss.pytorch.org/t/runtimeerror-trying-to-backward-through-the-graph-a-second-time-but-the-buffers-have-already-been-freed-specify-retain-graph-true-when-calling-backward-the-first-time/6795

# Case 1
from sklearn.metrics import log_loss
true_label = ["ginger", "rose", "rose", "ginger"]
pred_prob = [[.1, .9], [.8, .2], [.9, .1], [.05, .95]]
log_loss(true_label, pred_prob)
# 2.3025850929940455

log_loss(["spam", "ham", "ham", "spam"], [[.1, .9], [.8, .2], [.9, .1], [.05, .95]])
# 0.1212894692543532 # TD ?

# Case 2.1
import torch
import torch.nn as nn
import torch.nn.functional as F

score = torch.tensor([[10, 2, -3, 6, 9, 19]]) # Predictions for 6 classes per subject 
one_hot_label = F.one_hot(torch.tensor(0), num_classes=6).unsqueeze(0)
one_hot_label 
loss = nn.CrossEntropyLoss()
loss_value = loss(score.double(), one_hot_label.double())
print(loss_value) 

# Case 2.2
import torch
import torch.nn as nn

def compute_cross_entropy_loss_and_backpropagate(input, target):
    loss = nn.CrossEntropyLoss()
    output = loss(input, target)
    output.backward() # Compute the gradients of the loss
    return output, input.grad

# Create random input data (690 samples, 3 classes)
input = torch.randn(690, 3, requires_grad=True)
# Create a random target tensor (690 samples with 3 class indices)
target = torch.empty(690, dtype=torch.long).random_(3)
loss_value, gradients = compute_cross_entropy_loss_and_backpropagate(input, target)
print("Loss Value:", loss_value.item())
print("Gradients:\n", gradients)
gradients.shape # torch.Size([690, 3])

# Case 2.3 - stochastic gradient descent 
import torch
import torch.nn as nn
import torch.optim as optim
new_data = torch.randn(1, 30)
model = nn.Sequential(nn.Linear(in_features=30, out_features=20),
                      nn.Linear(in_features=20, out_features=10),
                      nn.Linear(in_features=10, out_features=5),
                      nn.Linear(in_features=5, out_features=2))
target = torch.tensor([[1., 0.]])
prediction = model(new_data)
loss = nn.CrossEntropyLoss()(prediction, target)
optimizer = optim.SGD(model.parameters(), lr=0.001)
loss.backward()
optimizer.step() # Update model parameters


