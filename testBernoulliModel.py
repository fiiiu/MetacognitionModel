
import numpy as np
import pymc


data=np.loadtxt('wager_performance_table.csv')

theta=np.empty(data.shape[0], dtype=object)
k=np.empty(data.shape, dtype=object)

for i in range(data.shape[0]):
    theta[i]=pymc.Uniform('theta_{0}'.format(i), lower=0, upper=1)
    for j in range(data.shape[1]):
        k[i][j]=pymc.Bernoulli('k_{0}{1}'.format(i,j), p=theta[i], value=data[i,j], observed=True)


