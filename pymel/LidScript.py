from pymel.core import *

def manageEyeLids(side):
    #Full Lid Management
    if getAttr('Eyes_controller.'+side+'FullyClosed'):
        #set the partial lids attributes to hidden so the meshes can actually be hidden later
        setAttr('Eyes_controller.'+side+'TopLid', 'hidden')
        setAttr('Eyes_controller.'+side+'BotLid', 'hidden')
        #bring the full lid mesh out using the rigs anchor
        anchor_pos = general.PyNode('j_'+side+'_top_eyelid_anchor').getTranslation(space='world')
        move('j_'+side+'_eyelid_full', anchor_pos, ws=True)
        scale('j_'+side+'_eyelid_full', [1,1,1])
    else:
        #place the full lid mesh hidden inside the body on the mid joint and scale it
        mid_joint_pos  = general.PyNode('j_mid').getTranslation(space='world')
        move('j_'+side+'_eyelid_full', mid_joint_pos, ws=True)
        scale('j_'+side+'_eyelid_full', [0,0,0])
        
    #Top Lid Management
    if getAttr('Eyes_controller.'+side+'TopLid') == 'hidden':
        #place the top lid meshes hidden inside the body on the mid joint and scale it
        mid_joint_pos  = general.PyNode('j_mid').getTranslation(space='world')
        move('j_'+side+'_eyelid_top_h_anchor', mid_joint_pos, ws=True)
        scale('j_'+side+'_eyelid_top_h_anchor', [0,0,0])
        scale('j_'+side+'_eyelid_top_half', [0,0,0])
        move('j_'+side+'_eyelid_top_q_anchor', mid_joint_pos, ws=True)
        scale('j_'+side+'_eyelid_top_q_anchor', [0,0,0])
        scale('j_'+side+'_eyelid_top_quarter', [0,0,0])
    if getAttr('Eyes_controller.'+side+'TopLid') == 'quarter':
        #Move the correct lid out onto the anchor and hide the other
        mid_joint_pos = general.PyNode('j_mid').getTranslation(space='world')
        anchor_pos = general.PyNode('j_'+side+'_top_eyelid_anchor').getTranslation(space='world')
        move('j_'+side+'_eyelid_top_q_anchor', anchor_pos, ws=True)
        scale('j_'+side+'_eyelid_top_q_anchor', [1,1,1])
        scale('j_'+side+'_eyelid_top_quarter', [1,1,1])
        move('j_'+side+'_eyelid_top_h_anchor', mid_joint_pos, ws=True)
        scale('j_'+side+'_eyelid_top_h_anchor', [0,0,0])
        scale('j_'+side+'_eyelid_top_half', [0,0,0])
    if getAttr('Eyes_controller.'+side+'TopLid') == 'half':
        #Move the correct lid out onto the anchor and hide the other
        mid_joint_pos = general.PyNode('j_mid').getTranslation(space='world')
        anchor_pos = general.PyNode('j_'+side+'_top_eyelid_anchor').getTranslation(space='world')
        move('j_'+side+'_eyelid_top_h_anchor', anchor_pos, ws=True)
        scale('j_'+side+'_eyelid_top_h_anchor', [1,1,1])
        scale('j_'+side+'_eyelid_top_half', [1,1,1])
        move('j_'+side+'_eyelid_top_q_anchor', mid_joint_pos, ws=True)
        scale('j_'+side+'_eyelid_top_q_anchor', [0,0,0])
        scale('j_'+side+'_eyelid_top_quarter', [0,0,0])
        
scriptJob(killAll=True)

scriptJob(attributeChange=['Eyes_controller.rFullyClosed', "manageEyeLids('r')"])
scriptJob(attributeChange=['Eyes_controller.rTopLid', "manageEyeLids('r')"])
scriptJob(attributeChange=['Eyes_controller.rBotLid', "manageEyeLids('r')"])

scriptJob(attributeChange=['Eyes_controller.lFullyClosed', "manageEyeLids('l')"])
scriptJob(attributeChange=['Eyes_controller.lTopLid', "manageEyeLids('l')"])
scriptJob(attributeChange=['Eyes_controller.lBotLid', "manageEyeLids('l')"])