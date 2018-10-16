def rec_coin(target,coins):
    min_coins = target
    
    if target in coins:
        return 1
    else:
        for value in [ c for c in coins if c<= target]:
            num_coins = rec_coin(target-value, coins) + 1
            min_coins = min(num_coins, min_coins)
    return min_coins
    
from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)
        print('Passed all tests.')
# Run Test

test = TestCoins()
test.check(rec_coin)