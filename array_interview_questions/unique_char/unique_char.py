def uni_char(s):
    count = {}
    for char in s:
        if not char in count:
            count[char] = 1
        else: 
             count[char] += 1
    for char in count:
        if count[char] > 1:
            return False
    return True

def uni_char2(s):
    return len(set(s)) == len(s)

def uni_char3(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True

from nose.tools import assert_equal

class TestUnique(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)
t.test(uni_char2)
t.test(uni_char3)