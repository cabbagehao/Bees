# 牛顿法 （此方法可以推广到开任意次根号。)
# 选取一点作为Xn，用下式反复计算Xn+1,直到Xn+1的平方与目标值非常接近。
# Xn+1 = xn - f(Xn)/f'(Xn)  

# 牛顿法原理
#  求目标值的平方根可理解为求 f(x) = x*x - target 的零点。
#  设X0为f(x)的零点， a为接近零点的值。
#  取一阶泰勒公式： F(x) = f(a) + f'(a)(x-a) = 0 移项可得牛顿法的式子。
#     当F(x)取无穷阶的泰勒公式时，求得的a == X0。 但是高阶泰勒公式求解a变得很困难，因此取1阶。
#     由于忽略掉了后面的项，因此F(x) = 0时，f(x)并不等于0而是接近0. 但此时求得的x比a要更靠近零点了
#     （因为a是随便在零点附近取的，而如果不舍弃高阶项的话，此时x就是零点，但舍弃了一些，所以偏离零点，可也比a更靠近零点）
#     认同了x比a更靠近零点的结论，则可以开始递推，每次迭代都能得到更靠近零点的值。

# 截距方式理解：
# 在原方程上取一点(x0,y0),设该点切线交x轴于x1,则切线方程为：
# k*(x1-x0) = 0-y0
# 即 x1 = x0 - y0/k, y0即为f(x0), k为f'(x0),故:
# x1 = x0 - f(x0)/f'(x0), 故只要理解x1比x0更靠近零点就可以递推了。

# 开1平方计算4次， 开1001平方计算8次， 1000000 -- 13     100000000 -- 17. 可以看到非常的高效。

def sqrt_cacl_newton(num, case_id):
    if num < 0:
        return False
    
    x = 1.0*num / 2
    while abs(x**2 - num) > 0.0001:
        xn = x - (x**2 - num) / (2*x)
        x = xn
        
    return x

TestCase = [    [1, 1],
                [9, 3],
                [2, 1.41421568627],
                [1001, 31.6385840391], 
            ]           




for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase[0]
    expect = testcase[1]
    ret = sqrt_cacl_newton(nums, i)
    if abs(expect - ret) > 0.0001:
        print 'Test Case ', i, ' failed.', expect, ret
        
