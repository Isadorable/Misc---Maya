import maya.cmds as cmds

cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
cmds.delete(ch=True)