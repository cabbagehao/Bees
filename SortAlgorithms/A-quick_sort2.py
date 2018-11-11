import random

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

def quick_sort(nums, left, right):
    if left >= right:
        return nums

    idx = _patition(nums, left, right)
    quick_sort(nums, left, idx-1)
    quick_sort(nums, idx+1, right)
    return nums


random.seed(5)
nums = random.sample(xrange(2000), 20)
print quick_sort(nums, 0, len(nums)-1)