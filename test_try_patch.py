import unittest
from mock import patch, Mock

import try_patch

class TestClassA(unittest.TestCase):

    #@patch('try_patch.ClassA')
    #def test_fast(self, patched_classA, spec=True):
    def test_fast(self):
        """
        Testing a slow method patched to be fast
        """
        with patch('try_patch.ClassA') as MockClassA:
            instance = MockClassA.return_value
            instance.slow_method.return_value = 'fast_result'
            result = try_patch.get_result()

        self.assertEqual(
            'fast_result',
            result
        )

    def test_slow(self):
        """
        Testing a slow method
        """
        self.assertEqual(
            'slow_result',
            try_patch.get_result()
        )
