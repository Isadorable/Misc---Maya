import maya.cmds as cmds
selected_joints = cmds.ls(sl=True, l=True)

for selected_joint in selected_joints:
    if cmds.objectType(selected_joint) != 'joint':
        cmds.select(selected_joint, d=True)
        selected_joints.remove(selected_joint)

cmds.select(selected_joints, hi=True)
joints_hierarchy = cmds.ls(sl=True, l=True)

for true_joint in joints_hierarchy:
    displayed = cmds.getAttr(true_joint + ".displayLocalAxis")
    cmds.setAttr(true_joint + ".displayLocalAxis", not displayed)