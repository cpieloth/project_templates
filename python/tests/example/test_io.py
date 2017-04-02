import unittest

import example.io

__author__ = 'christof.pieloth'


class IoTestCase(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(example.io.print_hello_world('bar'), 'Hello bar!')
