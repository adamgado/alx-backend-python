#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch

from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, correct):
        result = access_nested_map(map, path)
        self.assertEqual(result, correct)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, correct):
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
        self.assertEqual(f"KeyError('{correct}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        configure = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **configure)
        mock_obj = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock_obj.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test Memoize"""
    def test_memoize(self):

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
