"""
桶的个数为最大的数字，这样只需要遍历一遍即可。 缺点是桶可能过多。 重复数字不会保留。
"""

def bucket_sort(nums, case_id):
    num_arr = [0 for i in range(max(nums)+1)]
    for a in nums:
        num_arr[a] = 1

    return [i for i in range(len(num_arr)) if num_arr[i] == 1]



TestCase = [    [1, 2, 3, 4],
                [3, 2, 1, 4],
                [4, 3, 2, 1],
            ]
            
def check_sort(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True


for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase
    ret = bucket_sort(nums, i)
    if not check_sort(ret):
        print 'Test Case ', i, ' failed.', expect, ret
