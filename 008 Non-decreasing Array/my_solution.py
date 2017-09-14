
# 0-n遍历
# 1. 如果没有小于，pass
# 2. 如果有1个小于，检查小于前后是否相差>0
    # 1. 将 nums[i+1] 变大
    # 2. 将 nums[i] 变小
# 3. 如果有2个及以上的小于，failed

def checkPossibility(nums):
    count = 0
    for i in range(len(nums) - 1):
        pass
        if nums[i + 1] < nums[i]:
            count += 1
            if count > 1:
                return  False
            else:
                
                if i == 0:
                    continue
                
                if i+1 == len(nums)-1:
                    return True
                # Decrease nums[i]   and     Increase  nums[i+1]
                if nums[i+1] < nums[i-1] and nums[i+2] < nums[i]:
                    return False
    return True


testcases = [
                [ [], True ],           # nums is null
                [ [1,2,3], True ],      # normal
                [ [1,2,5,4,7], True ],  # num[i+2] > num[i] and num[i+1] > num[i-1]
                [ [1,2,5,4,4], True],   # num[i+2] < num[i]  and num[i+1] > num[i-1]
                [ [1,3,5,1,2], False],  # num[i+2] < num[i]  and num[i+1] < num[i-1]
                [ [1,2,5,1,7], True ],  # num[i+2] > num[i] and num[i+1] < num[i-1]
                [ [1,2,3,1,3,5,3], False],    # modify twice
                [ [5,4,3,2,1], False ],       # Decrease.
                [ [4,2,3], True],             # i = 0
                [ [1,2,3,-1], True],          # i = len(nums) - 1
                #[ [-1,4,2,3], True],
            ]

for case in testcases:
    nums = case[0]
    
    expect = case[1]
    case_id = testcases.index(case)
    ret = checkPossibility(nums)
    if expect != ret:
        print "Test Case ", case_id, "Failed. ", expect, ret



