# 某部门租用公共双人自行车，每辆自行车最多坐两人，自行车最大载重M，
# 给出部门每个人的体重，请问最少需要租用多少量双人自行车

import sys


# 贪心算法
def count_min_bike(weights, n, m):
    if n <= 1:
        return 1
    weights.sort()

    res = []
    left = 0
    right = n - 1
    while left < right:
        if weights[left] + weights[right] <= m:
            res.append((left, right))
            left += 1
            right -= 1
        else:
            right -= 1
    min_count = len(res) + (n - len(res) * 2)
    return min_count


if __name__ == "__main__":
    # questions = []
    # for line in sys.stdin:
    #     if not line.strip():
    #         break
    #     questions.append(str(line.strip()))

    # m = int(questions[0].split()[0])
    # n = int(questions[0].split()[1])
    # weights = list(map(int, questions[1].split()))
    # sys.stdout.write(str(count_min_bike(weights, n, m)) + "\n")

    weights = [10, 4, 3, 2, 6, 9, 2, 4, 5, 7]
    n = len(weights)
    m = 7
    print(count_min_bike(weights, n, m))
