import igraph as ig
import matplotlib


def visualize(graph: ig.Graph, axes: matplotlib.axes.Axes):
    """Applies a plot to the given matplotlib axes"""
    ig.plot(
        graph,
        target=axes,
        layout="circle",  # print nodes in a circular layout
        vertex_size=0.1,
        # vertex_color=["steelblue" if gender == "M" else "salmon" for gender in g.vs["gender"]],
        vertex_color="steelblue",
        vertex_frame_width=4.0,
        vertex_frame_color="white",
        vertex_label=graph.vs["verse"],
        vertex_label_size=7.0,
        # edge_width=[2 if married else 1 for married in g.es["married"]],
        # edge_color=["#7142cf" if married else "#AAA" for married in g.es["married"]]
    )
