# begin到end范围上找到第i个小的数
def select(arr, begin, end, i):
    if begin == end:
        return arr[begin]

    pivot = medainOfMedians(arr, begin, end)

    pivotRange = partition(arr, begin, end, pivot)

    if i >= pivotRange[0] and i <= pivotRange[1]:
        return arr[i]
    elif i < pivotRange[0]:
        return select(arr, begin, pivotRange[0] - 1, i)
    else:
        return select(arr, pivotRange[1] + 1, end, i)


def medainOfMedians(arr, begin, end):
    n = end - begin + 1
    if n % 5 == 0:
        offset = 0
    else:
        offset = 1

    mArr = [0] * ((n // 5) + offset)
    for i in range(len(mArr)):
        beginI = begin + i * 5
        endI = beginI + 4
        mArr[i] = getMedian(arr, beginI, min(end, endI))

    length = len(mArr)

    return select(mArr, 0, length - 1, length // 2)


def partition(arr, begin, end, pivotValue):
    small = begin - 1
    cur = begin
    big = end + 1
    while cur != big:
        if arr[cur] < pivotValue:
            small += 1
            arr[small], arr[cur] = arr[cur], arr[small]
            cur += 1
        elif arr[cur] > pivotValue:
            big -= 1
            arr[big], arr[cur] = arr[cur], arr[big]
        else:
            cur += 1
    return small + 1, big - 1


def getMedian(arr, begin, end):
    arr.sort()
    s = begin + end
    mid = (s // 2) + (s % 2)
    return arr[mid]


def getMinKthByBFPRT(arr, K):
    copyArr = arr[:]
    return select(copyArr, 0, len(copyArr) - 1, K - 1)


def getMinKNumsByBFPRT(arr, k):
    """BFPRT算法"""
    if k < 1 or k > len(arr):
        return arr

    minKth = getMinKthByBFPRT(arr, k)
    res = [0] * k
    index = 0
    for i in range(len(arr)):
        if arr[i] < minKth:
            res[index] = arr[i]
            index += 1

    while index != len(res):
        res[index] = minKth
        index += 1

    return res


if __name__ == "__main__":
    arr = [2, 23, 45, 6, 3, 677, 67, 43, 15]
    k = 4
    print(getMinKNumsByBFPRT(arr, k))
