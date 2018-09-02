def compress(s):
    count = {}
    ret = ""
    for string in s:
        if not string in count:
            count[string] = 1
        else:
            count[string] += 1
    for i in count:
        ret += i + str(count[i])
    return ret

from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)
