from collections import Counter
import math


# Calculate entropy
def entropy(data):


    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


# Calculate information gain
def info_gain(data, index):


    total_entropy = entropy(data)
    values = set(row[index] for row in data)
    weighted_entropy = 0
    for val in values:
        subset = [row for row in data if row[index] == val]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    return total_entropy - weighted_entropy


# ID3 algorithm
def id3(data, features):


    labels = [row[-1] for row in data]
    # Stop if all labels are same
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    # Stopif no features left
    if not features:
        return Counter(labels).most_common(1)[0][0]
    # Find best feature
    gains = [info_gain(data, i) for i in range(len(features))]
    best_index = gains.index(max(gains))
    best_feature = features[best_index]
    tree = {best_feature: {}}
    feature_values = set(row[best_index] for row in data)
    for value in feature_values:
        subset = [row[:best_index] + row[best_index + 1:] for row in data if
                  row[best_index] == value]
        sub_features = features[:best_index] + features[best_index + 1:]
        tree[best_feature][value] = id3(subset, sub_features)
    return tree
#
# Exampledatasets
#
# Underfitting example (all same label)
under_data = [
    ['A', 'Yes'],
    ['B', 'Yes'],
    ['C', 'Yes'],
]
under_features = ['Feature']
print("Underfitting Tree:", id3(under_data, under_features))
# Overfitting example (noisy, over-specified)
over_data = [
    ['Red', 'Round', 'Big', 'Yes'],
    ['Blue', 'Round', 'Small', 'No'],
    ['Red', 'Square', 'Big', 'Yes'],
    ['Blue', 'Square', 'Small', 'No'],
    ['Green', 'Round', 'Small', 'Yes'],
]
over_features = ['Color', 'Shape', 'Size']
print("Overfitting Tree:", id3(over_data, over_features))
# Balancedexample
balanced_data = [
    ['Sunny', 'Hot', 'High', 'No'],
    ['Overcast', 'Hot', 'High', 'Yes'],
    ['Rain', 'Mild', 'High', 'Yes'],
    ['Sunny', 'Cool', 'Normal', 'Yes'],
    ['Overcast', 'Cool', 'Normal', 'Yes'],
]
balanced_features = ['Weather', 'Temp', 'Humidity']
print("Balanced Tree:", id3(balanced_data, balanced_features))
