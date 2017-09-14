# This method do not efficient.   
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 
        k %= nums_len


        for i in range(k):
            nums.insert(0, nums.pop())
        
        
