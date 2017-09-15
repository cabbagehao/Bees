# -*- coding: UTF-8 -*-
import time

now = time.time()

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
# Tail 10%    
    # s = sorted(nums)
    # flag = False 
    # for i in range(len(nums)-1, 0, -1):
    #     if s[i-1] < s[i]:
    #         if flag:
    #             return s[i-1]
    #         else:
    #             flag = True
    # return s[-1]        
# Top 60%
    # s = list(sorted(set(nums)))
    ## s = list(set(nums)).sort()  #This will be more efficient? 15%
    # if len(s) < 3:
    #     return s[-1]
    # else:
    #     return s[-3]

# Top 40%
    # first, second, third = None, None, None

    # for i in nums:
    #     if i > first:
    #         third = second
    #         second = first
    #         first = i
    #     elif i > second and i != first:
    #         third = second
    #         second = i
    #     elif i > third and i != first and i != second:
    #         third = i

    # return first if third is None else third

# Top 30%
    # nums = set(nums)
    # if len(nums) < 3:
    #     return max(nums)

    # nums.remove(max(nums))
    # nums.remove(max(nums))
    # return max(nums)

# Top 20%(类似top 40%)
    # minInt = -2**31
    # max3 = [minInt,minInt,minInt]
    # for num in nums:
    #     if num > max3[0]:
    #         max3[0],max3[1],max3[2] = num, max3[0],max3[1]
    #     elif num < max3[0] and num > max3[1]:
    #         max3[1],max3[2] = num, max3[1]
    #     elif num < max3[1] and num > max3[2]:
    #         max3[2]= num
    # return max3[0] if len(set(nums)) < 3 else max3[2]
# Top 1  amazing.
    return sorted(set(nums))[-3] if len(set(nums))>2 else max(nums)
testcases = [
                [ [3,2,1], 1],      # normal
                [ [-3,-2,-1], -3],      # negtive
                [ [1,2], 2 ],       # no third
                [ [2,2,3,1], 1 ],   # repeat
                [ [ i for i in range(10000)], 9997],  # performance
            ]

for case in testcases:
    nums = case[0]
    expect = case[1]
    case_id = testcases.index(case)
    ret = thirdMax(nums)
    if expect != ret:
        print "Test Case ", case_id, "Failed. ", expect, ret

end = time.time()
print "%.3f ms" %((end - now) * 1000)

