# What does this code do ? 
# DESCRIPTION : It matches the translate of the imported rigs to the set selected
# What does a user need to do to run the script ? 
# DESCRIPTION: User needs to provide a list of rigs to translate into the LIST "child_object_list".
#              User needs to select the set and run the script to transform the rigs to the desired set.
# How to  run the script ?
# DESCRIPTION: copy this script into your python tab of the script editor and press run
# Assumptions made in the script:
# DESCRIPTION: This code assumes that you have already imported/referenced the child object into Maya scene.

import maya.cmds as cmds

child_object_list = ['zelda_V001_008:Bip001_GLOBAL', 'link_V001_004:Bip001_GLOBAL' , 'ganon_V001_002_file011:Bip001_GLOBAL']
selected_objects = cmds.ls(selection=True)
if selected_objects:
    parent_object = selected_objects[0]      
    # Query the world space transformation matrix of the parent object
    parent_transform = cmds.xform(parent_object, query=True, matrix=True, worldSpace=True)
    for child_obj in child_object_list:
        # Apply the same transformation matrix to zelda_V001_008:Bip001_GLOBAL
        cmds.xform(child_obj, matrix=parent_transform, worldSpace=True)       
        
