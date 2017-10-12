#!/usr/bin/python
#*_coding:utf-8_*
"""
    可以看到插入排序是最简单易写的，几行代码搞定。 
    只是它交换的次数有点多。
"""
def insert_sort(nums, case_id):
    for i in range(1, len(nums), 1):
        j = i;
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        

# [[nums, target, expect]]
TestCase = [    [1, 2, 3, 4, 5],
                [3, 2, 1, 4, 99, 22, 56, 11, 89],
                [4880, 3, 212, 10, 20413, 3110, 0, 1011, 999],
            ]           
def check_sort(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True



for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase
    insert_sort(nums, i)
    ret = nums
    if not check_sort(ret):
        print 'Test Case ', i, ' failed.',  ret
