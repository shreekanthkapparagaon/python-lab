# Supervised Learning
from sklearn.linear_model import LinearRegression
import numpy as np
# Features: [Size in sq ft]
X=np.array([[1000], [1500], [2000], [2500]])
# Labels: [Price in $]
y =np.array([200000, 250000, 300000, 350000])
model = LinearRegression()
model.fit(X, y)
# Predict the price of a 1800 sq ft house
print(model.predict([[1800]]))




# Unsupervised Learning
from sklearn.cluster import KMeans
import numpy as np
# Features: [Spending score, Frequency]
X=np.array([[10, 2], [20, 3], [11, 2], [100, 8], [105, 7]])
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
# Print cluster labels
print(kmeans.labels_)


# Semi-Supervised Learning
from sklearn.semi_supervised import LabelSpreading
import numpy as np
# Unlabeled:-1
X=np.array([[1], [2], [3], [8], [9], [10]])
y =np.array([0, 0,-1,-1, 1, 1])
model = LabelSpreading()
model.fit(X, y)
# Predict labels for all data
print(model.transduction_)


# Reinforcement Learning
# import numpy as np
# Simple grid world: 3 states, 2 actions
Q=np.zeros((3, 2)) # Q-table
alpha = 0.1 # learning rate
gamma =0.9 # discount factor
reward = [0, 1, 10]
# Simulate one step: from state 0, take action 1, go to state 1
state = 0
action = 1
next_state = 1
# Q-learning update
Q[state, action] = Q[state, action] + alpha * (reward[next_state] + gamma *
np.max(Q[next_state])- Q[state, action])
print(Q)