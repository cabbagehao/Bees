"""
先看一个有趣定理的证明。
GCD为最大公约数， LCM为最小公倍数
定理证明：  GCD(a, b) * LCM(a, b) == a * b
设
  a == k * m;
  b == k * n;
  其中 k为最小公约数，m n会互质的正整数（一定是存在的）
a * b = k*k* m *n,  因为k为最小公约数。 因此 k*m*n为最小公倍数。 定理得证。
"""

"""
  现在来证明欧几里得的辗转相除法正确性。
  a == k * m;
  b == k * n;
  设r为a/b的余数， x为a/b
  r = a - x*b
    = k*m - x*k*n
    = (m-n*x) * k
    
  即 r也是k的倍数， 且这个倍数比m和n要小（因为r是余数嘛，自然比b要小)。  
  因此另a = b,  b = r再次循环。 这样就得到越来越小的k倍数。 直到余数为0时得到k。
"""

def gcd(a, b):
    if a < b:
        a, b = b, a
    while(a % b > 0):
        rem = a % b
        a = b
        b = rem
    return a
