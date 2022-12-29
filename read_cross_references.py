from typing import Tuple, List

from bible_objects import VersePointer, OpenBibleCrossReference


def raw_interp(cross_references: str, ignore_first_row=False) -> List[Tuple[str, str, int]]:
    """The most basic interpretation of the open_bible cross-reference database"""
    if ignore_first_row:
        cross_references = '\n'.join(cross_references.splitlines()[1:])

    interp = []

    for line in cross_references.splitlines():
        from_verse, to_verse, votes = line.split('\t')
        interp.append((from_verse, to_verse, int(votes)))

    return interp


def verse_str_to_verse_pointer(verse_str: str) -> VersePointer:
    """Takes a verse string and converts it to a named pointer to that same information.

    Intended to improve legibility of code.

    :param verse_str: For example 'Gen.1.1'
    """
    book, chapter, verse = verse_str.split('.')
    return VersePointer(
        book_name=book, chapter=int(chapter), verse=int(verse)
    )


def raw_interp_to_cross_references(cross_references: List[Tuple[str, str, int]]) -> List[OpenBibleCrossReference]:
    """Converts the raw read of cross_references to a cleaner input

    :param cross_references: The return of raw_interp()
    :return: A list of objects which describe each bible cross_reference.
    """
    return [OpenBibleCrossReference(
        from_verse=verse_str_to_verse_pointer(cross_reference[0]),
        to_verse=verse_str_to_verse_pointer(cross_reference[1]),
        votes=cross_reference[2]
    ) for cross_reference in cross_references]
