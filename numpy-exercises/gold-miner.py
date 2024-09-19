#After a binge watching the discovery channel, you ditch your job as a trial lawyer to become a gold miner.
#You decide to prospect five locations underneath a 7x7 grid of land. How much gold do you uncover at each location?

import numpy as np

np.random.seed(5555)
gold = np.random.randint(low=0,high=10,size=(7,7))
print(gold)
locs = np.array([
    [0,4],
    [2,2],
    [5,1],
    [6,3]]
)
print(locs)

print(gold[locs[:,0], locs[:,1]])