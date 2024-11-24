# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 示例 2：

# 输入：height = [4,2,0,3,2,5]
# 输出：9

# 双指针法
def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:                
                water += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1
    return water

# 单个位置water[i]的水量 = max{[min(左边最大高度值, 右边最大高度值) - 当前位置高度height[i]], 0}

def trap_v2(height: list[int]) -> int:
    n = len(height)
    water = [0] * n
    max_left = 0
    for i in range(n):
        max_left = max(max_left, height[i])
        water[i] = max_left
    max_right = 0
    for i in range(n-1, -1, -1):
        max_right = max(max_right, height[i])
        water[i] = min(water[i], max_right) - height[i]
    return sum(water)


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height)) # 6
    print(trap_v2(height)) # 6

    height = [4,2,0,3,2,5]
    print(trap(height)) # 9
    print(trap_v2(height)) # 9
    
    height = [4,2,1,3,2,5]
    print(trap(height))
    print(trap_v2(height))