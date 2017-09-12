class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                #nums.pop(i)  # beat 34%
                del(nums[i])  # beat 50% 
                #nums.remove(nums[i-1]) # Time Limit Exceeded.

        if len(nums) >= 2 and nums[0] == nums[1]:
            nums.pop(0)

        return len(nums)
        
