“”“
  可以通过分治法递归实现。 只是稍微复杂些，作为参考。
  1. 将数列分为2部分，则最终结果有3种情况：
        1. 在左边部分
        2. 在右边部分
        3. 在两部分都有
  2. 前2种情况直接递归，第3种情况的最小和为： 前半部分包含最后一个的最小和序列 + 后半部分包含第一个的最小和序列
  3. 因此，函数里计算3个sum，比较这3个sum的大小即可。
        1. 左右2个sum通过递归计算。 每次递归都进行这样的过程，直到分解为单个元素的数组时返回。
        2. 另一个sum通过单独的函数计算
”“”


def find_min_sum_cross_subarray(left, right):
    
    left_sum = 100000
    this_sum = 0
    for i in range(len(left) - 1, -1, -1):
        this_sum += left[i]
        if this_sum < left_sum:
            left_sum = this_sum


    right_sum = 100000
    this_sum = 0
    for i in range(len(right) - 1, -1, -1):
        this_sum += right[i]
        if this_sum < right_sum:
            right_sum = this_sum

    return left_sum + right_sum

def find_min_sum_subarray(nums, case_id):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) / 2
    left = nums[:mid]
    right = nums[mid:]
    left_sum = find_min_sum_subarray(left, case_id)
    right_sum = find_min_sum_subarray(right, case_id)
    cross_sum = find_min_sum_cross_subarray(left, right)

    if left_sum <= right_sum and left_sum <= cross_sum:
        return left_sum
    elif right_sum <= left_sum and right_sum <= cross_sum:
        return right_sum
    else:
        return cross_sum


# [[nums, target, expect]]
TestCase = [    [[1], 1],
                [[1, 2, 3], 1],
                [[1,2,-1,-2], -3],                
            ]           




for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase[0]
    expect = testcase[1]
    ret = find_min_sum_subarray(nums, i)
    if abs(expect - ret) > 0.0001:
        print 'Test Case ', i, ' failed.', expect, ret
