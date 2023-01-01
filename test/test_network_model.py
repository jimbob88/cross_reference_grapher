import unittest

from bible_objects import OpenBibleCrossReference, VersePointer
from network_model import recursive_search


class TestRecursiveSearch(unittest.TestCase):
    def test_recursive_search_withCyclicReferences(self):
        cross_references = [
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Gen', chapter=1, verse=2),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=2),
                to_verse=VersePointer(book_name='Gen', chapter=1, verse=3),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=3),
                to_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                votes=36
            ),
        ]
        id_map, node_pairs = recursive_search(VersePointer(book_name='Gen', chapter=1, verse=1), cross_references)
        # self.assertEqual(id_map, {0: cross_references[0], 1: cross_references[1], 2: cross_references[2]})
        self.assertEqual([VersePointer(book_name='Gen', chapter=1, verse=1),
                          VersePointer(book_name='Gen', chapter=1, verse=2),
                          VersePointer(book_name='Gen', chapter=1, verse=3)], id_map)
        self.assertEqual({(0, 1), (1, 2), (2, 0)}, set(node_pairs))

    def test_recursive_search_withMultipleStartPoints(self):
        cross_references = [
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Gen', chapter=1, verse=2),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=2),
                to_verse=VersePointer(book_name='Gen', chapter=1, verse=3),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=3),
                to_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
                to_verse=VersePointer(book_name='Rom', chapter=1, verse=2),
                votes=36
            ),
            OpenBibleCrossReference(
                from_verse=VersePointer(book_name='Rom', chapter=1, verse=2),
                to_verse=VersePointer(book_name='Rom', chapter=1, verse=3),
                votes=36
            ),
        ]
        id_map, node_pairs = recursive_search(VersePointer(book_name='Gen', chapter=1, verse=1), cross_references)
        print(node_pairs)
        self.assertEqual(len(id_map), 5)
        self.assertEqual(id_map[0], VersePointer(book_name='Gen', chapter=1, verse=1))


if __name__ == '__main__':
    unittest.main()
