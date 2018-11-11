#!/usr/bin/python
#*_coding:utf-8_*

"""
    归并排序：
        1. 将序列分成左右两段，分别对2段排序然后merge
        2. 各段的排序实际上就是不断递归，直到只剩一个元素，return
        3. 左右两段都return后进行merge即可。
        4. merge就是拿第三个数组，将左右2段有序数组元素从头开始同时取出，哪边元素小就取哪边的元素，并往后移动下标继续比较。
    时间分析：
        N个元素的排序等于两个N/2个元素的排序和1次merge
        T(N) = 2*T(N/2) + 1  递归这个式子结果为T(N) = N + NlogN
    空间：
        合并两个排序的表需要线性的附加空间，所以归并排序实际上不太适用于内存里的排序。
        不过很多外部排序算法都是采用了归并这种思想。
"""    
def merge(nums1, nums2):
    # 不用交换大小
    # if len(nums1) > len(nums2):
    #     nums1, nums2 = nums2, nums1 
    if nums1 == []:
        return nums2
    if nums2 == []:
        return nums1
    # 每个merge里都有一个临时数组nums是不太好的。  
    # 由于merge在递归的尾端，因此任何时候只要有一个这样的数组就好了，可以通过传入一个数组参数进行改进。
    nums = []
    i, j = 0, 0     
    while True:
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1
            if i == len(nums1):
                nums.extend(nums2[j:])
                break
        else:
            nums.append(nums2[j])
            j += 1
            if j == len(nums2):
                nums.extend(nums1[i:])
                break
    # 打印merge过程能非常快速地调试
    print "merge: ", nums, nums1, nums2
    return nums

def merge_sort(nums, case_id=-1):
    if len(nums) <= 1:
        return nums

    mid = len(nums) / 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


# Test merge()
assert merge([3], [2]) == [2,3]
assert merge([1, 2, 4, 6], [5,7]) == [1,2,4,5,6,7]

# Test merge_sort()
TestCase = [    [1, 2, 3, 4, 5],
                [3, 2, 1, 4, 99, 22, 56, 11, 89],
                [4880, 3, 212, 10, 20413, 3110, 0, 1011, 999],
            ]           
def check_sort(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return False
    return True


for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase
    nums = merge_sort(nums, i)
    ret = nums
    if not check_sort(ret):
        print 'Test Case ', i, ' failed.',  ret

        
