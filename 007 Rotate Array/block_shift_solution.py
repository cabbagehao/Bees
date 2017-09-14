class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 
        k %= nums_len
        if k == 0:        
            return 

        pos = (nums_len - k) % nums_len
        temp_1 = nums[pos:]
        temp_2 = nums[:pos]
        nums[0:k] = temp_1
        nums[k:] = temp_2
        
        
testcases = [
                [ [], 5, [] ],                  # nums is null
                [ [1,2,3,4], 2, [3,4,1,2] ],    # K < len
                [ [1, 2,3,4], 6, [3, 4,1,2] ],  # k > len 
                [ [1, 3, 5, 7], 4,[1,3,5,7]],   # k = len
                [ [1, 2,3,4], 0, [1,2,3,4] ],   # k = 0
                [ [1, 2,3,4], -1, [2,3,4,1] ],  # k < 0
                [ [1,2] ,1, [2,1] ],
                [ [1,2,3], -3, [1,2,3]],        # k = -len
            ]

for case in testcases:
    nums = case[0]
    k = case[1]
    expect = case[2]
    case_id = testcases.index(case)
    ret = rotate(nums, k)
    if expect != nums:
        print "Test Case ", case_id, "Failed. ", expect, nums
