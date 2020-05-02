# -*- coding: utf-8 -*-
# Generated by codesnippet sphinx extension on 2020-05-03

import mdp
import numpy as np
np.random.seed(0)
node1 = mdp.nodes.PCANode(input_dim=100, output_dim=10)
node2 = mdp.nodes.SFANode(input_dim=100, output_dim=20)
layer = mdp.hinet.Layer([node1, node2])
layer
# Expected:
## Layer(input_dim=200, output_dim=30, dtype=None)

node1_1 = mdp.nodes.PCANode(input_dim=100, output_dim=50)
node1_2 = mdp.nodes.SFANode(input_dim=50, output_dim=10)
node1_flow = mdp.Flow([node1_1, node1_2])
node1 = mdp.hinet.FlowNode(node1_flow)
layer = mdp.hinet.Layer([node1, node2])
layer
# Expected:
## Layer(input_dim=200, output_dim=30, dtype=None)

switchboard = mdp.hinet.Switchboard(input_dim=6, connections=[0,1,2,3,4,3,4,5])
switchboard
# Expected:
## Switchboard(input_dim=6, output_dim=8, dtype=None)
x = mdp.numx.array([[2,4,6,8,10,12]])
switchboard.execute(x)
# Expected:
## array([[ 2,  4,  6,  8, 10,  8, 10, 12]])

mdp.hinet.show_flow(flow)

switchboard = mdp.hinet.Rectangular2dSwitchboard(in_channels_xy=(50, 50),
                                                 field_channels_xy=(10, 10),
                                                 field_spacing_xy=(5, 5),
                                                 in_channel_dim=3)
sfa_dim = 48
sfa_node = mdp.nodes.SFANode(input_dim=switchboard.out_channel_dim,
                             output_dim=sfa_dim)
sfa2_dim = 32
sfa2_node = mdp.nodes.SFA2Node(input_dim=sfa_dim,
                               output_dim=sfa2_dim)
flownode = mdp.hinet.FlowNode(mdp.Flow([sfa_node, sfa2_node]))
sfa_layer = mdp.hinet.CloneLayer(flownode,
                                 n_nodes=switchboard.output_channels)
flow = mdp.Flow([switchboard, sfa_layer])
