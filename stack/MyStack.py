#
# * 225. 用队列实现栈

# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
# 实现 MyStack 类：
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

# 注意：
# 你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
# 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。


class MyStack:
    """入栈操作时，首先将元素入队到 queue2，然后将 queue1的全部元素依次出队并入队到 queue2，
    此时 queue2的前端的元素即为新入栈的元素，再将 queue1和 queue2互换，
    则 queue1的元素即为栈内的元素，queue1的前端和后端分别对应栈顶和栈底。"""

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


# TODO 用一个队列实现栈的方法：
# * 简单来说就是把队列当成一个环用，每次都把除了队列末端的元素都出队然后依次加到原本末端元素的后端，
# * 这样原本最后的元素就被推到了队列最前端，实现了 Last In First Out。


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
