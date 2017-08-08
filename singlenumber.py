class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c=Counter(nums)
        for i in c:
            if c[i]==1:
                return i