from pymel.core import *

scriptJob(killAll=True)

rFullJob = scriptJob(attributeChange=['Eyes_controller.rFullyClosed', "manageEyeLids('r')"])
rTopJob = scriptJob(attributeChange=['Eyes_controller.rTopLid', "manageEyeLids('r')"])
rBotJob = scriptJob(attributeChange=['Eyes_controller.rBotLid', "manageEyeLids('r')"])

lFullJob = scriptJob(attributeChange=['Eyes_controller.lFullyClosed', "manageEyeLids('l')"])
lTopJob = scriptJob(attributeChange=['Eyes_controller.lTopLid', "manageEyeLids('l')"])
lBotJob = scriptJob(attributeChange=['Eyes_controller.lBotLid', "manageEyeLids('l')"])

def manageEyeLids(side):
    global rTopJob
    global lTopJob
    global rBotJob
    global lBotJob
  
    
    eyeScale = eyeScaleToLidSpace(side)
    #Full Lid Management
    if getAttr('Eyes_controller.'+side+'FullyClosed'):
        #set the partial lids attributes to hidden so the meshes can actually be hidden later
        #The partial lid jobs endlessly run if they aren't killed and remade before setting them here
        #would like cleaner solution to this, but from what I can tell in the docs, none are supported
        scriptJob( kill=rTopJob, force=True)
        scriptJob( kill=lTopJob, force=True)
        #setAttr('Eyes_controller.'+side+'TopLid', 0)
        setAttr('Eyes_controller.'+side+'TopLid', 'hidden')
        lTopJob = scriptJob(attributeChange=['Eyes_controller.lTopLid', "manageEyeLids('l')"])
        rTopJob = scriptJob(attributeChange=['Eyes_controller.rTopLid', "manageEyeLids('r')"])
        scriptJob( kill=rBotJob, force=True)
        scriptJob( kill=lBotJob, force=True)
        setAttr('Eyes_controller.'+side+'BotLid', 0)
        lBotJob = scriptJob(attributeChange=['Eyes_controller.lBotLid', "manageEyeLids('l')"])
        rBotJob = scriptJob(attributeChange=['Eyes_controller.rBotLid', "manageEyeLids('r')"])
        #bring the full lid mesh out using the rigs anchor
        anchor_world_transform = general.PyNode('j_'+side+'_top_eyelid_anchor').getMatrix(worldSpace=True)
        general.PyNode('j_'+side+'_eyelid_full').setMatrix(anchor_world_transform, worldSpace=True)
        scale('j_'+side+'_eyelid_full', eyeScale)
        parent( 'j_'+side+'_eyelid_full', 'j_'+side+'_top_eyelid_anchor' )
    else:
        #place the full lid mesh hidden inside the body on the mid joint and scale it
        mid_joint_pos  = general.PyNode('j_mid').getTranslation(space='world')
        move('j_'+side+'_eyelid_full', mid_joint_pos, ws=True)
        scale('j_'+side+'_eyelid_full', [0,0,0])
        parent( 'j_'+side+'_eyelid_full', 'j_mid' )
    
    #Partial Lid Management
    capital = ['Top', 'Bot']
    lowercase = ['top', 'bot']
    for i in range(2):
        if getAttr('Eyes_controller.'+side+capital[i]+'Lid') == 0: #0 is hidden
            #place the top lid meshes hidden inside the body on the mid joint and scale it
            mid_joint_pos  = general.PyNode('j_mid').getTranslation(space='world')
            move('j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', mid_joint_pos, ws=True)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', [0,0,0])
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_half', [0,0,0])
            parent( 'j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', 'j_mid' )
            move('j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', mid_joint_pos, ws=True)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', [0,0,0])
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_quarter', [0,0,0])
            parent( 'j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', 'j_mid' )
            #controllers
            setAttr(side+'_'+lowercase[i]+'_half_lid_controller.visibility', 0)
            setAttr(side+'_'+lowercase[i]+'_quarter_lid_controller.visibility', 0)
            
        if getAttr('Eyes_controller.'+side+capital[i]+'Lid') == 1: #1 is quarter
            #Move the correct lid out onto the anchor and hide the other
            mid_joint_pos = general.PyNode('j_mid').getTranslation(space='world')
            
            anchor_world_transform = general.PyNode('j_'+side+'_'+lowercase[i]+'_eyelid_anchor').getMatrix(worldSpace=True)
            general.PyNode('j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor').setMatrix(anchor_world_transform, worldSpace=True)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', eyeScale)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_quarter', eyeScale)
            parent( 'j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', 'j_'+side+'_'+lowercase[i]+'_eyelid_anchor' )
            
            move('j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', mid_joint_pos, ws=True)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', [0,0,0])
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_half', [0,0,0])
            parent( 'j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', 'j_mid' )
            #controllers
            setAttr(side+'_'+lowercase[i]+'_half_lid_controller.visibility', 0)
            setAttr(side+'_'+lowercase[i]+'_quarter_lid_controller.visibility', 1)
            
        if getAttr('Eyes_controller.'+side+capital[i]+'Lid') == 2: #2 is half
            #Move the correct lid out onto the anchor and hide the other
            mid_joint_pos = general.PyNode('j_mid').getTranslation(space='world')
            
            anchor_world_transform = general.PyNode('j_'+side+'_'+lowercase[i]+'_eyelid_anchor').getMatrix(worldSpace=True)
            general.PyNode('j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor').setMatrix(anchor_world_transform, worldSpace=True)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', eyeScale)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_half', eyeScale)
            parent( 'j_'+side+'_eyelid_'+lowercase[i]+'_h_anchor', 'j_'+side+'_'+lowercase[i]+'_eyelid_anchor' )
            
            move('j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', mid_joint_pos, ws=True)
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', [0,0,0])
            scale('j_'+side+'_eyelid_'+lowercase[i]+'_quarter', [0,0,0])
            parent( 'j_'+side+'_eyelid_'+lowercase[i]+'_q_anchor', 'j_mid' )
            #controllers
            setAttr(side+'_'+lowercase[i]+'_half_lid_controller.visibility', 1)
            setAttr(side+'_'+lowercase[i]+'_quarter_lid_controller.visibility', 0)
    select( 'Eyes_controller', visible=True)
    
#Retrieves scale transform done on the 'side' eye joint
#Returns a transform vector that can apply the same transform on a lid
#eye: X Y Z
#lid: Z Y X
#note: on future rigs orienting the joints more carefully could be better
def eyeScaleToLidSpace(side):
    eyeScale = general.PyNode('j_'+side+'_eye').getScale()
    return [eyeScale[2], eyeScale[1], eyeScale[0]]