# 直接遍历查找距离最短。
def words_distance(nums, word1, word2):
    nums_len = len(nums)
    min_distance = nums_len
    pos1 = nums_len
    pos2 = nums_len
    for i in range(nums_len):
        if nums[i] == word1:
            pos1 = i
        elif nums[i] == word2:
            pos2 = i
        else:
            continue

        d = abs(pos1 - pos2)
        if d < min_distance:
            min_distance = d 

    return min_distance


testcases = [
                [ ['a','b'], 'a', 'b', 1],
                [ ['a','b','c'], 'a', 'c', 2],
                [ ['a', 'b', 'c', 'a', 'c'], 'a', 'c', 1]
            ]

for case in testcases:
    nums = case[0]
    word1 = case[1]
    word2 = case[2]
    expect = case[3]
    case_id = testcases.index(case)
    ret = words_distance(nums, word1, word2)
    if expect != ret:
        print "Test Case ", case_id, "Failed. ", expect, ret
