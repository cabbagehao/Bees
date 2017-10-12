#!/usr/bin/python
#*_coding:utf-8_*
def partion(nums, left, right, pos):
    """
        由于将pivot储存在了头部，所以最终交换pivot时会用一个小于pivot的交换。
        所以这里让j从右往左查找。（也可以让i从左往右，也可以将pivot存在尾部）
        直到j指向一个小于pivot的值或者i==j
        i < j 表示 nums[j] < pivot  
        i == j表示 j左边已经没有比pivot大的了。 
        下面这种写法也许更直白些。
        while (true) {
            while (arr[i] < temp && i < right) {
                i++;
            }
            while (arr[j] > temp && j < left) {
                j++
            }
            if (i >= j)
                break;
            swap(arr[i], arr[j]);
        }     

    """
    # pos目前为最左边元素。 可以通过优化pos提高快速排序的效率。
    pivot = nums[pos]
    nums[left], nums[pos] = nums[pos], nums[left]
    i, j = left+1, right
    while i <= j:
        if nums[j] < pivot:
            while nums[i] < pivot and i < j:
                i += 1

            if i == j:
                break 
            else:      
                nums[i], nums[j] = nums[j], nums[i]
        j -= 1
    
    nums[left], nums[j] = nums[j], nums[left]
    return j

assert partion([1,2,3,4,5], 0, 4, 3) == 3


def quick_sort(nums, left, right, case_id):
    if left >= right: return
        
    pos = left # choose a good pos can get better result.
    pivot_pos = partion(nums, left, right, pos)
    quick_sort(nums, left, pivot_pos-1, case_id)
    quick_sort(nums, pivot_pos+1, right, case_id)
    


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
    #expect = testcase[1]
    quick_sort(nums, 0, len(nums)-1, i)
    ret = nums
    #if abs(expect - ret) > 0.0001:
     #   print 'Test Case ', i, ' failed.', expect, ret
    #print ret
    if not check_sort(ret):
        print 'Test Case ', i, ' failed.',  ret
