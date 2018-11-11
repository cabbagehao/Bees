def _patition(nums, i, j):
    pivot = nums[i]
    while i < j:
        while nums[j] > pivot:
            j -= 1
            if i == j: break
        else:
            nums[i] = nums[j]
            i += 1

        if i == j: break

        while nums[i] < pivot:
            i += 1
            if i == j: break
        else:
            nums[j] = nums[i]
            j -= 1
    nums[i] = pivot
    return i

def topk_with_quick_sort(nums, left, right, k):
    if left >= right:
        return nums

    idx = _patition(nums, left, right)
    if idx == k:
        return nums[:k]
    elif idx > k:
        topk_with_quick_sort(nums, left, idx-1, k)
    else:
        topk_with_quick_sort(nums, idx+1, right, k)
    return nums[:k]

import random
import copy
random.seed(5)
nums = random.sample(xrange(2000), 20)
nums_copy = copy.copy(nums)
print sorted(nums_copy)
print topk_with_quick_sort(nums, 0, len(nums)-1, 5)    