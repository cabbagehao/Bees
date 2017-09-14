# 此种方式能够提高少量性能，对本题数据集来说 interval=16 32 64的效果一样。
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        d_max = 1
        d = 1
        interval = 64
        while (len(nums) - 1) % interval != 0:
            nums.append(nums[-1])
        for i in range(0, len(nums)-interval, interval):
            # TODO 可以尝试j倒序，如果d已经比interval大，则直接退出。
            for j in range(interval):
                if nums[i+j] < nums[i+j+1]:
                    d += 1
                else:
                    if d_max < d:
                        d_max = d
                    d = 1

        return max(d, d_max)      
