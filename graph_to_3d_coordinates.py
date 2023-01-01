from typing import List, Tuple

import igraph


def to_3d_points(
        graph: igraph.Graph,
        layout_mode: str = 'kk'
) -> Tuple[
    Tuple[List[float], List[float], List[float]],
    Tuple[List[float], List[float], List[float]],
]:
    layout = graph.layout(layout_mode, dim=3)

    x_nodes = [coord[0] for coord in layout]
    y_nodes = [coord[1] for coord in layout]
    z_nodes = [coord[2] for coord in layout]

    x_edges = []
    y_edges = []
    z_edges = []
    for edge in graph.get_edgelist():
        x_edges.extend((layout[edge[0]][0], layout[edge[1]][0], None))
        y_edges.extend((layout[edge[0]][1], layout[edge[1]][1], None))
        z_edges.extend((layout[edge[0]][2], layout[edge[1]][2], None))

    return (x_nodes, y_nodes, z_nodes), (x_edges, y_edges, z_edges)
