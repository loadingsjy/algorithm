
# 给定一个函数f，可以1~5的数字等概率返回一个。请加工出1~7的数字等概率返回一个函数g。

# 给定一个函数f，可以a~b的数字等概率返回一个。请加工出c~d的数字等概率返回一个函数g。

# 给定一个函数f，以p为概率返回0，以1-p为概率返回1。请加工出等概率返回0和1的函数g。


import random

def random_1To5():
    return random.randint(1, 5)

# 由等概率返回1到5的函数构造等概率返回1和0的函数
def random1To5_01():
    while 1:
        res = random_1To5()
        if res == 3:
            continue
        else:
            break
    return 1 if res < 3 else 0

# 由等概率返回0和1的函数构造等概率返回1到7的函数
def random_1To7():
    while 1:
        res = (random1To5_01() << 2) + (random1To5_01() << 1) + (random1To5_01())
        # assert 0 <= res <= 7
        if res == 7:
            continue
        else:
            break
    return res+1

# 由等概率返回a到b的函数构造等概率返回c到d的函数
def random_aTob_cTod(a, b, c, d):
    pass



# 以p为概率返回0，以1-p为概率返回1的函数
def random_p(p):
    if p < 0 or p > 1:
        raise ValueError("p must be between 0 and 1")

    i = random.random()
    if i < p:
        return 0
    else:
        return 1
    
def random_01():
    while 1:
        a = random_p(0.83)
        b = random_p(0.83)
        if (a == 0 and b == 0) or (a == 1 and b == 1):
            continue
        else:
            break
    return 1 if a == 0 and b == 1 else 0
        

if __name__ == '__main__':
    print(random_1To5())
    print(random1To5_01())
    print(random_1To7())
    print(random_01())