import unittest

from bible_objects import OpenBibleCrossReference, VersePointer
from read_cross_references import raw_interp, raw_interp_to_objects, verse_str_to_verse_pointer


class RawInterp(unittest.TestCase):
    def test_raw_interp_withNoHeader(self):
        example = ("Gen.1.1\tRom.11.36\t36\n"
                   "Gen.1.1\tEph.3.9\t32\n"
                   "Gen.1.1\tPs.136.5\t44\n")
        interp = raw_interp(example, ignore_first_row=False)

        self.assertEqual(len(interp), 3)
        self.assertEqual(interp[0], ("Gen.1.1", "Rom.11.36", 36))
        self.assertEqual(interp[1], ("Gen.1.1", "Eph.3.9", 32))
        self.assertEqual(interp[2], ("Gen.1.1", "Ps.136.5", 44))

    def test_raw_interp_withHeader_ignoresHeader(self):
        example = ("From Verse\tTo Verse\tVotes	#www.openbible.info CC-BY 2022-12-26\n"
                   "Gen.1.1\tRom.11.36\t36\n"
                   "Gen.1.1\tEph.3.9\t32\n"
                   "Gen.1.1\tPs.136.5\t44\n")
        interp = raw_interp(example, ignore_first_row=True)

        self.assertEqual(len(interp), 3)
        self.assertEqual(interp[0], ("Gen.1.1", "Rom.11.36", 36))
        self.assertEqual(interp[1], ("Gen.1.1", "Eph.3.9", 32))
        self.assertEqual(interp[2], ("Gen.1.1", "Ps.136.5", 44))

    def test_verse_str_to_verse_pointer(self):
        example = "Gen.1.1"
        self.assertEqual(verse_str_to_verse_pointer(example), VersePointer(book_name='Gen', chapter=1, verse=1))

    def test_raw_interp_to_objects(self):
        interp = [
            ("Gen.1.1", "Rom.11.36", 36),
        ]

        objs = raw_interp_to_objects(interp)

        self.assertEqual(len(interp), len(objs))
        self.assertEqual(objs[0], OpenBibleCrossReference(
            from_verse=VersePointer(book_name='Gen', chapter=1, verse=1),
            to_verse=VersePointer(book_name='Rom', chapter=11, verse=36),
            votes=36
        ))


if __name__ == '__main__':
    unittest.main()
