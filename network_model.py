from typing import Iterable, Tuple, Dict, List

from bible_objects import VersePointer, OpenBibleCrossReference
from search_cross_references import find_from_verse


def recursive_search(from_verse: VersePointer,
                     cross_references: Iterable[OpenBibleCrossReference]
                     ) -> Tuple[List[VersePointer], List[Tuple[int, int]]]:
    """

    :param from_verse: The verse to start the search from
    :param cross_references: The Open Bible Database of Cross-References
    :return: Tuple (id_map: the id of each VersePointer is its index,
            the route i.e. (1, 2) means verse idx 1 goes to verse idx 2.
    """
    stack = [from_verse]
    visited: List[VersePointer] = []
    nodes = []

    while stack:
        from_verse = stack.pop()
        if from_verse not in visited:
            visited.append(from_verse)
        refs = [ref.to_verse for ref in find_from_verse(from_verse, cross_references)]

        stack.extend([ref for ref in refs if ref not in visited])

        for to_verse in refs:
            if to_verse not in visited:
                visited.append(to_verse)
            nodes.append((visited.index(from_verse), visited.index(to_verse)))

    return visited, nodes
