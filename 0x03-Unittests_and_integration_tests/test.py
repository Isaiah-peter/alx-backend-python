#!/usr/bin/env python3

from test_utils import TestAccessNestedMap

maps = TestAccessNestedMap()

one = maps.test_access_nested_map({"a": 1}, ("a"), 1)
two = maps.test_access_nested_map({"a": {"b": 2}}, ("a"), {"b": 2})
three = maps.test_access_nested_map({"a": {"b": 2}}, ("a", "b"), 2)

print(one)
print(two)
print(three)