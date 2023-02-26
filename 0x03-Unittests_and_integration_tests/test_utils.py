#!/usr/bin/env python3
"""testing utils.access_nested_map"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """method to test that the method returns error"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """test if a function return json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("test_utils.get_json")
    def test_get_json(self, url, payload, mock_get):
        """get json"""
        mock_get.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """test memoize"""

    def test_memoize(self):
        """test momorise"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            testClass = TestClass()
            testClass.a_method
            testClass.a_method
            mockMethod.assert_called_once
