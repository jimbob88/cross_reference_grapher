import igraph
import pyvis.network


def main():
    igraph_model = igraph.read('out.gml', format='gml')

    networkx_model = igraph_model.to_networkx()

    pyvis_model = pyvis.network.Network('1080px', '1920px')
    pyvis_model.from_nx(networkx_model)
    pyvis_model.show('nx.html')


if __name__ == '__main__':
    main()
