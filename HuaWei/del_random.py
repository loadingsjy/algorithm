# 2.明明的随机数
# 明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
# 数据范围： 1≤n≤1000
# 1≤n≤1000  ，输入的数字大小满足 1≤val≤500
 
import sys

# 时间复杂度O(500+n)
# 空间复杂度O(500+n)
def del_random(arr, n):
    res = []
    nums = [0] * 500
    for n in arr:
        nums[n-1] = n
    for i in range(500):
        if nums[i] == 0:
            continue
        else:
            res.append(nums[i])
    return res



if __name__ == '__main__':
    questions =[]
    for line in sys.stdin:
        if not line.strip():
            break
        a = int(line.strip())
        questions.append(a)
    n = questions[0]
    arrs = questions[1:]
    # assert n == len(arrs)
    res = del_random(arrs, n)
    sys.stdout.write('\n'.join(map(str, res)))