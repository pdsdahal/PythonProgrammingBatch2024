import numpy as np

one_dim = np.array([13, 10, 12, 22])
print(one_dim)
print("Total Sum : ", np.sum(one_dim))
print("Min : ", np.min(one_dim))
print("Max : ", np.max(one_dim))
print("Mean : ", np.mean(one_dim))
print("Median : ", np.median(one_dim))
print("Standard Deviation : ", np.std(one_dim))
print("Variance : ", np.var(one_dim))

# 10, 12, 13,22
# (40/100) * (4+1) = 2
# 12
# If you are in the 30th percentile, it means that 30% of the values in the group are below you,
# and 70% are above you.
print("Percentile : ", np.percentile(one_dim, 40))

# The cumulative sum is a sequence of sums where each sum includes all previous numbers up to that point in a dataset.
print("Cumulative Sum : ", np.cumsum(one_dim))
