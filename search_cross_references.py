from typing import Set, Iterable, Callable

from bible_objects import VersePointer, OpenBibleCrossReference


def find_from_verse(from_verse: VersePointer, cross_references: Iterable[OpenBibleCrossReference]) -> Set[OpenBibleCrossReference]:
    """Given a from_verse, find all cross-references that are directly from"""
    return {
        cross_reference for cross_reference in cross_references if cross_reference.from_verse == from_verse
    }


def find_to_verse(to_verse: VersePointer, cross_references: Iterable[OpenBibleCrossReference]) -> Set[OpenBibleCrossReference]:
    """Given a to_verse, find all cross-references that are directly to"""
    return {
        cross_reference for cross_reference in cross_references if cross_reference.to_verse == to_verse
    }


def filter_cross_references(filter_function: Callable[[OpenBibleCrossReference], bool],
                            cross_references: Iterable[OpenBibleCrossReference]) -> Set[OpenBibleCrossReference]:
    """Useful alias function (i.e. only getting cross-references with votes > 5"""
    return set(
        filter(filter_function, cross_references)
    )
