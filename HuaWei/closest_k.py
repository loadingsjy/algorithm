# 放暑假了，小明决定到某旅游景点游玩，他在网上搜索到了各种价位的酒店(长度为n的数组Q A),他的心理价位是x元，请帮他筛
# 选出k个最接近x元的酒店(n>=k>0)，并由低到高打印酒店的价格

# 输入描述:
# 第一行:n,k,x
# 第二行A[0]A[1]A[2]...A[n-1]
# 输出描述:
# 从低到高打印筛选出的酒店价格

# 示例一:
# 输入
# 10 5 6
# 1 2 3 4 5 6 7 89 10
# 输出
# 4 5 6 7 8
# 示例二:
# 输入
# 10 4 6
# 10 9 8 7 6 5 4 3 2 1
# 输出
# 4 5 6 7
# 说明
# 数组长度n= 10,筛选个数k=4，目标价位x= 6
# 当4和8距离x相同时，优先选择价格低的4
# 示例三:
# 输入
# 6 3 1000
# 30 30 200 500 70 300
# 输出
# 200 300 500

# 备注:
# 1.酒店价格数组A和小明的心理价位x均为整型数据;(0<,k,x<10000)
# 2.优先选择价格最接近心理价位的酒店，若两家酒店和心理价位差价相同，则选择价格较低的酒店。(比如100元和300元距离心理价
# 位200元同样接近，此时选择100元)
# 3.酒店价格可能相同重复
import functools


def binary_search_right_frist_larger(arr, num):
    low = 0
    high = len(arr) - 1

    if arr[high] <= num:
        return -1  # element not found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= num:
            low = mid + 1
        else:
            high = mid - 1

    return low


# 选出k个最接近x元的酒店
def closest_k(arr, k, x):

    arr.sort()
    n = len(arr)
    index = binary_search_right_frist_larger(arr, x)

    if index == 0:
        return arr[:k]
    if index == -1:
        return arr[n - k :]

    res = []
    right = index
    left = index - 1

    count = 0
    while left >= 0 and right < n:
        if arr[right] - x < x - arr[left]:
            res.append(right)
            right += 1
        else:
            res.append(left)
            left -= 1
        count += 1

        if count == k:
            break

    if count < k:
        if right == n:
            while left >= 0 and count != k:
                res.append(left)
                left -= 1
                count += 1
        if left == -1:
            while right < n and count != k:
                res.append(right)
                right += 1
                count += 1

    return sorted([arr[i] for i in res])


def cmp(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        else:
            return 1
    else:
        return 1


def closest_k_v2(arr, k, x):
    deal = []
    for n in arr:
        deal.append((n, abs(x - n)))

    deal.sort(key=functools.cmp_to_key(cmp))
    # print(deal)
    return sorted([x for x, _ in deal[:k]])


if __name__ == "__main__":
    arr = [1, 2, 4, 7, 8, 9]
    k = 5
    x = 6
    print(closest_k(arr, k, x))
    print(closest_k_v2(arr, k, x))

    arr = [30, 30, 200, 500, 70, 300]
    k = 3
    x = 1000
    print(closest_k(arr, k, x))
    print(closest_k_v2(arr, k, x))
