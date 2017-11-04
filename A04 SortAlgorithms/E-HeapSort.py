#!/usr/bin/python
#*_coding:utf-8_*
"""
    建立二叉堆需要O(N)时间， 然后执行N次DeleteMin操作，最小的元素先离开堆。
    将这些元素记录到另一个数组再拷贝回来，就得到N个元素的排序。
    每个DeleteMin操作花费O(logN),因此总时间为O(NlogN).
        也可以将每次删除的最小元素储存在堆末尾(堆删除元素后缩小的空间)，来避免另一个数组的空间开销。

    建立大顶堆：
        1. 先将序列完全放入到数组中，组成一棵完全二叉树
        2. 从最后一个非叶子节点开始，调整堆。
"""

        
def max_heapify(nums, index, heap_size, case_id=-1):
    """
        仅仅只调整index位置，调整它的位置使整个堆满足大顶堆。（假定除了index其他位置都是满足的）
        
        判断index的2个孩子是否有比它大的：
            如果是，则交换最大的孩子
            如果不是，则不交换。
        接着判断index的左孩子，右孩子， 左孩子的孩子， 如果index的左右孩子都比它小，则局部满足堆性质，
        函数返回。（因为假定其他位置是满足堆性质的，所以index这个局部满足后整个堆就满足了）            

    """
    if index >= heap_size:
        return
    max_idx = index
    left_idx = index*2 + 1
    right_idx = index*2 + 2

    if left_idx < heap_size and nums[index] < nums[left_idx]:
        max_idx = left_idx
    if right_idx < heap_size and nums[max_idx] < nums[right_idx]:
        max_idx = right_idx

    if max_idx == index:
        return

    nums[index], nums[max_idx] = nums[max_idx], nums[index]
    max_heapify(nums, max_idx, heap_size)

"""
    尝试了不每次只调整一个元素，而是同时调整的元素。 有个问题就是后面更大的元素无法到前面去，因而不会更简单，故放弃这种方法。
    max_idx = index
    open_list = [index]
    child = []
    while True:
        if open_list == [] and child == []:
            break
        if open_list == []:
            child, open_list = open_list, child

        index = open_list.pop(0)
        left_idx = index*2 + 1
        right_idx = index*2 + 2        
        if left_idx < len(nums) and nums[index] < nums[left_idx]:
            max_idx = left_idx
        if right_idx < len(nums) and nums[index] < nums[right_idx]:
            max_idx = right_idx

        nums[index], nums[max_idx] = nums[max_idx], nums[index] 
        child.append(left_idx)  
        child.append(right_idx)
"""

test_nums = [1, 2, 3, 4, 5]
ret_nums = [1, 5, 3, 4, 2]
max_heapify(test_nums, 1, 5)
# python2 assert不能加括号，否则恒为真!!!
assert test_nums == ret_nums, "max_heapify() assert False."


def build_max_heap(nums, heap_size, case_id=-1):
    """
        建立堆可以看做是将整个list max_heapfiy的过程。
        由于heapify一次后，该位置及子节点都满足堆性质，所以可以考虑从后往前遍历。 跳过最底层的叶子节点。
        所以build_max_heap循环n/2遍，max_heapify耗费O(logn),总时间为O(n*logn)
    """
    last_parent = (heap_size-1) / 2     # floor
    for i in range(last_parent, -1, -1):
        max_heapify(nums, i, heap_size)
    return nums

def heap_sort(nums):
    """
        大顶堆的堆顶是最大的，因此将其交换到末尾，并且将堆大小缩小1个，这样这个最大的元素在末尾就不参与
        堆的调整了。 
        其余部分调整后堆顶又是最大了，重复这个过程就可得到从小到大排列的数组。
        时间复杂度： 
            建堆花费O(nlogn)
            每次交换和堆调整花费nlogn
        损失了原数组的顺序信息。 比如case2 本来就是排序的，还是要打乱重排一遍。
    """
    heap_size = len(nums)
    heap = build_max_heap(nums, heap_size)
    while heap_size > 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap_size -= 1
        max_heapify(heap, 0, heap_size)
    nums = heap
    return nums

# [[nums, target, expect]]
TestCase = [    [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5, 6, 7],
                [3, 2, 1, 4, 99, 22, 56, 11, 89],
                [4880, 3, 212, 10, 20413, 3110, 0, 1011, 999],
            ]           
def check_sort(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return False
    return True

def check_max_heap(nums):
    for i in range(len(nums)):
        if 2*i+1 < len(nums) and nums[i] <= nums[2*i+1]:
            return False

        if 2*i+2 < len(nums) and nums[i] <= nums[2*i+2]:
            return False
    return True

for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase
    build_max_heap(nums, len(nums), i)
    ret = nums
    if not check_max_heap(ret):
        print 'Test Case ', i, ' failed.',  ret

        
