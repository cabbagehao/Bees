# 初始化一个列表（以2开始）
# 从第一个值2开始取，去掉所有可以被2整除的数
# 然后取第二个数3，去掉所有可以被3整除的数。   
# 因为当前取的这个数，如果不是素数，肯定被删除掉了。 因此只需要考虑删除它的倍数。

def prime_number(num):
    prime_list = [ i for i in range(2, num, 1)]
    for i in prime_list:
        for j in prime_list:
            if j % i == 0:
                prime_list.remove(j)
    print prime_list
