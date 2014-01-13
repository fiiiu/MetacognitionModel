
import numpy as np
import pymc


data=np.loadtxt('Data/wager_performance.csv')
nkids=data.shape[0]

#theta=np.empty(data.shape[0], dtype=object)
# k=np.empty(data.shape, dtype=object)
# for i in range(data.shape[0]):
#     theta[i]=pymc.Uniform('theta_{0}'.format(i), lower=0, upper=1)
#     for j in range(data.shape[1]):
#         k[i][j]=pymc.Bernoulli('k_{0}{1}'.format(i,j), p=theta[i], value=data[i,j], observed=True)

theta=np.empty(nkids, dtype=object)
k=np.empty(nkids, dtype=object)
for i in range(nkids):
    theta[i]=pymc.Uniform('theta_{0}'.format(i), lower=0, upper=1)
    k[i]=pymc.Bernoulli('k_{0}'.format(i), p=theta[i], value=data[i], observed=True)


data=np.array([[1, 0, 1], [1, 1, 0]])
s=[[[0.2, 0.8], [0.5, 0.4], [0.3, 0.9]], [[0.9, 0.8], [0.8, 0.4], [0.3, 0.9]]]
nkids=data.shape[0]
ntrials=data.shape[1]
sigma=np.empty(nkids, dtype=object)
x=np.empty((nkids,ntrials,2), dtype=object)
r=np.empty((nkids,ntrials), dtype=object)
for i in range(nkids):
    sigma[i]=pymc.Uniform('sigma_{0}'.format(i), lower=0, upper=100)
    for j in range(ntrials):
        x[i,j]=pymc.Normal('x_{0}{1}'.format(i,j), mu=s[i][j], tau=sigma[i]**-2)
        #r[i,j]=x[i,j][0]#np.argmax(x[i,j])
        @deterministic
        def r(y):
            np.argmax(y)