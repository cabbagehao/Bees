# 直接循环remove，效率比交换元素提高一倍,非常简洁，2行搞定。

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
            
        return len(nums)
