import unittest
from mock import patch, Mock

import try_patch

class TestClassA(unittest.TestCase):

    @patch('try_patch.ClassA')
    def test_fast(self, patched_classA):
        """
        Testing a slow method patched to be fast
        """
        patched_classA.method = Mock(return_value='classA')
        self.assertEqual(
            'classA',
            patched_classA.method()
        )

    def test_slow(self):
        """
        Testing a slow method
        """
        self.assertEqual(
            'classA',
            try_patch.ClassA().method()
        )
