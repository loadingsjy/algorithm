def deepth(stack):
    """不改变栈的数量状况，返回栈的最大深度"""
    if not stack:
        return 0
    num = stack.pop()
    deep = deepth(stack) + 1
    stack.append(num)
    return deep


def stack_max(stack, deepth):
    """不改变栈的数量状况，返回深度为deepth的栈的最大值"""
    if deepth == 0:
        return float("-inf")
    num = stack.pop()
    rest_max = stack_max(stack, deepth - 1)
    res = max(num, rest_max)
    stack.append(num)
    return res


def times(stack, deepth, num):
    """不改变栈的数量状况，返回深度为deepth的栈num出现的次数"""
    if deepth == 0:
        return 0
    n = stack.pop()
    t = times(stack, deepth - 1, num) + (1 if n == num else 0)
    stack.append(n)
    return t


def down(stack, deepth, max_num, times):
    """不改变栈的数据的相对位置状况，把出现times的max_num数字沉底"""
    if deepth == 0:
        for _ in range(times):
            stack.append(max_num)
        return
    num = stack.pop()
    down(stack, deepth - 1, max_num, times)
    if num != max_num:
        stack.append(num)


def sort_stack(stack):
    """时间复杂度：O(n^2)"""
    deep = deepth(stack)
    while deep > 0:
        max_num = stack_max(stack, deep)
        k = times(stack, deep, max_num)
        down(stack, deep, max_num, k)
        deep -= k


if __name__ == "__main__":
    stack = [3, 7, 2, 9, 4, 3, 5, 3, 7, 8, 1]
    sort_stack(stack)
    print(stack)
