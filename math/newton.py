import random

def newton_sqrt(x):
    """牛顿迭代法求根号x"""
    x = float(x)
    if x == 0:
        return 0.0
    return sqrt_my_iter(2.0, x)


def sqrt_my_rec(i, x):
    res = (i + x / i) / 2.0
    if abs(res - i) < 1e-9:
        return res
    else:
        return sqrt_my_rec(res, x)
    
    
def sqrt_my_iter(i, x):
    res = (i + x / i) / 2.0
    while abs(res - i) > 1e-9:
        i = res
        res = (i + x / i) / 2.0
    return res
        


if __name__ == "__main__":
    
    for i in range(10000):
        num = random.randint(2,9999)
        if abs(sqrt_my_iter(2.0, num) - sqrt_my_rec(2.0, num)) > 1e-8:
            print('error')
            
    print('success')
        
    
    print(newton_sqrt(7))
