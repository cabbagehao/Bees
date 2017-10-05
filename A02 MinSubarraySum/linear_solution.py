"""
    求最小和，无非就是尽量加负数。
    如果this_num加上num[i]后还是正数，则置零重新计算。
        
"""
def minimum_subarray_sum(nums, case_id):
    min_sum = 100000
    this_sum = 0
    for i in range(len(nums)):
        this_sum += nums[i]
 
        if this_sum < min_sum:
            min_sum = this_sum   
        elif this_sum > 0:
            this_sum = 0
    return min_sum


# [[nums, target, expect]]
TestCase = [    [[1], 1],
                [[1, 2, 3], 1],
                [[1,2,-1,-2], -3],                
            ]           




for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase[0]
    expect = testcase[1]
    ret = minimum_subarray_sum(nums, i)
    if abs(expect - ret) > 0.0001:
        print 'Test Case ', i, ' failed.', expect, ret
