# -*- coding: UTF-8 -*-
import time
import math
# 算法分为初始化和更新2个阶段：
# 初始化：
#   if nums[i+1] > nums[i] 表示第一次发现有需要交换的，于是设置 beg end max_ min_及found标志
# 更新：
#   更新阶段只需要判断nums[i+1]和min_ max_的大小即可。 不管它是升序还是降序。
#   if nums[i+1] < min_ 表示需要更新beg和min_  并且设置end为i+1
#   if nums[i+1] < max_ 则更新end即可
#   else 更新max_
# 此方法更加简洁，效率更高。  可优化的地方是end的赋值。

def findUnsortedSubarray(nums, case_id):
    found = False
    min_ = None
    max_ = None
    beg = None
    end = None

    for i in range(len(nums) - 1):
        if not found:
            if nums[i+1] < nums[i]:
                beg = i
                end = i + 1
                max_ = nums[i]
                min_ = nums[i+1]
                found = True
                beg = update_beg_pos(nums, beg, nums[i+1])
        else:
            if nums[i+1] < min_:
                beg = update_beg_pos(nums, beg, nums[i+1])
                min_ = nums[i+1]
                end = i + 1
            elif nums[i+1] < max_:
                end = i + 1
            else:
                max_ = nums[i+1]           

    return 0 if not found else end - beg + 1

def update_beg_pos(nums, pos, target):
    for j in range(pos, -1, -1):
        if nums[j] <= target:
            pos = j+1   
            break
        if j == 0:
            pos = 0

    return pos

test_list1 = []
test_list2 = []
max_test = 10000
for i in range(max_test):
    a = i if i%2 ==0 else -i                 # 0 -1 2 -3 4 
    b = i if i < max_test/2 else max_test-i  # 0 1 2 3 4 3 2 1
    test_list1.append(a)
    test_list2.append(b)

test_list3 = [0] * max_test  # 1 3 5 6 4 2
for i in range(int(math.ceil(max_test / 2))):
    test_list3[-i] = 2*i+1     
    test_list3[i] = 2*i 
    
# 用例为上一个解法的用例，未新更改。
testcases = [
                [ [], 0],                           # [] 
                [ [1,2,3,4,5], 0],                  # normal increase
                [ [2, 6, 4, 8, 10], 2],             # one decrease, num[i-1] > num[i+1] 
                [ [2, 6, 1, 8, 10], 3],             # one decrease, num[i-1] < num[i+1]
                [ [2, 6, 2, 8, 10], 2],             # one decrease, num[i-1] == num[i+1]
                [ [6, 2, 8, 10], 2],                # one decrease, num[i-1] not exist
                [ [6, 7, 8, 2], 4],                 # one decrease, N_flag branch 2.
                [ [1,2,4,3,5,6,3], 5],              # 2 decrease, num[i+1] >= min_num
                [ [1,2,4,3,5,6,2], 5],              # 2 decrease, num[i+1] < min_num, num[i+1] == num[m-1]
                [ [1,2,4,3,5,6,1], 6],              # 2 decrease, num[i+1] < min_num, num[i+1] < num[m-1]
                [ test_list1, max_test],            # performance  N_flag和M_flag流程交替，但是m不会移动。
                [ test_list2, max_test-2],          # performance  从max_test/2开始，每次走N_flag brach2
                [ test_list3, max_test-1],          # performance 每次M_flag都走完整流程
                [ [1,3,5,4,2], 4],                  # Failed case added. 
                [ [2,4,3,1,5], 4],                  # Failed case added.  
                [ [2,6,4,8,10,9,15], 5],            # Failed case added. 
                [ [2,5,3,1,4], 5],                  # Failed case added.
                [ [2,5,4,1,3], 5],                  # Failed case added. 
                [ [1,2,3,4,5,5,4,3,2,1,1,2,3,4,5], 13] # Failed case added. 
                
            ]

now = time.time()
for case in testcases:
    nums = case[0]
    expect = case[1]
    case_id = testcases.index(case)
    ret = findUnsortedSubarray(nums, case_id)
    if expect != ret:
        print "Test Case ", case_id, "Failed. ", expect, ret

end = time.time()
print "%.3f ms" %((end - now) * 1000)

