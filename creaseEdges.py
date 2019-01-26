import maya.cmds as cmds


def selectCrease(creaseValue):
    """ Select edges matching a specific crease value """
    sel = cmds.ls(sl=True, l=True)
    edgeCollection = cmds.polyListComponentConversion(sel, te=True)
    edges = cmds.filterExpand(edgeCollection, sm=32, expand=True)

    creasedEdges = []

    for edge in edges:
        edgeValue = cmds.polyCrease(edge, query=True, value=True)
        if edgeValue[0] == creaseValue:
            creasedEdges.append(edge)
    cmds.select(creasedEdges)


def setCrease(creaseValue):
    """ Set edges to a specific crease value """
    selection = cmds.ls(sl=True, fl=True)
    for edge in selection:
        cmds.polyCrease(edge, ch=True, value=creaseValue, vertexValue=0)
