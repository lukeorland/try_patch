import unittest
from mock import patch, Mock

import try_patch


class TestSlowClassNoPatch(unittest.TestCase):

    def test_slow(self):
        """
        Testing a slow method
        """
        self.assertEqual(
            'slow_result',
            try_patch.get_result()
        )


class TestSlowClassContextManager(unittest.TestCase):

    def test_fast(self):
        """
        Testing a slow method patched to be fast using context manager
        """
        with patch('try_patch.SlowClass') as MockSlowClass:
            instance = MockSlowClass.return_value
            instance.slow_method.return_value = 'fast_result'
            result = try_patch.get_result()

        self.assertEqual(
            'fast_result',
            result
        )


class TestSlowClassPatchObjectDecorator(unittest.TestCase):

    @patch.object(try_patch.SlowClass, 'slow_method', return_value='fast_result')
    def test_fast(self, MockSlowClass):
        """
        Testing a slow method patched to be fast using @patch.object
        """
        self.assertEqual(
            'fast_result',
            try_patch.get_result()
        )


class TestSlowClassPatchDecorator(unittest.TestCase):

    @patch('try_patch.SlowClass', spec=True)
    def test_fast(self, MockSlowClass):
        """
        Testing a slow method patched to be fast using @patch
        """
        instance = MockSlowClass.return_value
        instance.slow_method.return_value = 'fast_result'
        self.assertEqual(
            'fast_result',
            try_patch.get_result()
        )
