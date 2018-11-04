#coding:utf-8
from __future__ import division
import copy

# way1
''' 
    非常笨的方法。 轮询4个操作数，轮询4个操作， 且轮询括号位置。 
    在4个数时，总过计算了7千多次。 way2计算2千多次。 但是依然不够性能
'''
# way2
'''
    第一个计算
        4个数字挑2个，4个op挑1个
    第二个计算
        3个数字挑2个，4个op挑1个
    第三个计算
        2个数字，4个op挑1个
    
    如果是* 和 +， 则跳过交换操作数的式子
    优点：
        这种方法不需要考虑如何打括号。 打括号的意义也就就是对某2个数优先计算。
        直接将计算分为3步，每一步都枚举2个数出来。 并且可以方便扩展到计算N个数的问题
        列表里直接储存计算的表达式str，避免了得到结果得不到式子的问题。
    缺点：
        搜索空间仍然巨大， 4个数2500多， 5个数直接到14W了。。
    优化：
        1. 交换律去重。  搜索空间：2500 -> 1960
        2. 3操作数的交换律去重   //依赖优化3的实现
        3. 不再考虑 /和-,全变为+和*， 每个数字 都有变负、变为倒数;  //todo
'''    
# way2:
# 去除交换律产生的重复式子
# 全局的list,每一个enumete都应该去重
dup_list = []
def enumate_all_pair_in_list(item_list, op_list):
    for pos1, item1 in enumerate(item_list):
        for pos2, item2 in enumerate(item_list):
            if pos1 == pos2:
                continue
            for op in op_list:
                if op == '+' or op == '*':
                    dup_list.append((item2, item1, op))
                if (item1, item2, op) not in dup_list:
                    yield item1, item2, op

def to_eval_str(a, b, op, no_bracket=False):
    # same_level = ['/':'*', '+':'-']
    # 如果a b带1个括号，则判断能不能将其括号去掉，外面再加括号
    # 如果带了2个括号，则其括号是不能去掉的。 TODO
    # if a.count('(') == 1:
    #     inner_op = a[3]
    #     if same_level.get(inner_op) == op:
    #         a = a[1:-1]
    # if b.count('(') == 1:
    #     inner_op = b[3]
    #     if same_level.get(inner_op) == op:
    #         b = b[1:-1]

    if no_bracket:
        return '%s %s %s' %(a, op, b)
    else:
        return '(%s %s %s)' %(a, op, b)

def get_eval_value(eval_str):
    try:
        result = eval(eval_str)
    except ZeroDivisionError:
        return -1
    return result

def loop_enumate(num_str_list, op_list):
    all_calc_str = []
    if len(num_str_list) == 2:
        x_last, y_last = num_str_list
        for op_last in op_list:
            calc_str = to_eval_str(x_last, y_last, op_last, no_bracket=True)
            all_calc_str.append(calc_str)
        return all_calc_str

    for x, y, op in enumate_all_pair_in_list(num_str_list, op_list):
        next_stage = copy.copy(num_str_list)
        next_stage.remove(x)
        next_stage.remove(y)
        calc_str = to_eval_str(x, y, op)
        next_stage.append(calc_str)
        all_calc_str.extend(loop_enumate(next_stage, op_list))
    return all_calc_str

def main():
    num_list = [3, 5, 9, 4]
    # way1
    # for a in num_list:
    #     for b in num_list:
    #         for c in num_list:
    #             for d in num_list:
    #                 if len(set([a, b, c, d])) != 4:
    #                     continue
    #                 loop_each_op([a, b, c, d])

    # way2
    num_str_list = ['3', '5', '9', '4']
    all_calc_str = loop_enumate(num_str_list, op)
    for calc_str in all_calc_str:
        result = get_eval_value(calc_str)
        print(calc_str)
        # if result == 24:
        #     print(calc_str)
   
op = ['+', '-', '*', '/']
main()


#********** way 1************#
'''
def fun(a, b, op):
    if op == '+':
        return a + b
    if op =='-':
        return (a - b)
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            return -999
        else:
            return 1.0*a / b
    else:
        print('error')

def add_bracket(calc_str, order_list):
    calc_list = list(calc_str)
    for order in order_list:
        # find index
        index = -1
        cnt = 0
        for i in range(len(calc_list)):
            if calc_list[i] in op:
                cnt += 1
                if cnt == order:
                    index = i
                    break

        assert index != -1, str(calc_list) + ' ' + str(order_list) + ' ' + str(order)
        
        check_list = ['(', ')']
        # look ahead to insert '('
        tmp_list = []
        for i in range(index, -1, -1):
            if calc_list[i].isdigit() and not tmp_list:
                calc_list.insert(i, '(')
                break
            if calc_list[i] == ')':
                tmp_list.append(calc_list[i])
            elif calc_list[i] == '(':
                if tmp_list[-1] == ')':
                    tmp_list.pop()
                if not tmp_list:
                    calc_list.insert(i, '(')
                    break
        # print(calc_list, index)
        # look behind to insert ')'
        tmp_list = []
        for i in range(index+1, len(calc_list)):
            if calc_list[i].isdigit() and not tmp_list:
                calc_list.insert(i+1, ')')
                break            
            if calc_list[i] == '(':
                tmp_list.append(calc_list[i])
                continue
            elif calc_list[i] == ')':
                if tmp_list[-1] == '(':
                    tmp_list.pop()
                if not tmp_list:
                    calc_list.insert(i+1, ')')
                    break      
    calc_str = ''.join(calc_list)             
    # print(calc_str)
    return calc_str

def check_high_level(op_list):
    return op_list.count('/') + op_list.count('*')

def new_fun(num_list, op_list, order_list):
    # print(num_list, op_list, order_list)
    calc_str = str(num_list[0])
    for i in range(len(op_list)):
        calc_str += op_list[i] + str(num_list[i+1])
    calc_str_with_brac = add_bracket(calc_str, order_list)
    try:
        result = eval(calc_str_with_brac)
    except ZeroDivisionError:
        pass
    else:
        if result == 24:
            print(calc_str_with_brac + ' = 24')
    # print(calc_str, calc_str_with_brac)
        # num_list[pos] = calc_str
        # del(num_list[pos+1])

def loop_each_op(num_list):
    order_list = [1, 2, 3]
    for i in op:
        for j in op:
            for k in op:
                op_list = [i, j, k]
                # run_with_no_bracket(i, j, k, num_list)
                # run_with_bracket(i, j, k, num_list)
                high_cnt = check_high_level(op_list)
                if high_cnt == 3 or high_cnt == 0:
                    new_fun(num_list, op_list, order_list[:2])
                else:
                    for x in order_list:
                        for y in order_list:
                            if len(set([x, y])) != 2:
                                continue
                            new_fun(num_list, op_list, [x, y])
'''
