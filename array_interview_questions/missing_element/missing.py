from nose.tools import assert_equal
import collections

def my_finder(arr1, arr2):
    for i in range(len(arr1)):
        if sorted(arr1)[i] != sorted(arr2)[i]:
            return sorted(arr1)[i]

def finder(arr1, arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0: 
            return num
        else: 
            d[num] -= 1

def finder_clever(arr1, arr2): 
    result=0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        
    return result 

class TestFinder(object):
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

t = TestFinder()
t.test(my_finder)
t.test(finder)
t.test(finder_clever)