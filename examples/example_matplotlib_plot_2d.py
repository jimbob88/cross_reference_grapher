"""
A simple example using matplotlib.

I personally much prefer the output from cairocffi (example_igraph_plot_2d.py), so I would recommend using that instead, I believe their plots are
much more impressive and easier to read. I am sure you can mess with the matplotlib setup and get similar or even better results (the key advantage
being that you can have an interactive 2d plot).
"""
import igraph
from matplotlib import pyplot as plt


def main():
    igraph_model = igraph.read('out.gml', format='gml')

    fig, ax = plt.subplots(figsize=(5, 5))
    igraph.plot(
        igraph_model,
        target=ax,
        layout="fr",
        vertex_size=0.01,
        edge_width=0.1,
        # vertex_color=["steelblue" if gender == "M" else "salmon" for gender in g.vs["gender"]],
        vertex_color="steelblue",
        vertex_frame_color="white",
        vertex_label=igraph_model.vs["all"],
        vertex_label_size=2,
    )
    plt.show()


if __name__ == '__main__':
    main()
