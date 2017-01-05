#!/usr/bin/env python
import unittest
from sillymap.burrows_wheeler import burrows_wheeler

class TestBW(unittest.TestCase):
    def test_basic_bw(self):
        self.assertEqual(burrows_wheeler("mississippi"), "ipssm$pissii")

    def test_empty(self):
        self.assertEqual(burrows_wheeler(""), "$")

if __name__ == '__main__':
    unittest.main()
