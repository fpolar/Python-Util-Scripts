from pymel.core import *

sides = ['l', 'r']
verts = ['_top_', '_bot_']
#lid_names = ['tip', 'mid', 'front', 'outer', 'inner']
lid_names = ['front', 'outer', 'inner']
brow_names = ['inner', 'mid', 'outer', 'notch']
brow_long_names = ['inner', 'mid', 'outer', 'inner_selector|notch']

driverBaseValue = 1.5
drivenMultiplier = 1.5

for side in sides:
    side_flip_flag = 1
    if side == 'r':
        side_flip_flag = -1
    for b in range(0,len(brow_names)):
        curr_joint = PyNode('j_'+side+'_eyebrow_'+brow_names[b])
        curr_control = PyNode(side+'_eyebrow_controls|'+brow_long_names[b]+'_selector')
        select(curr_joint)
        delete(cn=True)
        cutKey(curr_joint.ty)
        drivenValueLow = driverBaseValue * drivenMultiplier * -1 * side_flip_flag + curr_joint.ty.get()
        drivenValueHigh = driverBaseValue * drivenMultiplier * side_flip_flag + curr_joint.ty.get()
        setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue*-1, v=drivenValueLow)
        setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)
    for vert in verts:
        for c in range(0,len(lid_names)):
            curr_joint = PyNode('j_'+side+vert+'eyelid_'+lid_names[c])
            curr_control = PyNode(side+vert+'eyelid_controls|'+lid_names[c]+'_selector')
            #geometry constraint slider
            select(curr_joint)
            delete(cn=True)
            cutKey(curr_joint.ty)
            drivenValueLow = driverBaseValue * drivenMultiplier * -1 * side_flip_flag + curr_joint.ty.get()
            drivenValueHigh = driverBaseValue * drivenMultiplier * side_flip_flag + curr_joint.ty.get()
            setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=-1*driverBaseValue, v=drivenValueLow)
            setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)
