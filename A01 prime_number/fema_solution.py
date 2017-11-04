#*_coding:utf-8_*
"""
    测试一个大数是不是素数
    用2到根号N判断的方式不适用于大数

    费马小定理：
        如果P是素数，且0<A<P， 则A^(P-1)与1同余于模P
        比如67是素数，则2^66 % 67 = 1  3^66 % 67 = 1
    所以只要检验2^(N-1) % N是否为1可以大致判断。
        如果不为1，则肯定不是素数
        但如果为1，则 可能 是素数。 因为有一些合数也满足这个式子。 比如341
            可以尝试多个A，减小这种错误的概率
            存在一些数的集合Carmichael数(卡密歇尔数，伪素数)， 这些数不是素数却对所有与N互素的A满足费马小定理。 比如561
    二次探测定理：
        如果P是素数，且X<P那么X**2 % P = 1仅有的2个解为x=1, P-1
        X**2 - 1 % P == 0 意味着 P必然整除x-1或者x+1
        只要不满足这个定理，则可以断言P不是素数。

    生成一张伪素数表对费马定理判断素数进行容错处理，但是生成这个表也比较耗资源。
    Miller-Rabin算法能够很好地解决费马定理的问题A^(P-1)满足后继续测试A^（(P-1)/2）
"""
import random

def witness(a, i, N):
    # return 0 :    N is definitely composite.
    # return 1:     N may be prime.
    if i == 0:
        return 1
    x = witness(a, i/2, N)
    if(x==0):
        return 0

    y = (x*x) % N
    if(y == 1 and x != 1 and x != N-1):
        return 0
    # this section confused me.
    if(i % 2 != 0):
        y = (a*y)%N

    return y

def is_prime(N):
    assert N > 1, "0 or 1 is invalid."
    if N < 4: return True
    a = random.randint(2, N-2)
    ret = witness(a, N-1, N)

    return ret == 1
for i in range(2, 200):
    if is_prime(i):
        print i
