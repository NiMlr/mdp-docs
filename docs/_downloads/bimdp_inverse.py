# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-13

import mdp
import numpy as np
np.random.seed(0)
import numpy as np
import bimdp

pca_node = bimdp.nodes.PCABiNode()
sfa_node = bimdp.nodes.SFABiNode()
flow = pca_node + sfa_node
x = np.random.random((50,5))
flow.train(x)

x = np.random.random((3,5))
y, msg = flow.execute(x)

inv_x, _ = flow.execute(y, {"method": "inverse"}, 1)
assert np.all(np.abs(x - inv_x) < 0.0000001)

inv2_x = flow.inverse(y)
assert np.all(np.abs(inv2_x - inv_x) < 0.0000001)
