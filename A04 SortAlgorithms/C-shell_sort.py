#!/usr/bin/python
#*_coding:utf-8_*
"""
    插入排序：
    def insert_sort(nums, case_id):
        for i in range(1, len(nums), 1):
            j = i;
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
    可以看到希尔排序的for部分和插入排序是一样的，只是把插入排序的1变为d    
    因为插入排序在当前序列已经部分有序时效率是很高的，希尔排序利用了这一点让序列逐渐有序。
    先将间隔大的子序列都排好，然后逐渐缩小间隔至1，这时相当于执行了1个正常的插入排序。
"""

        
def shell_sort(nums, case_id):
    d = min(20, max(2, len(nums) / 50))
    while d > 0:
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j-d]:
                nums[j], nums[j-d] = nums[j-d], nums[j]
                j -= d
        d /= 2

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
    shell_sort(nums, i)
    ret = nums
    if not check_sort(ret):
        print 'Test Case ', i, ' failed.',  ret
