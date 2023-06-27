"""
Plotly 3d Plot with a unique colour for each book of the bible
"""
from pathlib import Path
from typing import Sequence, Dict

import igraph

from graph_to_3d_coordinates import to_3d_points
import plotly.graph_objects as go
import seaborn as sns


def assign_colours(books: Sequence[str]) -> Dict[str, str]:
    books = list(set(books))
    book_to_colour = {}
    for idx, colour in enumerate(sns.color_palette(None, len(books))):
        rgb = (colour[0] * 255, colour[1] * 255, colour[2] * 255)
        book_to_colour[books[idx]] = f'rgb{rgb[0], rgb[1], rgb[2]}'

    return book_to_colour


def main():
    igraph_model = igraph.read('out.gml', format='gml')

    book_to_colour = assign_colours(igraph_model.vs["bookname"])
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
                                          color=[book_to_colour[book] for book in igraph_model.vs["bookname"]],
                                          colorscale='Viridis',
                                          line=dict(color='rgb(50,50,50)', width=0.5)
                                          ),
                              text=igraph_model.vs["all"],
                              hoverinfo='text'
                              )
    data = [node_trace, edge_trace]
    fig = go.Figure(data=data, layout=None)

    html = fig.to_html()
    Path('out.html').write_text(html, encoding='utf-8')


if __name__ == '__main__':
    main()
