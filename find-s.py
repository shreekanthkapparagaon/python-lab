# Find-s algorithm
def find_s_with_negatives(data, labels):
    h = data[0][:]  # Start with the first example, make a copy
    for i in range(1, len(data)):
        if labels[i] == "Yes":  # Positive example
            for j in range(len(h)):
                if h[j] != data[i][j]:
                    h[j] = '?'  # Generalize if attribute differs
                else:  # Negative example
                    for j in range(len(h)):
                        if h[j] == data[i][j]:
                            h[j] = '?'  # Remove matching attribute to avoid covering negatives
    return h


# Exampledataset
data = [
    ['Sunny', 'Warm', 'Normal'],
    ['Sunny', 'Warm', 'High'],
    ['Rainy', 'Cold', 'High'],
    ['Sunny', 'Warm', 'High']
]
labels = ["Yes", "Yes", "No", "Yes"]  # Run the modified
# Find-S algorithm
print(find_s_with_negatives(data, labels))
# Candidate
# elimination
# algorithm

