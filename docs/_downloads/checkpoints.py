# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-13

import mdp
import numpy as np
np.random.seed(0)
def gen_data(blocks,dims):
    mat = np.random.random((dims,dims))-0.5
    for i in xrange(blocks):
        # put variables on columns and observations on rows
        block = mdp.utils.mult(np.random.random((1000,dims)), mat)
        yield block

pca = mdp.nodes.PCANode(output_dim=0.9)
exp = mdp.nodes.PolynomialExpansionNode(2)
sfa = mdp.nodes.SFANode()

class PCADimensionExceededException(Exception):
    """Exception base class for PCA exceeded dimensions case."""
    pass

class CheckPCA(mdp.CheckpointFunction):
    def __init__(self,max_dim):
        self.max_dim = max_dim
    def __call__(self,node):
        node.stop_training()
        act_dim = node.get_output_dim()
        if act_dim > self.max_dim:
            errstr = 'PCA output dimensions exceeded maximum '+\
                     '(%d > %d)'%(act_dim,self.max_dim)
            raise PCADimensionExceededException, errstr
        else:
            print 'PCA output dimensions = %d'%(act_dim)

flow = mdp.CheckpointFlow([pca, exp, sfa])

flow.train([gen_data(10, 50), None, gen_data(10, 50)],
           [CheckPCA(10), None, None])
# Expected:
## Traceback (most recent call last):
##   File "<stdin>", line 2, in ?
##   [...]
## __main__.PCADimensionExceededException: PCA output dimensions exceeded maximum (25 > 10)

flow[0] = mdp.nodes.PCANode(output_dim=0.9)
flow.train([gen_data(10, 12), None, gen_data(10, 12)],
           [CheckPCA(10), None, None])
# Expected:
## PCA output dimensions = 7

pca = mdp.nodes.PCANode(output_dim=0.9)
exp = mdp.nodes.PolynomialExpansionNode(2)
sfa = mdp.nodes.SFANode()
flow = mdp.CheckpointFlow([pca, exp, sfa])
flow.train([gen_data(10, 12), None, gen_data(10, 12)],
           [CheckPCA(10),
            None,
            mdp.CheckpointSaveFunction('dummy.pic',
                                       stop_training = 1,
                                       protocol = 0)])
# Expected:
## PCA output dimensions = 6

fl = file('dummy.pic')
import cPickle
sfa_reloaded = cPickle.load(fl)
sfa_reloaded
# Expected:
## SFANode(input_dim=27, output_dim=27, dtype='float64')

fl.close()
import os
os.remove('dummy.pic')
