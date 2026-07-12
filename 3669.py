
import bisect


# backtracking, number theory
def factors(n):
    result = [[] for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        for j in range(i, n+1, i):
            result[j].append(i)
    return result


MAX_N = 10**5
FACTORS = factors(MAX_N)
class Solution(object):
    def minDifference(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def backtracking(remain):
            start = curr[-1] if curr else 1
            if len(curr) == k-1 and remain >= start:
                curr.append(remain)
                if not result or result[-1]-result[0] > curr[-1]-curr[0]:
                    result[:] = curr
                curr.pop()
                return
            factors = FACTORS[remain]
            for i in xrange(bisect.bisect_left(factors, start), len(factors)):
                curr.append(factors[i])
                backtracking(remain//factors[i])
                curr.pop()
                    
        result, curr = [], []
        backtracking(n)
        return result    
