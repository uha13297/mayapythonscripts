import random
import maya.cmds as cmds

# Create the window UI
Ran = cmds.window("Randomizer", t="Randomizer Ver 0.01", w=300, h=200)
cmds.columnLayout(adj=True)
cmds.separator(h=10)
cmds.text("Welcome to Attribute Randomizer")
cmds.separator(h=10)

# Sliders for translate, rotate, and scale
AttRanT = cmds.intSliderGrp(label="Translate", min=-5, max=5, field=True)
AttRanR = cmds.intSliderGrp(label="Rotate", min=-5, max=5, field=True)
AttRanS = cmds.intSliderGrp(label="Scale", min=-100, max=100, field=True)

# Randomize button
cmds.button(l="Randomize", c="main()")

cmds.showWindow(Ran)


def get_attr_value(ctrl):
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Please select a controller to randomize.")

    attr_list = cmds.listAttr(selection, keyable=True)
    return attr_list


def main():
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Please select a control to randomize.")
        return

    ctrl = selection[0]

    # Query slider values
    AR_T = cmds.intSliderGrp(AttRanT, q=True, value=True)
    AR_R = cmds.intSliderGrp(AttRanR, q=True, value=True)
    AR_S = cmds.intSliderGrp(AttRanS, q=True, value=True)

    # Apply randomization
    trans_randomized(ctrl, AR_T)
    rot_randomized(ctrl, AR_R)
    scale_randomized(ctrl, AR_S)


def trans_randomized(ctrl, translate_range):
    attrs = ["translateX", "translateY", "translateZ"]
    for attr in attrs:
        random_attr_value = random.uniform(-translate_range, translate_range)
        full_attr_name = f"{ctrl}.{attr}"
        cmds.setAttr(full_attr_name, random_attr_value)


def rot_randomized(ctrl, rotate_range):
    attrs = ["rotateX", "rotateY", "rotateZ"]
    for attr in attrs:
        random_attr_value = random.uniform(-rotate_range, rotate_range)
        full_attr_name = f"{ctrl}.{attr}"
        cmds.setAttr(full_attr_name, random_attr_value)


def scale_randomized(ctrl, scale_range):
    attrs = ["scaleX", "scaleY", "scaleZ"]
    for attr in attrs:
        random_attr_value = random.uniform(0.1, scale_range)  # Prevent negative scale
        full_attr_name = f"{ctrl}.{attr}"
        cmds.setAttr(full_attr_name, random_attr_value)
