from unittest2 import TestCase
from hypothesis import given, strategies as st

def get_num(num):
    return [x for x in xrange(num)]

class Test(TestCase):
    @given(st.integers(1, 10))
    def test_simple_test(self, s):
        self.assertEqual(get_num(s), [x for x in xrange(s+1)])