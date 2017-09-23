# -*- coding: UTF-8 -*-
# 看了下基本都是类似交换head和next的解法。
# 可以尝试一下交换2个/3个/5个，可能速率会有提高，但是判断就更为复杂化。
import time
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head, case_id=-1):
    pre_node = None
    while head is not None :
        next_node = head.next
        head.next = pre_node 
        pre_node = head
        head = next_node
        
    test_list = []
    while pre_node is not None:
        test_list.append(pre_node.val)
        pre_node = pre_node.next
    return test_list
    # return pre_node


case_max = 10000

case_1 = ['a', 'b', 'c', 'd', 'e', 'f']
case_1_rev = ['f', 'e', 'd', 'c', 'b', 'a']

case_2 = [0] * case_max
case_2_rev = [0] * case_max
for i in range(case_max):
    case_2[i] = i
    case_2_rev[case_max-1 - i] = i

def test_case_gen(list_):
    nodes = []
    for i in range(len(list_)):
        nodes.append(ListNode(list_[i]))

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]

    return (nodes, nodes[0]) if nodes != [] else (nodes, None)

testcases = [
                [ [], [] ],                           
                [ ['a'], ['a'] ],
                [ ['a', 'b'], ['b','a']],
                [ case_1, case_1_rev],
                [ case_2, case_2_rev],  # performance
            ]

now = time.time()
for case in testcases:
    nums = case[0]
    (nodes, head) = test_case_gen(nums)
    expect = case[1]
    case_id = testcases.index(case)
    ret = reverseList(head, case_id)
    if expect != ret:
        print "Test Case ", case_id, "Failed. ", expect, ret

end = time.time()
print "%.3f ms" %((end - now) * 1000)

