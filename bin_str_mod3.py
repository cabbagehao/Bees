'''
一个很长的二进制串，求其除3的余数。
    看到一个很棒的思路，用状态机去实现。 ref:https://blog.csdn.net/Ginray/article/details/77884853
    
    前提结论为： 二进制串加一个0表示2倍，加一个1表示2倍+1
    初始状态为0，遇到1时变为1，遇到0时不变,以此类推（因为遇到0表示加倍，余数仍然为0，遇到1时变为2倍+1，所以余数为1)

    Methods 1 (state merchine): 
        0@0 ==> 0
        0@1 ==> 1

        1@0 ==> 2
        1@1 ==> 0

        2@0 ==> 1
        2@1 ==> 2

    Methods 2(Regular expression):
        1((10*1)|(01*0))*10*
'''
def bin_mod3(bin_str):
    state = 0
    for i in bin_str:
        if state == 0:
            if i == '1':
                state = 1
        elif state == 1:
            if i == '0':
                state = 2
            else:
                state = 0
        elif state == 2:
            if i == '0':
                state = 1
    return state

for num in range(1000):
    bin_str = bin(num)[2:]
    assert bin_mod3(bin_str) == num %3
