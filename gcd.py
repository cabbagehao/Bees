### 最大公约数 ###
"""
    先来证明欧几里得的辗转相除法正确性。
    a == k * m;
    b == k * n;
    设r为a/b的余数， x为a/b
    r = a - x*b
      = k*m - x*k*n
      = (m-n*x) * k
    即 r也是k的倍数， 且这个倍数比m和n要小（因为r是余数嘛，自然比b要小)。
    如果r == 0， 则a能够被b整除，最大公约数即为b。 否则题目等价转化为求b和r的公约数
    因此另a = b,  b = r再次循环。 这样就得到越来越小的k倍数。 直到余数为0时得到k。
"""

# fraction.py里的gcd使用的此方法， cpython里使用的另一种移位的方法。
def gcd_1(a, b):
    while b:
        a, b = b, a % b
    return a

# 减法版本类似， a和b的差也是它们的最大公约数k乘一个值
def gcd_2(a, b):
    while b:
        if a > b:
          a -= b
        else:
          b -= a
    return a

def gcd_3(a, b):
    # TODO:other solution.
    pass

### 最小公倍数 ###
"""
  定理证明：  GCD(a, b) * LCM(a, b) == a * b
  设
    a == k * m;
    b == k * n;
    其中 k为最大公约数，m n一定是互质的正整数
    最小公倍数则是 m * n * k == a * b / k
"""
def lcm(a, b):
  return a * b / gcd(a, b)
