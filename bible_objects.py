from typing import NamedTuple


class VersePointer(NamedTuple):
    book_name: str
    chapter: int
    verse: int


class OpenBibleCrossReference(NamedTuple):
    from_verse: VersePointer
    to_verse: VersePointer
    votes: int
