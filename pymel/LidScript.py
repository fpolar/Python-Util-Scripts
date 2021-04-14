from pymel.core import *

#namespace for when model is referenced in a scene
#when the model is referenced the parent commands error
#for now the transforms of the eyes will have to be done before the lids are out
ns = selected()[0].namespace()

scriptJob(killAll=True)

rFullJob = scriptJob(attributeChange=[ns+'Eyes_controller.rFullyClosed', "manageEyeLids('r')"])
rTopJob = scriptJob(attributeChange=[ns+'Eyes_controller.rTopLid', "manageEyeLids('r')"])
rBotJob = scriptJob(attributeChange=[ns+'Eyes_controller.rBotLid', "manageEyeLids('r')"])

lFullJob = scriptJob(attributeChange=[ns+'Eyes_controller.lFullyClosed', "manageEyeLids('l')"])
lTopJob = scriptJob(attributeChange=[ns+'Eyes_controller.lTopLid', "manageEyeLids('l')"])
lBotJob = scriptJob(attributeChange=[ns+'Eyes_controller.lBotLid', "manageEyeLids('l')"])

#read any changes in the properties of the eyelid controller
#and call transformation functions on respective joints 
def manageEyeLids(side):

    controllerSelected = False
    if selected():
        constrollerSelected = (ns+'Eyes_controller') == selected()[0] 
    eyeScale = eyeScaleToLidSpace(side)
    #Full Lid Management
    if getAttr(ns+'Eyes_controller.'+side+'FullyClosed'):
        #bring the full lid mesh out using the rigs anchor
        anchor_world_transform = general.PyNode(ns+'j_'+side+'_top_eyelid_anchor').getMatrix(worldSpace=True)
        general.PyNode(ns+'j_'+side+'_eyelid_full').setMatrix(anchor_world_transform, worldSpace=True)
        if getAttr(ns+'Eyes_controller.'+side+'BotLid'):
            setAttr(ns+'Eyes_controller.'+side+'BotLid', 0)        
        if getAttr(ns+'Eyes_controller.'+side+'TopLid'):
            setAttr(ns+'Eyes_controller.'+side+'TopLid', 0)
        scale(ns+'j_'+side+'_eyelid_full', eyeScale)
        if not ns:
            parent(ns+'j_'+side+'_eyelid_full', ns+'j_'+side+'_top_eyelid_anchor' )
    else:
        #place the full lid mesh hidden inside the body on the mid joint and scale it
    	mid_joint_pos  = general.PyNode(ns+'j_mid').getTranslation(space='world')
        move(ns+'j_'+side+'_eyelid_full', mid_joint_pos, ws=True)
        scale(ns+'j_'+side+'_eyelid_full', [0,0,0])
        if not ns:
            parent(ns+'j_'+side+'_eyelid_full', ns+'j_mid' )
    
    #Partial Lid Management
    capital = ['Top', 'Bot']
    lowercase = ['top', 'bot']
    for i in range(2):
        if getAttr(ns+'Eyes_controller.'+side+capital[i]+'Lid') == 0: #0 is hidden
            #place the top lid meshes hidden inside the body on the mid joint and scale it
            shrinkLid(side, lowercase[i], 'half')
            shrinkLid(side, lowercase[i], 'quarter')
            #controllers
            setAttr(ns+side+'_'+lowercase[i]+'_half_lid_controller.visibility', 0)
            setAttr(ns+side+'_'+lowercase[i]+'_quarter_lid_controller.visibility', 0)
            
        if getAttr(ns+'Eyes_controller.'+side+capital[i]+'Lid') == 1: #1 is quarter
            #Move the correct lid out onto the anchor and hide the other
            
            anchor_world_transform = general.PyNode(ns+'j_'+side+'_'+lowercase[i]+'_eyelid_anchor').getMatrix(worldSpace=True)
            general.PyNode(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor').setMatrix(anchor_world_transform, worldSpace=True)
            scale(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', eyeScale)
            scale(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_quarter', eyeScale)
            if not ns:
                parent(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', ns+'j_'+side+'_'+lowercase[i]+'_eyelid_anchor' )
            
            shrinkLid(side, lowercase[i], 'half')
            #controllers
            setAttr(ns+side+'_'+lowercase[i]+'_half_lid_controller.visibility', 0)
            setAttr(ns+side+'_'+lowercase[i]+'_quarter_lid_controller.visibility', 1)
            
        if getAttr(ns+'Eyes_controller.'+side+capital[i]+'Lid') == 2: #2 is half
            #Move the correct lid out onto the anchor and hide the other
            
            anchor_world_transform = general.PyNode(ns+'j_'+side+'_'+lowercase[i]+'_eyelid_anchor').getMatrix(worldSpace=True)
            general.PyNode(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor').setMatrix(anchor_world_transform, worldSpace=True)
            scale(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', eyeScale)
            scale(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_half', eyeScale)
            if not ns:
                parent(ns+'j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', ns+'j_'+side+'_'+lowercase[i]+'_eyelid_anchor' )
            
            shrinkLid(side, lowercase[i], 'quarter')
            #controllers
            setAttr(ns+side+'_'+lowercase[i]+'_half_lid_controller.visibility', 1)
            setAttr(ns+side+'_'+lowercase[i]+'_quarter_lid_controller.visibility', 0)
    
    if controllerSelected: 
        select(ns+'Eyes_controller')        

#Retrieves scale transform done on the 'side' eye joint
#Returns a transform vector that can apply the same transform on a lid 
#eye orientation: X Y Z
#lid orientation: Z Y X
def eyeScaleToLidSpace(side):
    eyeScale = general.PyNode(ns+'j_'+side+'_eye').getScale()
    return [eyeScale[2], eyeScale[1], eyeScale[0]]

def shrinkLid(side, vert, size):
    mid_joint_pos  = general.PyNode(ns+'j_mid').getTranslation(space='world')
    move(ns+'j_'+side+'_eyelid_'+vert+'_'+size[0]+'_anchor', mid_joint_pos, ws=True)
    move(ns+'j_'+side+'_eyelid_'+vert+'_'+size, mid_joint_pos, ws=True)
    scale(ns+'j_'+side+'_eyelid_'+vert+'_'+size[0]+'_anchor', [0,0,0])
    scale(ns+'j_'+side+'_eyelid_'+vert+'_'+size, [0,0,0])
    if not ns:
        parent(ns+'j_'+side+'_eyelid_'+vert+'_'+size[0]+'_anchor', ns+'j_mid' )