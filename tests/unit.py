#!/usr/bin/env python
import unittest
from sillymap.burrows_wheeler import burrows_wheeler
from sillymap.count_lookup import count_lookup
from sillymap.rank_lookup import Rank

class TestBW(unittest.TestCase):
    def test_basic_bw(self):
        self.assertEqual(burrows_wheeler("mississippi"), "ipssm$pissii")

    def test_empty(self):
        self.assertEqual(burrows_wheeler(""), "$")

class TestCountLookup(unittest.TestCase):
    def test_basic_count_lookup(self):
        c = count_lookup("mi")
        self.assertEqual(c["i"], 0)
        self.assertEqual(c["m"], 1)

    def test_basic_count_lookup(self):
        c = count_lookup("mississippi")
        self.assertEqual(c['i'], 0)
        self.assertEqual(c['m'], 4)
        self.assertEqual(c['p'], 5)
        self.assertEqual(c['s'], 7)

class TestRankLookup(unittest.TestCase):
    def test_basic_rank_lookup(self):
        rank = Rank()
        rank.add_text("ipssm$pissii")

        self.assertEqual(rank.rank(-1,"i"), 0)
        self.assertEqual(rank.rank(0,"i"), 1)
        self.assertEqual(rank.rank(11,"s"), 4)

if __name__ == '__main__':
    unittest.main()
