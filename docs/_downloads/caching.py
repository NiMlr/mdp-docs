# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-13

import mdp
import numpy as np
np.random.seed(0)
import mdp
import numpy as np
from timeit import Timer
x = np.random.rand(3000,1000)
pca_node = mdp.nodes.PCANode()
pca_node.train(x)
pca_node.stop_training()

timer = Timer("pca_node.execute(x)", "from __main__ import pca_node, x")
mdp.caching.set_cachedir("/tmp/my_cache")
mdp.activate_extension("cache_execute")
print timer.repeat(1, 1)[0], 'sec'
# Expected:
## 1.188946008682251 sec
print timer.repeat(1, 1)[0], 'sec'
# Expected:
## 0.112375974655 sec
mdp.deactivate_extension("cache_execute")
print timer.repeat(1, 1)[0], 'sec'
# Expected:
## 0.801102161407 sec

mdp.caching.activate_caching(cachedir='/tmp/my_cache',
    cache_classes=[mdp.nodes.SFANode, mdp.nodes.FDANode],
    cache_instances=[pca_node])
mdp.caching.deactivate_caching()

with mdp.caching.cache(cachedir='/tmp/my_cache', cache_instances=[pca_node]):
    # in the block, the cache is active
    print timer.repeat(1, 1)[0], 'sec'
# Expected:
## 0.101263999939 sec
print timer.repeat(1, 1)[0], 'sec'
# Expected:
## 0.801436901093 sec
