# Sensitivity
def sensitivity(true_positives, false_negatives):
    """
    Calculates the sensitivity (recall) of a binary classifier.
    Args:
        true_positives: Number of correctly classified positive cases.
        false_negatives: Number of incorrectly classified positive cases.
    Returns:
        The sensitivity (recall) as a float between 0 and 1.
    """
    if true_positives + false_negatives == 0:
        return 0.0
    else:
        return true_positives / (true_positives + false_negatives)

true_positives = 100
false_negatives = 10
sensitivity_score = sensitivity(true_positives, false_negatives)
print("Sensitivity (Recall):", sensitivity_score)

# Specificity

# F-1 score

# AUC
