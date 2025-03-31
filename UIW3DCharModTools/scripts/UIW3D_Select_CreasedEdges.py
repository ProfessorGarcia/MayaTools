import maya.cmds as cmds

def select_creased_edges():
    selection = cmds.ls(selection=True, long=True)
    if not selection:
        cmds.warning("Please select a polygon object.")
        return

    obj = selection[0]

    # Get total number of edges
    edge_count = cmds.polyEvaluate(obj, edge=True)

    creased_edges = []

    for i in range(edge_count):
        edge = f"{obj}.e[{i}]"
        crease = cmds.polyCrease(edge, query=True, value=True)
        if crease and crease[0] > 0.0:
            creased_edges.append(edge)

    if creased_edges:
        # Switch to edge selection mode
        cmds.selectType(edge=True)
        # Select the creased edges
        cmds.select(creased_edges, replace=True)
        print(f"Selected {len(creased_edges)} creased edge(s).")
    else:
        cmds.warning("No creased edges found on the selected object.")

# Run it
select_creased_edges()
