#!/usr/bin/env python
import unittest
from sillymap.burrows_wheeler import burrows_wheeler
from sillymap.count_lookup import count_lookup
from sillymap.rank_lookup import Rank
from sillymap.backwards_search import backwards_search

class TestBW(unittest.TestCase):
    def test_basic_bw(self):
        self.assertEqual(burrows_wheeler("mississippi"), ("ipssm$pissii", [11,10,7,4,1,0,9,8,6,3,5,2]))

    def test_empty(self):
        self.assertEqual(burrows_wheeler(""), ("$", [0]))

class TestCountLookup(unittest.TestCase):
    def test_basic_count_lookup(self):
        c = count_lookup("mi")
        self.assertEqual(c["i"], 0)
        self.assertEqual(c["m"], 1)

    def test_second_count_lookup(self):
        c = count_lookup("mississippi")
        self.assertEqual(c['i'], 0)
        self.assertEqual(c['m'], 4)
        self.assertEqual(c['p'], 5)
        self.assertEqual(c['s'], 7)

    def test_third_count_lookup(self):
        c = count_lookup("ipssm$pissii")
        self.assertEqual(c['s'], 8)
        self.assertEqual(c['i'], 1)

class TestRankLookup(unittest.TestCase):
    def test_basic_rank_lookup(self):
        rank = Rank()
        rank.add_text("ipssm$pissii")

        self.assertEqual(rank.rank(-1,"i"), 0)
        self.assertEqual(rank.rank(0,"i"), 1)
        self.assertEqual(rank.rank(11,"s"), 4)

class TestBackwardsSearch(unittest.TestCase):
    def test_basic_backwards_search(self):
        cl = count_lookup("ipssm$pissii")
        rank = Rank()
        rank.add_text("ipssm$pissii")
        s,e = backwards_search("iss", cl, rank, 12)
        self.assertEqual(s, 3)
        self.assertEqual(e, 4)

    def test_basic_backwards_search2(self):
        cl = count_lookup("ipssm$pissii")
        rank = Rank()
        rank.add_text("ipssm$pissii")
        s, e = backwards_search("miss", cl, rank, 12)
        self.assertEqual(s, 5)
        self.assertEqual(e, 5)

    def test_basic_backwards_search3(self):
        cl = count_lookup("ipssm$pissii")
        rank = Rank()
        rank.add_text("ipssm$pissii")
        s, e = backwards_search("ppi", cl, rank, 12)
        self.assertEqual(s, 7)
        self.assertEqual(e, 7)

if __name__ == '__main__':
    unittest.main()
