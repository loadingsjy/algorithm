# 纸牌游戏
# 两个人轮流拿走数组中的纸牌，每次只能拿走最左或者最右边的纸牌，最后谁纸牌的总和最大，谁获胜。(数组中数组都是正数)


# 先手函数
def frist(arr, left, right):
    if left == right:
        return arr[left]
    return max(
        arr[left] + second(arr, left + 1, right),
        arr[right] + second(arr, left, right - 1),
    )


# 后手函数
def second(arr, left, right):
    if left == right:
        return 0
    return min(frist(arr, left + 1, right), frist(arr, left, right - 1))


# 主函数
def cards_game(arr):
    if len(arr) == 0:
        return 0
    frist_score = frist(arr, 0, len(arr) - 1)
    second_score = second(arr, 0, len(arr) - 1)
    
    if frist_score > second_score:
        print("First player wins!")
        return frist_score
    elif frist_score < second_score:
        print("Second player wins!")
        return second_score
    else:
        print("It's a tie!")
        return frist_score



if __name__ == '__main__':
    # Example:
    arr = [5, 1, 6, 9, 4, 8, 7, 2, 10]
    print('score: ',cards_game(arr))