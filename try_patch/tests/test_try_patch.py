import unittest
from mock import patch, Mock

import try_patch

class TestClassA(unittest.TestCase):

    @patch('try_patch.ClassA')
    def test_fast(self, patched_classA, spec=True):
        """
        Testing a slow method patched to be fast
        """
        patched_classA.slow_method = Mock(return_value='fast_method')
        self.assertEqual(
            'fast_method',
            try_patch.get_result()
        )

    def test_slow(self):
        """
        Testing a slow method
        """
        self.assertEqual(
            'slow_method',
            try_patch.get_result()
        )
