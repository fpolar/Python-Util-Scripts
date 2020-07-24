 #This approach of setting driven keys has been the best preforming approach so far because it works locally on the bones and works using offset from their current position, making the eye transforns work correctly even if other controls/joints are rotated or translated

from pymel.core import *

cut_key_flag = True
set_driven_key_flag = True

sides = ['l', 'r']
verts = ['top', 'bot']
#if this gets too bloated, read from json file
control_transform_dict = {'eyebrow':{'inner':{'inner':{'ty':1.5, 'rz':90}}, 'mid':{'mid':{'ty':1.5, 'rz':90}}, 'outer':{'outer':{'ty':1.5, 'rz':90}}, 'notch':{'notch':{'ty':1.5, 'rz':1.5}}}}
control_transform_dict['eyelid'] = {'mid':{'mid':{'ty':1.5}}, 'inner':{'inner':{'ty':1.5}}, 'front':{'front':{'ty':1.5}}, 'outer':{'outer':{'ty':1.5}}}

driverBaseValue = 1

for side in sides:
    flip_flag = 1
    if side == 'r':
        flip_flag = -1
    for curr_group_name in control_transform_dict:
        verts_mod = ['']
        if curr_group_name == 'eyelid':
            verts_mod = ['top_', 'bot_']
        else:
            flip_flag = 1
        for vert in verts_mod:
            for curr_control_name in control_transform_dict[curr_group_name]:
                curr_control = PyNode(side+'_'+vert+curr_group_name+'_controls|'+curr_control_name+'_selector')
                print(curr_control)
                for curr_joint_name in control_transform_dict[curr_group_name][curr_control_name]:
                    curr_joint = PyNode('j_'+side+'_'+vert+curr_group_name+'_'+curr_joint_name)
                    print(curr_joint)
                    for curr_attr_name in control_transform_dict[curr_group_name][curr_control_name][curr_joint_name]:
                        if 'r' in curr_attr_name:
                            driverBaseValue = 90
                        else:
                            driverBaseValue = 1
                        cutKey(eval('curr_joint.'+curr_attr_name))
                        curr_mult = control_transform_dict[curr_group_name][curr_control_name][curr_joint_name][curr_attr_name]
                        drivenValueLow = curr_mult * -1 * flip_flag + eval('curr_joint.'+curr_attr_name).get()
                        drivenValueHigh = curr_mult * flip_flag + eval('curr_joint.'+curr_attr_name).get()
                        setDrivenKeyframe(eval('curr_joint.'+curr_attr_name), cd=eval('curr_control.'+curr_attr_name), driverValue=driverBaseValue*-1, v=drivenValueLow)
                        setDrivenKeyframe(eval('curr_joint.'+curr_attr_name), cd=eval('curr_control.'+curr_attr_name), driverValue=driverBaseValue, v=drivenValueHigh)
                    #     curr_joint = PyNode('j_'+side+'_'+curr_group_name+'_'+curr_joint_name)
                    #     curr_control = PyNode(side+'_'+curr_group_name+'_controls|'+brow_long_names[b]+'_selector')
                    #     if cut_key_flag:
                    #         cutKey(curr_joint.ty)
                    #     if set_driven_key_flag:
                    #         drivenValueLow = driverBaseValue * drivenMultiplier * -1 + curr_joint.ty.get()
                    #         drivenValueHigh = driverBaseValue * drivenMultiplier  + curr_joint.ty.get()
                    #         setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue*-1, v=drivenValueLow)
                    #         setDrivenKeyframe(curr_joint.ty, cd=curr_control.ty, driverValue=driverBaseValue, v=drivenValueHigh)