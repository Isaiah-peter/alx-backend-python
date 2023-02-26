#!/usr/bin/env python3
"""testing utils.access_nested_map"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, access_map, path, answer):
        """testing access_nested_map"""
        self.assertEqual(access_nested_map(access_map, path), answer)
