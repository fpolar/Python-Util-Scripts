#This approach of setting driven keys has been the best preforming approach so far because it works locally on the bones and works using offset from their current position, making the eye transforns work correctly even if other controls/joints are rotated or translated

from pymel.core import *

cut_key_flag = True
set_driven_key_flag = True

sides = ['l', 'r']
verts = ['_top_', '_bot_']
#lid_names = ['tip', 'mid', 'front', 'outer', 'inner']
lid_names = ['mid', 'front', 'outer', 'inner']
lid_names_to_modifiers = {'mid':{'tx':1.5, 'scale':.2}, 'front':{'ty':1.5}, 'outer':{'ty':1.5}, 'inner':{'ty':1.5}}
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
        if cut_key_flag:
            cutKey(curr_joint.ty)
        if set_driven_key_flag:
            drivenValueLow = driverBaseValue * drivenMultiplier * -1 * side_flip_flag + curr_joint.ty.get()
            drivenValueHigh = driverBaseValue * drivenMultiplier * side_flip_flag + curr_joint.ty.get()
            setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue*-1, v=drivenValueLow)
            setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)
    for vert in verts:
        for c in range(0,len(lid_names)):
            curr_joint = PyNode('j_'+side+vert+'eyelid_'+lid_names[c])
            curr_control = PyNode(side+vert+'eyelid_controls|'+lid_names[c]+'_selector')
            curr_joint_attr = curr_joint.ty
            if lid_names[c] == 'mid':
                curr_joint_attr = curr_joint.tx
                side_flip_flag *= -1
            #geometry constraint slider
            if cut_key_flag:
                cutKey(curr_joint_attr)
            if set_driven_key_flag:
                #vertical eyelid movement
                drivenValueLow = driverBaseValue * drivenMultiplier * -1 * side_flip_flag + curr_joint_attr.get()
                drivenValueHigh = driverBaseValue * drivenMultiplier * side_flip_flag + curr_joint_attr.get()
                setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=-1*driverBaseValue, v=drivenValueLow)
                setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)
            if lid_names[c] == 'front':
                #trying to stick eyelids to eye without geo constraint
                zDrivenMultiplier = .2
                curr_joint_attr = curr_joint.tz
                drivenValueLow = -1 * driverBaseValue * zDrivenMultiplier + curr_joint_attr.get()
                drivenValueMid = curr_joint_attr.get()
                setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=-1*driverBaseValue, v=drivenValueLow)
                setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=0, v=drivenValueMid)
                setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueLow)
            if lid_names[c] == 'mid':
                side_flip_flag *= -1
