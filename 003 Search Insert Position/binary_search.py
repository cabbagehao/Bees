# 采用2分法去查找位置，但是结果来看没有顺序查找快（因为有除法？）
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        try:
            index = nums.index(target)
            return index
        except ValueError:
            # binary search
            i = 0
            j = len(nums) -1

            med = -1
            while i <= j :
                med = (i + j) / 2
                if nums[med] < target:
                    i = med + 1
                else:
                    j = med - 1

        return max(med, i)
