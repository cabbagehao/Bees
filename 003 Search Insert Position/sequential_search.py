class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 如果存在时直接.index会更快。
        try:
            index = nums.index(target)
            return index
        except ValueError:
            index = 0
            for i in range(len(nums)):
                index = i
                if nums[i] >= target:
                    break
            # nums所有值都比target小时特殊处理
            if len(nums) > 0 and nums[-1] < target:
                index += 1

            return index
