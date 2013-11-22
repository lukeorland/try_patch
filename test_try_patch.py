import unittest
from mock import patch, Mock

import try_patch


class TestClassANoPatch(unittest.TestCase):

    def test_slow(self):
        """
        Testing a slow method
        """
        self.assertEqual(
            'slow_result',
            try_patch.get_result()
        )


class TestClassAContextManager(unittest.TestCase):

    def test_fast(self):
        """
        Testing a slow method patched to be fast using context manager
        """
        with patch('try_patch.ClassA') as MockClassA:
            instance = MockClassA.return_value
            instance.slow_method.return_value = 'fast_result'
            result = try_patch.get_result()

        self.assertEqual(
            'fast_result',
            result
        )


class TestClassAPatchObjectDecorator(unittest.TestCase):

    @patch.object(try_patch.ClassA, 'slow_method', return_value='fast_result')
    def test_fast(self, mock_classA):
        """
        Testing a slow method patched to be fast using @patch.object
        """
        self.assertEqual(
            'fast_result',
            try_patch.get_result()
        )


class TestClassAPatchDecorator(unittest.TestCase):

    @patch('try_patch.ClassA', spec=True)
    def test_fast(self, MockClassA):
        """
        Testing a slow method patched to be fast using @patch
        """
        instance = MockClassA.return_value
        instance.slow_method.return_value = 'fast_result'
        self.assertEqual(
            'fast_result',
            try_patch.get_result()
        )
