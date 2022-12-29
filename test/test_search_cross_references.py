import unittest

from bible_objects import OpenBibleCrossReference, VersePointer
from search_cross_references import find_from_verse, filter_cross_references


class TestSearch(unittest.TestCase):
    def test_find_from_verse_withAllReferences_returnsAllReferences(self):
        cross_references = [
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Rom', chapter=11, verse=36),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Rom', chapter=1, verse=1),  # fake
                votes=0
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Psa', chapter=1, verse=1),  # fake
                votes=0
            ),
        ]

        cross_reference = find_from_verse(VersePointer(book_name='Gen', chapter=1, verse=1), cross_references)

        self.assertEqual(set(cross_references), cross_reference)

    def test_find_from_verse_withOneReference_returnsOneReference(self):
        cross_references = [
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Rom', chapter=11, verse=36),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=2),
                to_verse=VersePointer(book_name='Rom', chapter=1, verse=1),  # fake
                votes=0
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=2),
                to_verse=VersePointer(book_name='Psa', chapter=1, verse=1),  # fake
                votes=0
            ),
        ]

        cross_reference = find_from_verse(VersePointer(book_name='Gen', chapter=1, verse=1), cross_references)

        self.assertEqual({cross_references[0]}, cross_reference)

    def test_filter_cross_references(self):
        cross_references = [
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Rom', chapter=11, verse=36),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Rom', chapter=1, verse=1),  # fake
                votes=0
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Psa', chapter=1, verse=1),  # fake
                votes=0
            ),
        ]

        cross_reference = filter_cross_references(lambda cr: cr.votes > 5, cross_references)

        self.assertEqual({cross_references[0]}, cross_reference)


if __name__ == '__main__':
    unittest.main()
