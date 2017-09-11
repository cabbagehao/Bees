# 遍历元素，在字典里查找是否有target-nums[i]
# 如果有就finish，若没有就将自身添加进dict。
# 时间O(n)  空间O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data_dict = {}
        for i in range(len(nums)):
            if data_dict.has_key(target - nums[i]):
                return data_dict[target - nums[i]], i
            else:
                data_dict[nums[i]] = i
