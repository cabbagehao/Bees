# 1. 生成k+2数组 num_plus < Failed  Time limit exceeded.>
# 遍历nums_plus，如果在nums中有，则表示匹配，加入到set
# 返回set个数

# 2. 直接遍历原数组查找 < Passed >
# 如果数组中有nums[i] +ｋ，则count + 1 (储存到set or dict都太耗时间了)

import time

now = time.time()

def findPairs(nums, k):
    if k < 0:
        return 0

    count = 0
    nums_set = set(nums)
    if k == 0:
        for item in nums_set:
            if nums.count(item) > 1:
                count += 1
        return count

    for item in nums_set:
        if item + k in nums_set:
            count += 1

    return count


testcases = [
                [ [3,1,4,1,5], 2, 2 ],  # k = 2
                [ [1,2,3,4,5], 1, 4 ],  # k = 1
                [ [3,1,4,1,5], 0, 1 ],  # k = 0
                [ [1,2,3,4,5], -1, 0 ], # k = -1
                [ [1,3,3,5,5], 1, 0 ],  # expect 0
                [ [ i for i in range(10000)], 1, 9999],  # performance
            ]

for case in testcases:
    nums = case[0]
    k = case[1]
    expect = case[2]
    case_id = testcases.index(case)
    ret = findPairs(nums, k)
    if expect != ret:
        print "Test Case ", case_id, "Failed. ", expect, ret

end = time.time()
print "%.3f ms" %((end - now) * 1000)

