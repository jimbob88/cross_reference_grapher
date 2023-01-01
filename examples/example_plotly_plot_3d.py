"""
"""
import igraph

from graph_to_3d_coordinates import to_3d_points
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio


# import chart_studio.plotly.graph_objs as go


def main():
    igraph_model = igraph.read('out.gml', format='gml')

    node_coords, edge_coords = to_3d_points(igraph_model, layout_mode='fr')

    edge_trace = go.Scatter3d(x=edge_coords[0],
                              y=edge_coords[1],
                              z=edge_coords[2],
                              mode='lines',
                              line=dict(color='rgb(125,125,125)', width=1),
                              hoverinfo='none'
                              )
    node_trace = go.Scatter3d(x=node_coords[0],
                              y=node_coords[1],
                              z=node_coords[2],
                              mode='markers',
                              name='verses',
                              marker=dict(symbol='circle',
                                          size=6,
                                          # color='blue',
                                          colorscale='Viridis',
                                          line=dict(color='rgb(50,50,50)', width=0.5)
                                          ),
                              text=igraph_model.vs["verse"],
                              hoverinfo='text'
                              )
    data = [node_trace, edge_trace]
    fig = go.Figure(data=data, layout=None)

    # py.plot(fig, filename='Bible Verse')
    pio.write_html(fig, file='hello_world.html', auto_open=True)


if __name__ == '__main__':
    main()
