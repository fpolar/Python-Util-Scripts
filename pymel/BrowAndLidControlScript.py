from pymel.core import *

selectedNodes = selected()
joints = []
controls = []

for node in selectedNodes:
    if str(node.nodeType()) == 'joint':
        joints.append(node)
    else:
        controls.append(node)

sides = ['l', 'r']
verts = ['_top_', '_bot_']
children = ['tip', 'mid', 'front', 'outer', 'inner']
children_heirarchy = ['tip_controller', 'tip_controller|mid_controller', 'tip_controller|mid_controller|front_controller', 'tip_controller|mid_controller|outer_controller', 'tip_controller|mid_controller|inner_controller']
for side in sides:
    for vert in verts:
        for c in range(0,len(children)):
            curr_joint = PyNode('j_'+side+vert+'eyelid_'+children[c])
            curr_control = PyNode(side+vert+'lid_controls|'+children_heirarchy[c])
            select(curr_joint)
            delete(cn=True)
            pointConstraint(curr_control, curr_joint, mo=True)
            orientConstraint(curr_control, curr_joint, mo=True)
            #if children[c] == 'front' or children[c] == 'inner' or children[c] == 'outer':
                #geometryConstraint(PyNode(side+'_eye'), curr_joint)
            if children[c] == 'mid':
                scaleConstraint(curr_control, curr_joint, mo=True)
            delete(cn=True)
