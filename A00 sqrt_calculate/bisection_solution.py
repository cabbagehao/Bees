# 2分法查找平方根。
# 1 -- 执行了14次   100000000.5执行了51次。  可以看到同样精度下比牛顿法慢了好几倍。
def sqrt_cacl_newton(num, case_id):
    if num < 0:
        return False

    count = 0
    down = 0
    up = num
    x = 1.0*(up + down)/ 2
    while abs(x**2 - num) > 0.0001:
        if x**2 > num:
            up = x
        else:
            down = x

        x = 1.0*(up + down)/ 2
        count += 1

    print num, count
    return x

# [[nums, target, expect]]
TestCase = [    [1, 1],
                [9, 3],
                [2, 1.41421568627],
                [100000000.5, 31.6385840391], 
            ]           




for i in range(len(TestCase)):
    testcase = TestCase[i]
    nums = testcase[0]
    expect = testcase[1]
    ret = sqrt_cacl_newton(nums, i)
    if abs(expect - ret) > 0.0001:
        print 'Test Case ', i, ' failed.', expect, ret
