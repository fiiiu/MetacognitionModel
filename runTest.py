

import pymc
import matplotlib.pyplot as plt
import testBernoulliModel
import numpy as np

model=pymc.MCMC(testBernoulliModel)

model.sample(iter=1000, burn=100, thin=5)

n_subs=testBernoulliModel.data.shape[0]
data_means=np.empty(n_subs, dtype=float)
model_means=np.empty(n_subs, dtype=float)

for i in range(n_subs):
    data_means[i]=np.mean(testBernoulliModel.data[i])
    #model_means[i]=np.mean(model.trace('theta_{0}'.format(i))[:])
    model_means[i]=np.mean(model.trace('theta_{0}'.format(i))[:])

 
#print model_means, data_means

# plt.plot(data_means, model_means, 'ks')
# plt.show()

plt.hist(model.trace('theta_0')[:])
plt.show()