#!/usr/bin/env python
import unittest
import subprocess

class TestSimpleMapping(unittest.TestCase):
    def test_map_1_read(self):
        subprocess.run(['python', 'bin/sillymap', 'index', 'tests/test_data/reference.fa'])
        result = subprocess.run(['python', 'bin/sillymap', 'map', 'tests/test_data/reference.fa', 'tests/test_data/reads_1.fq'], stdout=subprocess.PIPE)
        subprocess.run(['rm', 'tests/test_data/reference.fa.silly'])
        self.assertEqual(result.stdout, b'read1,5\n')

    def test_map_5_reads(self):
        subprocess.run(['python', 'bin/sillymap', 'index', 'tests/test_data/reference.fa'])
        result = subprocess.run(['python', 'bin/sillymap', 'map', 'tests/test_data/reference.fa', 'tests/test_data/reads_2.fq'], stdout=subprocess.PIPE)
        subprocess.run(['rm', 'tests/test_data/reference.fa.silly'])
        self.assertEqual(result.stdout, b'read1,5\nread2,0\nread3,10\nread4,15\nread5,5\n')

if __name__ == '__main__':
    unittest.main()
