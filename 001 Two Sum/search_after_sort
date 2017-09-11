# 先排序，在从首尾同时查找
# 效率较几何方法慢。 时间O(n), 空间O(n)
# 改进： 可以自己实现log(n)的排序。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_pos_list = list(enumerate(nums))
        sorted_num =  sorted(num_pos_list, cmp=lambda x,y:cmp(x[1],y[1]))

        len_num = len(nums)
        i = 0
        j = len_num - 1
        while i < j:
            if sorted_num[i][1] + sorted_num[j][1] == target:
                return sorted_num[i][0], sorted_num[j][0]

            if sorted_num[i][1] + sorted_num[j][1] < target:
                i += 1
            else:
                j -= 1

        return None
