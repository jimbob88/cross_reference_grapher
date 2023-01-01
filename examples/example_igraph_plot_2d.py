"""
Using cairocffi for plotting
"""
import igraph


def main():
    igraph_model = igraph.read('out.gml', format='gml')

    igraph.plot(igraph_model, 'out.png',
                bbox=(0, 0, 10000, 10000),
                vertex_label=igraph_model.vs["verse"],
                vertex_color=["blue" if verse == "Gen.1.1" else "red" for verse in igraph_model.vs["verse"]],
                vertex_size=[60 if verse == "Gen.1.1" else 4 for verse in igraph_model.vs["verse"]],
                )


if __name__ == '__main__':
    main()
