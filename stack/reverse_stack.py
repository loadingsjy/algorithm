from copy import deepcopy


def reverseStack(stack):
    if not stack:
        return stack
    else:
        top = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack, top)
        return stack


def insertAtBottom(stack, value):
    if not stack:
        stack.append(value)
    else:
        top = stack.pop()
        insertAtBottom(stack, value)
        stack.append(top)


def bottemOut(stack):
    """函数功能：把栈底元素拿出来返回，上面元素盖下来"""
    result = stack.pop()
    if not stack:
        return result
    else:
        last = bottemOut(stack)
        stack.append(result)
        return last


def reverseStack_v2(stack):
    """时间复杂度：O(n^2)"""
    if not stack:
        return
    i = bottemOut(stack)
    reverseStack_v2(stack)
    stack.append(i)


if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    print(stack)
    stack_1 = deepcopy(stack)
    stack_2 = deepcopy(stack)

    reverseStack(stack_1)
    print(stack_1)
    reverseStack_v2(stack_2)
    print(stack_2)
