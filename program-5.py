import numpy as np


# Function to calculate entropy
def entropy(y):


    values,counts=np.unique(y,return_counts = True)
    ent = 0
    n = len(y)
# Loop over each unique value and its count to compute the probability and its
#     contribution
# to
# entropy.
    for count in counts:
        p = count / float(n)
        if p > 0:
            ent -=p * np.log2(p)
    return ent


# Function to calculate information gain for a single feature column
def information_gain(X_column, y):
    parent_entropy = entropy(y)
    values, counts = np.unique(X_column, return_counts=True)
    weighted_entropy = 0.0
    n = len(y)
    # Loop over each unique value and compute the weighted entropy.
    for i in range(len(values)):
        v = values[i]
        weight = counts[i] / float(n)
        # Select the subset of y where the feature equals the value v.
        subset = y[X_column == v]
        weighted_entropy += weight * entropy(subset)  # Information gain is the reduction in entropy.
    return parent_entropy - weighted_entropy


# Function to find the best feature for splitting the data.
def best_feature(X, y):


    n_features=X.shape[1]
    best = -1
    best_ig = -1
    # Loop over each feature column and compute information gain.
    for i in range(n_features):
        ig = information_gain(X[:,i], y)
        if ig > best_ig:
            best_ig = ig
        best = i
    return best


# Function to build the decision tree using the ID3 algorithm.
def build_tree(X, y):
    # If all labels are the same, return that label.
    if len(set(y)) == 1:
        return int(y[0])
    # Choose the feature with the highest information gain.
    feature = best_feature(X,y)
    tree = {int(feature):{}}
    # Get unique values for the chosen feature.
    unique_values=np.unique(X[:, feature])
    for v in unique_values:
        # Create a mask for rows where the feature has value v.
        mask = X[:, feature] == v
        # Recursively build the subtree for this branch.\
        subtree = build_tree(X[mask],y[mask])
        tree[int(feature)][int(v)] = subtree
    return tree
# ANDGate Dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 0, 0, 1])  # AND operation results
# Train the decision tree using ID3
tree = build_tree(X, y)
# Print the decision tree
print("Decision Tree:", tree)
