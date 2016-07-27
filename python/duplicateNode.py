import nuke


def duplicateNode(node):
    # Store selection
    orig_selection = nuke.selectedNodes()

    # Select only the target node
    [n.setSelected(False) for n in nuke.selectedNodes()]
    node.setSelected(True)

    # Copy the selected node and clear selection again
    nuke.nodeCopy("%clipboard%")
    node.setSelected(False)

    nuke.nodePaste("%clipboard%")
    duplicated_node = nuke.selectedNode()

    # Restore original selection
    [n.setSelected(False) for n in nuke.selectedNodes()] # Deselect all
    [n.setSelected(True) for n in orig_selection] # Select originally selected

    return duplicated_node