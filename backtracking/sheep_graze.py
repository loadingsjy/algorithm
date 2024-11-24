

# 假设草原上有n分草，两只羊分别先后吃草，每只羊只能吃4**k(k=0,1,2,3...)份草，两只羊分先后手吃草，谁先吃完草堆谁就赢。假设两只羊都是聪明的，问是先手赢还是后手赢？

def winner(n):
    if n < 5:
        return '后手' if n == 0 or n == 2 else '先手'
    base = 1
    while base <= n:
        if winner(n-base) == '后手':
            return '先手'
        if base > n / 4:    # 防止base*4之后溢出
            break
        base *= 4
    return '后手'


# **根据第一种方法打印出结果后发现的规律
def winner_v2(n):
    if n % 5 == 0 or n % 5 == 2:
        return '后手'
    else:
        return '先手'
    
    
if __name__ == '__main__':
    n = 11
    print(winner(n)) # Output: "First"
    print(winner_v2(n)) # Output: "First"