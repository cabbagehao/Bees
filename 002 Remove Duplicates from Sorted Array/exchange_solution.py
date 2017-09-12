# 题目需要不重复的N项都在数组前面。 因此只有删除多余元素/交换不重复元素2种办法
# 设置1个pos变量储存当前不重复的位置。  若有新的不重复项，则更新pos并储存。

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 
            
        pos = 0
        for i in range(length - 1):
            if nums[i] != nums[i+1]:
                pos += 1
                nums[pos] = nums[i+1]
        return pos + 1
        
