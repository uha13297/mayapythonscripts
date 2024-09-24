import maya.cmds as cmds

def tweener(tween_perc):
    selection = cmds.ls(selection=True)
    current_frame = cmds.currentTime(query=True)

    if not selection:
        cmds.warning("No object selected.")
        return

    attrs = cmds.listAnimatable(selection)
    if not attrs:
        cmds.warning("No animatable attributes found.")
        return

    for attr in attrs:
        prev_key = cmds.findKeyframe(attr, which="previous")
        next_key = cmds.findKeyframe(attr, which="next")

        # Error check for missing keyframes
        if prev_key == next_key:
            continue

        prev_value = cmds.getAttr(f"{attr}", time=prev_key)
        next_value = cmds.getAttr(f"{attr}", time=next_key)

        # Calculate the tween value
        x = next_value - prev_value
        tween_value = prev_value + (x * (tween_perc / 100))

        cmds.setKeyframe(attr, time=current_frame, value=tween_value)

def tween_ui():
    # Create the window UI
    if cmds.window("TweenWindow", exists=True):
        cmds.deleteUI("TweenWindow")

    tui = cmds.window("TweenWindow", title="Tween Machine Ver 0.01", widthHeight=(200, 100))
    cmds.columnLayout(adjustableColumn=True)
    cmds.separator(height=10)
    cmds.text("Welcome to Tween Machine")
    cmds.separator(height=10)

    # Create a slider for tween percentage
    slider = cmds.intSliderGrp(label="Tween", minValue=0, maxValue=100, value=50, field=True)

   
    cmds.button(label="Tween", command=lambda *args: tweener(cmds.intSliderGrp(slider, query=True, value=True)))

    cmds.showWindow(tui)

tween_ui()
