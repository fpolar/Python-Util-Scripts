from pymel.core import *

l_lid_constraints = ['Eyes_constraint.lLidClosed', 'Eyes_constraint.LFullyClosed', 'l_eyelid_top_constraint.MeshOut', 'l_eyelid_bottom_constraint.MeshOut']
r_lid_constraints = ['Eyes_constraint.rLidClosed', 'Eyes_constraint.RFullyClosed', 'r_eyelid_top_constraint.MeshOut', 'r_eyelid_bottom_constraint.MeshOut']
l_lid_bones = ['l_eyelid_joint','l_eyelid_full','l_eyelid_top', 'l_eyelid_bottom']
r_lid_bones = ['r_eyelid_joint','r_eyelid_full','r_eyelid_top', 'r_eyelid_bottom']

constraint_lists = [l_lid_constraints, r_lid_constraints]
bones_lists = [l_lid_bones, r_lid_bones]
eye_bones = ['l_eye', 'r_eye']

def moveLids(side, full, left, right):
    if getAttr(constraint_lists[side][0]):
        print`"eye closed"`
        matchTransform(bones_lists[side][0], eye_bones[side])
    else:
        print`"eye open"`
        move(0,0,0, bones_lists[side][0], objectSpace=True)
        for constraint in constraint_list[side]:
            setAttr(constraint, false)

scriptJob(killAll=True)

scriptJob(attributeChange=['Eyes_constraint.rLidClosed', "moveLids(1, 0, 0, 0)"])
scriptJob(attributeChange=['Eyes_constraint.lLidClosed', "moveLids(1, 0, 0, 0)"])

            
    