def permute(s):
    output = []
    
    if len(s) <= 1:
        output=[s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                output+=[let+perm]
                # print(let, perm)
    return output

from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self,solution):
        
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        # assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
        print ('All test cases passed.')
        


# Run Tests
t = TestPerm()
t.test(permute)