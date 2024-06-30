# What does this code do ? 
# DESCRIPTION : It matches the translate of the imported rigs to the set selected
# What does a user need to provide ? 
# DESC: the user needs to select the set and run the script to transform the rigs to the desired set
# How to  run the script ? 
# DESC: copy this script into your python tab of the script editor and press run ; ideally can make a shelf button for it too
# Assumptions made in the script:
# This code assumes that you have already imported the child object into Maya scene.
# You can provide a list of all child objects to be transformed in the child_object_list below. 
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
        

