# 顺序比较相邻大小
# TODO 直接跳到 d_max比较，如果小于则中间这段都不用比较了
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0        
        d_max = 1
        d = 1
        for i in range(nums_len - 1):
            if nums[i] < nums[i+1]:
                d += 1
            else:
                if d_max < d:
                    d_max = d
                d = 1

        return max(d, d_max)        
