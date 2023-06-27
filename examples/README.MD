# Examples

The following examples show a simple use-case for the dataset. A gallery is available [here](https://imgur.com/a/7B2i1Tn).

All these examples are designed to be run through pycharm, although editing the imports will allow them to be used in the terminal.

The example images generated below use the following criteria:

1. All of them look at cross-references from Genesis 1:1 (in principio creavit Deus caelum et terram).
2. They take only cross-references with more than 5 votes, if you wanted fewer connections you could increase the vote limit by changing the filter
   in `create_databse.py` and `create_small_database.py`. This will make the plots less impressive but much more usable.
3. I used `create_small_database.py` to only create graphs at a depth of 2. (See the README at the root of this repository to find out what this
   means).

The images are also screenshots, so do not show the full-resolution of the image you get. (For example the IGraph plot is very zoom-able)

### example_matplotlib_plot_2d.py

This plot isn't fantastically useful, but it is certainly interesting as it gives a base 2d visualization that shows _how interlinked the verses are_.
I personally would not use it to actually read the values because of the size of the text.

![Matplotlib Genesis 1:1 Depth 2](https://i.imgur.com/kU3X4Oj.png)

### example_igraph_plot_2d.py

This is another not-so-useful graph, it has a small advantage over the matplotlib plot due to the scattering of the nodes and the obvious root node.

![Igraph Genesis 1:1 Depth 2](https://i.imgur.com/nkOeunS.png)

### example_plotly_plot_3d.py

This is my personal favourite graph as it is fully interactive in 3D. It is far easier to navigate then any of the 2D options and it allows you to
properly read all the verse numbers. With some pruning this could actually be useful!

![Plotly Genesis 1:1 Depth 2](https://i.imgur.com/3EjDMU7.png)

## Do It Yourself

This guide assumes you are techy and know how to use python!

1. In order to do it yourself, you need to obtain the cross-reference database
   from [openbible.info](https://www.openbible.info/labs/cross-references/).
   If you scroll to the bottom of this page, you can download the cross-reference data zip (alternatively
   click [here](https://a.openbible.info/data/cross-references.zip)).
2. Extract the cross_references.txt and move it to the `./examples/` folder.
3. Execute the `create_small_database.py` (it will go much faster). You should get an `out_small.gml`, rename this to `out.gml`.
4. Execute the `example_*.py` files and generate the different plots!