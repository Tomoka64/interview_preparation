from nose.tools import assert_equal

def anagram(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    return sorted(s1) == sorted(s2)

def anagram2(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    if count[letter] != 0:
        return False
    
    return True

class AnagramTest(object):
    def __init__(self):
        self.counter = 1

    def test(self, ana):
        assert_equal(ana('god','dodg'), False)
        assert_equal(ana('god', 'dog'), True)
        assert_equal(ana('god', ' dog'), True)
        print("all test has passed", self.counter)
        self.counter += 1

t = AnagramTest()
t.test(anagram)
t.test(anagram2)
