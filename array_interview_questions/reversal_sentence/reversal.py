def rev_word(s):
    return " ".join(reversed(s.split()))

def rev_word_proper(s):
    words = []
    length = len(s)
    i = 0
    while i < length: 
        if s[i] != " ":
            word_start = i
            while i < length and s[i] != " ":
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reverse(words))

def reverse(list):
    ret = []
    i = len(list) -1
    while i >= 0:
        ret.append(list[i])
        i -= 1
    return ret

from nose.tools import assert_equal

class ReversalTest(object):
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run test
t = ReversalTest()
t.test(rev_word)
t.test(rev_word_proper)
