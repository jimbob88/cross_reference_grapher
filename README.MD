# Cross-Reference Grapher

The following is a project which doesn't necessarily have anything to do with visual graphs. Although, if you check out the `./examples/` directory, you
can see it used in this way! This project concerns graphs in the Computer Science sense. It connects nodes (verses) using arcs to other nodes (other
verses). For example, when Jesus says "Eli Eli Lama Sabachthani?" at Golgotha we know this occurs at Matthew 27:46 and Mark 15:34. Therefore, we would
have two nodes "Matthew 27:46" and "Mark 15:34" which are connected by an arc. We also know Jesus is quoting Psalm 22:1. So we would have another node
called "Psalm 22:1" connected to these two verses.

This would be represented by the computer like so:

![Cross-Reference Graph Example](https://i.imgur.com/rXeHa14.png)

This project intends to make it easy for python to import and analyse cross-references
from [openbible.info](https://www.openbible.info/labs/cross-references/).

## igraph

This project is massively indebted to [igraph](https://igraph.org/). Therefore, it also inherits a lot of features of igraph. In the examples folder
you will see that it is used to generate `gml` graph files. These files can be imported into other programs (like [Gephi](https://gephi.org/)). It
also means that you could make a huge database, which could take a while, and then export it to a gml. This gml will then be _extremely_ fast to open
and analyse.

Igraph also gives the ability to find the shortest paths and minimum spanning trees. One could make a game where you have to try and get from a bible
verse to another bible verse via the shortest route!

## A Vision

This project could be applied in a lot of ways, if you take a look in the examples directory you will find it being used for creating interactive
plots. One could also build a bible software with cross-reference support (for example when I click Matthew 1:23, the software could take you to
Isaiah 7:14, see [BibleHub](https://biblehub.com/crossref/matthew/1-23.htm)).

My vision for this project, the way I'd love to see it utilized, would be in an animated video. I have been researching how to program animations for
creating videos (so far I have looked at [manim](https://github.com/3b1b/manim)), I think it would be awesome for making short animations to show how
the bible is connected. For example, you could have a YouTube channel that does a deep-dive into every verse of the bible, using these
cross-references to make an animation of a tree. I imagine a tree forming from each verse as you connect the roots. Just an idea! Feel free to
plagiarise!
