# Recursively
# Dynamically (Using Memoization to store results)
# Iteratively


def fib_rec(n):
    if n <=2:
        return int((n+1)/2)
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b , a + b
    return a


def fib_dyn(n):
    cache = [None] * (n + 1)
  
    if n == 0 or n == 1:
        return n
 
    if cache[n] != None:
        return cache[n]
    
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]

print(fib_dyn(10))

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print('Passed all tests.')

t = TestFib()

t.test(fib_rec)
t.test(fib_dyn) 
t.test(fib_iter)