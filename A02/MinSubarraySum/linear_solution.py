"""
    求最小和，无非就是尽量加负数。
    如果this_num加上num[i]后还是正数，则置零重新计算。
        
"""
def minimum_subarray_sum(nums, case_id):
    min_sum = 100000
    this_sum = 0
    for i in range(len(nums)):
        this_sum += nums[i]
 
        if min_sum < this_sum:
            min_sum = this_sum   
        elif this_sum > 0:
            this_sum = 0
