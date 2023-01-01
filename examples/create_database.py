from pathlib import Path

from bible_objects import VersePointer
from igraph_model import to_igraph
from network_model import recursive_search
from read_cross_references import raw_interp, raw_interp_to_cross_references
from search_cross_references import filter_cross_references


def main():
    source = Path('cross_references.txt').read_text(encoding='utf-8')
    raw = raw_interp(source, ignore_first_row=True)
    cross_references = raw_interp_to_cross_references(raw)

    filtered_set = filter_cross_references(lambda cr: cr.votes > 5, cross_references)

    id_map, edges = recursive_search(
        VersePointer(book_name='Gen', chapter=1, verse=1),
        filtered_set
    )

    igraph_model = to_igraph(id_map, edges)

    igraph_model.write("out.gml", format='gml')
    print("Wrote model to out.gml")


if __name__ == '__main__':
    main()
