# 原题链接： https://leetcode.com/problems/two-sum/description
# 将nums里所有元素都放在 y=x 这条直线上
# 设y = -x + target直线 与 y=x直线的交点为(a, a)
# 可以得到所求的2个元素与交点距离相同，由于nums所有元素都在y=x上，即是 |x1 - a| == |x2 - a|
# 无需排序，时间O(n),空间O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d_dict = {}
        intersection_x = 1.0 * target / 2

        for i in range(len(nums)):
            d = abs(nums[i] - intersection_x)
            if d_dict.has_key(d):
                # 有不满足条件的2个相同元素时需要排除
                if nums[d_dict[d]] + nums[i] != target:
                    continue
                else:
                    return [d_dict[d], i]
            else:
                d_dict[d] = i
