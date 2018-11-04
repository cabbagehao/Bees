"""
比较高效的幂运算方法。
只需要计算log(b)次平方  （log(b)/2奇数次的乘法）
"""

def Pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    
    if b % 2 == 0:
        Pow(a*a, b/2)
    else:
        Pow(a*a, b/2) * a
