from nose.tools import assert_equal

# my answer 
def my_pair_sum(list, target):
    if len(list) < 2:
        return 
    ret = set()
    for i in range(len(list)):
        j = i + 1
        while j < len(list):
            if (list[i]+ list[j] == target):
                if not (list[i], list[j]) in ret:
                    ret.add( ( min(list[i], list[j]), max(list[i], list[j]) ) )
            j += 1
    return len(ret)

# @Code-Hex これレベル高くね？↓
def pair_sum(arr,k):
    counter = 0
    lookup = set()
    for num in arr:
        if k-num in lookup:
            counter+=1
        else:
            lookup.add(num)
    return counter

class TestPair(object):
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')

t = TestPair()
t.test(pair_sum)
t.test(my_pair_sum)
