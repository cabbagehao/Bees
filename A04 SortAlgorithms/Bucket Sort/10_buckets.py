"""
  只使用10个桶。（实际上是20个，可以优化。）
    第一遍排序将nums中的数放到个位对应的桶中去。 每个桶是一个数组，可以装多个数据。
    第二遍排序将桶中的数放到十位对应的桶（另一个桶）中去。 以此类推。
    * 每次从桶中取数据都要从0号桶取到9号桶。 且桶中数据得按顺序读取。*
  
  正确性验证：
    第一遍时，每个桶中数字的个位数是一样的。
    第二遍时，假如2号桶中有2个数字，则2个数字的十位一样，下面数字的个位数较小。（因为上一轮中个位数小的在小号的桶，因此会先取到它，放到当前桶）
    以此类推，第N遍排序后，每个桶里数字后N位肯定是有顺序的。   所以最终是有顺序的。
  
  复杂度：
    排序的次数是最大值的位数D。 比如1234就要排序4遍（个位/十位/百位/千位）
    每次排序从10个桶中遍历N个数。 因此时间复杂度为 D*O(N)  空间复杂度为 2*O(N)
"""


def get_ith_digit(number, i):
    while i > 1:
        number /= 10
        i -= 1
    return number%10

def get_level_of_number(number):
    n = 0
    while number > 0:
        n += 1
        number /= 10
    return n

assert get_ith_digit(543, 2) == 4
assert get_level_of_number(345600) == 6

def bucket_sort(nums, case_id):
    bucket_num = 10
    buckets = [[] for i in range(bucket_num)]
    buckets_tmp = [[] for i in range(bucket_num)]
    max_num = max(nums)
    dims = get_level_of_number(max_num)

    for num in nums:
        unit = get_ith_digit(num, 1)
        buckets[unit].append(num)

    for i in range(2, dims+1):
        for num_arr in buckets:
            for num in num_arr:
                digit = get_ith_digit(num, i)
                buckets_tmp[digit].append(num)

        buckets = buckets_tmp
        buckets_tmp = [[] for i in range(bucket_num)]

    return [num for num_arr in buckets for num in num_arr]


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
    ret = bucket_sort(nums, i)
    if not check_sort(ret):
        print 'Test Case ', i, ' failed.',  ret
        
        
        
