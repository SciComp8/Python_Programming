scRNA_seq_metadata = [
    ["cell_id", "sample_id", "cell_type", "condition", "treatment", "sequencing_batch", "nUMI", "nGene", "percent_mt"],
    ["cell_001", "sample_A", "T-cell", "healthy", "none", "batch_1", 1200, 800, 2.5],
    ["cell_002", "sample_A", "B-cell", "disease", "drug_X", "batch_1", 1500, 1000, 3.1],
    ["cell_003", "sample_B", "Monocyte", "disease", "drug_Y", "batch_2", 1800, 1100, 4.0],
    ["cell_004", "sample_B", "NK-cell", "healthy", "none", "batch_2", 1400, 950, 2.8],
]

for row in scRNA_seq_metadata:
    print(row)


position = scRNA_seq_metadata.index(["cell_004", "sample_B", "NK-cell", "healthy", "none", "batch_2", 1400, 950, 2.8])

# Remove an element in a specific position and save the removed element
removed_element = scRNA_seq_metadata.pop(position)
for row in scRNA_seq_metadata:
    print(row)

# ['cell_id', 'sample_id', 'cell_type', 'condition', 'treatment', 'sequencing_batch', 'nUMI', 'nGene', 'percent_mt']
# ['cell_001', 'sample_A', 'T-cell', 'healthy', 'none', 'batch_1', 1200, 800, 2.5]
# ['cell_002', 'sample_A', 'B-cell', 'disease', 'drug_X', 'batch_1', 1500, 1000, 3.1]
# ['cell_003', 'sample_B', 'Monocyte', 'disease', 'drug_Y', 'batch_2', 1800, 1100, 4.0]

# Locate the first element
scRNA_seq_metadata[0]

# Locate the last element
scRNA_seq_metadata[-1]

# Locate the penultimate 倒数第二的 element
scRNA_seq_metadata[-2]
