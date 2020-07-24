 #This approach of setting driven keys has been the best preforming approach so far because it works locally on the bones and works using offset from their current position, making the eye transforns work correctly even if other controls/joints are rotated or translated

from pymel.core import *

cut_key_flag = True
set_driven_key_flag = True

sides = ['l', 'r']
verts = ['top', 'bot']
#if this gets too bloated, read from json file
control_transform_dict = {'eyebrow':{'inner':{'inner':{'ty':1.5}}, 'mid':{'mid':{'ty':1.5}}, 'outer':{'outer':{'ty':1.5}}, 'notch':{'notch':{'ty':1.5}}}}
#lid_names = ['mid', 'front', 'outer', 'inner']
#lid_names_to_modifiers = {'mid':{'tx':1.5, 'sz':.2, 'sx':.2}, 'front':{'ty':1.5}, 'outer':{'ty':1.5}, 'inner':{'ty':1.5}}
#brow_names = ['inner', 'mid', 'outer', 'notch']
#brow_long_names = ['inner', 'mid', 'outer', 'inner_selector|notch']

driverBaseValue = 1.5
drivenMultiplier = 1.5

for side in sides:
    side_flip_flag = 1
    if side == 'r':
        side_flip_flag = -1
    #eyebrow control connections
    for b in range(0,len(brow_names)):
        curr_joint = PyNode('j_'+side+'_eyebrow_'+brow_names[b])
        curr_control = PyNode(side+'_eyebrow_controls|'+brow_long_names[b]+'_selector')
        if cut_key_flag:
            cutKey(curr_joint.ty)
        if set_driven_key_flag:
            drivenValueLow = driverBaseValue * drivenMultiplier * -1 + curr_joint.ty.get()
            drivenValueHigh = driverBaseValue * drivenMultiplier  + curr_joint.ty.get()
            setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue*-1, v=drivenValueLow)
            setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)
            
    #eyebrow control connections
    for vert in verts:
        for curr_spec in lid_names_to_modifiers:
            if curr_spec ==  'mid' and vert == '_top_':
                print(curr_spec, side_flip_flag)
                side_flip_flag *= -1
            elif side == 'r':
                side_flip_flag = -1
            print(curr_spec, side_flip_flag)
            print(lid_names_to_modifiers[curr_spec])
            curr_joint = PyNode('j_'+side+'_'+vert+'_eyelid_'+curr_spec)
            curr_control = PyNode(side+'_'+vert+'_eyelid_controls|'+curr_spec+'_selector')
            for curr_attr in lid_names_to_modifiers[curr_spec]:
                print(side, side_flip_flag)
                curr_joint_attr = eval('curr_joint.'+curr_attr)
                curr_multiplier = lid_names_to_modifiers[curr_spec][curr_attr] 
                if cut_key_flag:
                    cutKey(curr_joint_attr)
                if set_driven_key_flag:
                        drivenValueLow = driverBaseValue * curr_multiplier * -1 * side_flip_flag + curr_joint_attr.get()
                        drivenValueHigh = driverBaseValue * curr_multiplier * side_flip_flag + curr_joint_attr.get()
                        setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=-1*driverBaseValue, v=drivenValueLow)
                        setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)
            #if lid_names[c] == 'front':
            #    #trying to stick eyelids to eye without geo constraint
            #    zDrivenMultiplier = .2
            #    curr_joint_attr = curr_joint.tz
            #    drivenValueLow = -1 * driverBaseValue * zDrivenMultiplier + curr_joint_attr.get()
            #    drivenValueMid = curr_joint_attr.get()
            #    setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=-1*driverBaseValue, v=drivenValueLow)
            #    setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=0, v=drivenValueMid)
            #    setDrivenKeyframe(curr_joint_attr, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueLow)
