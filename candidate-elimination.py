
def more_general(h1, h2):


    """Check if h1 is more general than h2."""
    return all(x == '?' or x == y for x, y in zip(h1, h2))


def candidate_elimination(data, labels):


    """Performs Candidate Elimination
    Algorithm."""
    n = len(data[0])
    S = data[0]  # Most specific
    # hypothesis
    G = ['?'] * n  # Most
    # general
    # hypothesis
    for i, instance in enumerate(data):
        if labels[i] == "Yes": 
            for j in range(n):
                if S[j] != instance[j]:
                    S[j] = '?'
            else:  # Negative Example
                G = [S[j] if S[j] != '?' else '?' for j in range(n)]
    return S, G
# Exampledataset (attributes and
# labels)
data = [
['Sunny', 'Warm', 'Normal'],
['Sunny', 'Warm', 'High'],
['Rainy', 'Cold', 'High'],
['Sunny', 'Warm', 'High']
]
labels = ["Yes", "Yes", "No", "Yes"]
# Run algorithm
S_final, G_final = candidate_elimination(data,labels)
print("Final Specific Hypothesis:",S_final)
print("Final General Hypothesis:",G_final)
