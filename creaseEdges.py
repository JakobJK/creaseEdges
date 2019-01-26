import maya.cmds as cmds


def selectCrease(creaseValue=0):
    """ Select edges matching a specific crease value """
    sel = cmds.ls(sl=True, l=True)
    edgeCollection = cmds.polyListComponentConversion(sel, te=True)
    edges = cmds.filterExpand(edgeCollection, sm=32, expand=True)

    creasedEdges = []

    for edge in edges:
        edgeValue = cmds.polyCrease(edge, query=True, value=True)
        if creaseValue == 0:
            if edgeValue[0] > 0:
                creasedEdges.append(edge)
        else:
            if edgeValue[0] == creaseValue:
                creasedEdges.append(edge)
    cmds.select(creasedEdges)


def setCrease(creaseValue):
    """ Set edges to a specific crease value """
    selection = cmds.ls(sl=True, fl=True)
    for edge in selection:
        cmds.polyCrease(edge, ch=True, value=creaseValue, vertexValue=0)


def clearCrease():
    """ Select edges matching a specific crease value """
    sel = cmds.ls(sl=True, l=True)
    edgeCollection = cmds.polyListComponentConversion(sel, te=True)
    edges = cmds.filterExpand(edgeCollection, sm=32, expand=True)

    for edge in edges:
        cmds.polyCrease(edge, ch=True, value=0, vertexValue=0)
    cmds.select(sel)
