from typing import List, Tuple

from bible_objects import VersePointer
import igraph as ig

from read_cross_references import verse_pointer_to_str


def to_igraph(id_map: List[VersePointer], edges: List[Tuple[int, int]]) -> ig.Graph:
    """Converts the network_model into an igraph model"""
    graph = ig.Graph(len(id_map), edges)
    graph.vs["all"] = [verse_pointer_to_str(v_ptr) for v_ptr in id_map]
    graph.vs["bookname"] = [v_ptr.book_name for v_ptr in id_map]
    graph.vs["chapter"] = [v_ptr.chapter for v_ptr in id_map]
    graph.vs["verse"] = [v_ptr.verse for v_ptr in id_map]

    return graph
