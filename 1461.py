class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return 2**k <= len(s) and len({s[i:i+k] for i in xrange(len(s)-k+1)}) == 2**k
