# 中国象棋的棋盘，棋盘大小为9×10，(0,0)位置有一个“馬”棋子，要求给定目标坐标(a,b)，马必须跳k步到达目标地点，求总的跳法的方法数
import numpy as np

def horse_jump_recursive(x, y, steps):
    '''潜台词：从(0,0)出发，要去往(x,y)，剩下必须需要走steps步。返回方法数。'''
    if x < 0 or y < 0 or x > 8 or y > 9:     # 超出棋盘
        return 0
    if steps == 0:      # 没有步数了
        return 1 if (x, y) == (0, 0) else 0
    return (
        horse_jump_recursive(x - 2, y - 1, steps - 1)
        + horse_jump_recursive(x - 2, y + 1, steps - 1)
        + horse_jump_recursive(x - 1, y - 2, steps - 1)
        + horse_jump_recursive(x - 1, y + 2, steps - 1)
        + horse_jump_recursive(x + 1, y - 2, steps - 1)
        + horse_jump_recursive(x + 1, y + 2, steps - 1)
        + horse_jump_recursive(x + 2, y - 1, steps - 1)
        + horse_jump_recursive(x + 2, y + 1, steps - 1)
    )


def horse_jump_dp(x, y, steps):
    if x < 0 or y < 0 or x > 8 or y > 9:     # 超出棋盘
        return 0
    dp = np.zeros((9, 10, steps+1), dtype=int)
    dp[0,0,0] = 1
    for i in range(1, steps+1):
        for j in range(9):
            for k in range(10):
                dp[j,k,i] = (
                    getValue(dp, j-2, k-1, i-1)
                    + getValue(dp, j-2, k+1, i-1)
                    + getValue(dp, j-1, k-2, i-1)
                    + getValue(dp, j-1, k+2, i-1)
                    + getValue(dp, j+1, k-2, i-1)
                    + getValue(dp, j+1, k+2, i-1)
                    + getValue(dp, j+2, k-1, i-1)
                    + getValue(dp, j+2, k+1, i-1)
                )
    return dp[x,y,steps]
    
def getValue(dp, x, y, steps):
    if x < 0 or y < 0 or x > 8 or y > 9:     # 超出棋盘
        return 0
    return dp[x,y,steps]


if __name__ == '__main__':
    print(horse_jump_recursive(5, 5, 6))
    print(horse_jump_dp(5, 5, 6))
    print(horse_jump_dp(7, 7, 10))



