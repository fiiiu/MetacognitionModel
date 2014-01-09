

import numpy as np
import pymc


data=np.loadtxt('Data/wager_performance.csv')
stimulus=np.loadtxt('Data/wager_scale.csv')

nkids=data.shape[0]
#theta=np.empty(data.shape[0], dtype=object)
s=np.empty(data.shape, dtype=object)
x=np.empty((nkids, data.shape[1], 9), dtype=object)
sigma=np.empty(nkids, dtype=object)
k=np.empty(data.shape, dtype=object)

for i in range(nkids):
    #theta[i]=pymc.Uniform('theta_{0}'.format(i), lower=0, upper=1)
    sigma[i]=pymc.Uniform('sigma_{0}'.format(i), lower=0, upper=100)
    x[i]=pymc.Normal('x_{0}'.format(i), mu=parameters.get_sizes(stimulus[i]))
    k[i]=


    for j in range(data.shape[1]):
        s[i][j]=
        k[i][j]=pymc.Bernoulli('k_{0}{1}'.format(i,j), p=theta[i], value=data[i,j], observed=True)
        x[i][j]=pymc.Normal('x_{0}{1}'.format(i,j), mu=s[i,j], tau=sigma[i]**-2)

        @pymc.deterministic
        k[i][j]=


    # @pymc.deterministic(name='time_model_%s' % ID,plot=False)
    # def line_model(xx=datax,slope=slopeArr[i],avg=offsetArr[i]):
    #     return slope*xx + avg

@pymc.deterministic
def k(x):
    index=np.argmax(x)
    external_index=np.argmax(parameters.get_sizes(s???))
