# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

# 示例 1：
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 示例 2：
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。

# 思路：
# 我们可以将「相邻的孩子中，评分高的孩子必须获得更多的糖果」这句话拆分为两个规则，分别处理。
# 左规则：当 ratings[i−1]<ratings[i] 时，i 号学生的糖果数量将比 i−1 号孩子的糖果数量多。
# 右规则：当 ratings[i]>ratings[i+1] 时，i 号学生的糖果数量将比 i+1 号孩子的糖果数量多。
# 我们遍历该数组两次，处理出每一个学生分别满足左规则或右规则时，最少需要被分得的糖果数量。每个人最终分得的糖果数量即为这两个数量的最大值。
# 具体地，以左规则为例：我们从左到右遍历该数组，假设当前遍历到位置 i，如果有 ratings[i−1]<ratings[i] 那么 i 号学生的糖果数量将比 i−1 号孩子的糖果数量多，我们令 left[i]=left[i−1]+1 即可，否则我们令 left[i]=1。



def candy(ratings: list[int]) -> int:
    n = len(ratings)
    left = [1] * n
    for i in range(n-1):
        if ratings[i] < ratings[i+1]:
            left[i+1] = left[i] + 1

    right = [1] * n
    for i in range(n-1,0,-1):
        if ratings[i-1] > ratings[i]:
            right[i-1] = right[i] + 1

    answer = [max(left[i], right[i]) for i in range(n)]
    print(answer)
    return sum(answer)


if __name__ == '__main__':
    ratings = [1,0,2]
    print(candy(ratings))

    ratings = [1,2,2]
    print(candy(ratings))

    ratings = [1,2,3,4,5,6,7,8,9,10]
    print(candy(ratings))

    ratings = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
    print(candy(ratings))

    ratings = [1,2,3,3,3,2,1,3,3,1,2,4,2]
    print(candy(ratings))