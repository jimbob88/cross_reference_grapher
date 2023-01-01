"""
A simple example using matplotlib.

The matplotlib plotting system is currently not worth doing if you have > 10 verses.
Use igraph plot if you want a 2d plot
"""
import igraph
from matplotlib import pyplot as plt

from matplotlib_visual import visualize


def main():
    igraph_model = igraph.read('out.gml', format='gml')
    
    fig, ax = plt.subplots(figsize=(30, 30))
    visualize(igraph_model, ax)
    plt.show()


if __name__ == '__main__':
    main()
