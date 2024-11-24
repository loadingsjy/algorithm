# a~z的所有子序列按照字典序排序，给定字符串s，问s是这些子序列的第几个？


# 必须以i号字符开头，长度为l的子序列有多少个？(i从1开始，即a代表1，b代表2，c代表3...)
def g(i, l):
    count = 0
    if l == 0:
        return 0
    if l == 1:
        return 1
    for j in range(i + 1, 27):
        count += g(j, l - 1)
    return count


# 长度为l的子序列有多少个？
def f(length):
    count = 0
    for i in range(1, 27):
        count += g(i, length)
    return count


def kth(s):
    count = 0
    l = len(s)

    # 长度小于l子序列都排在前面(长度至少为1)
    for i in range(1, l):
        count += f(i)
    # print(count)
    
    frist = ord(s[0]) - ord("a") + 1
    # 长度为l,第一个字符序小于s[0]的子序列都排在前面
    for i in range(1, frist):
        count += g(i, l)
        
    # print(count)
    pre = frist
    for i in range(1, l):
        cur = ord(s[i]) - ord("a") + 1
        for j in range(pre + 1, cur):
            count += g(j, l - i)
        pre = cur
    return count + 1


if __name__ == "__main__":
    # print(f(5))
    # print(g(4, 3))

    s = "abcfg"
    print(kth(s))
