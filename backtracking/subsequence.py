# 打印字符串的所有子序列


def process(str, i):
    if i == len(str):
        print("".join(str))
        return
    process(str, i + 1)
    temp = str[i]
    str[i] = ""
    process(str, i + 1)
    str[i] = temp


def process_2(str, i, res):
    if i == len(str):
        print("".join(res))
        return

    res_keep = res[:]
    res_keep.append(str[i])
    process_2(str, i + 1, res_keep)  # 要的当前字符的路径

    res_not_include = res[:]
    process_2(str, i + 1, res_not_include)  # 不要的当前字符的路径


def print_all_subsequences(str):
    process(list(str), 0)
    print("\n")
    process_2(list(str), 0, [])


def all_subsequence(s):
    n = len(s)
    path = []
    res = []

    def dfs(i):
        if i == n:
            path.append("".join(res))
            return
        dfs(i + 1)
        res.append(s[i])
        dfs(i + 1)
        res.pop()

    dfs(0)
    return path


if __name__ == "__main__":
    a = "abc"
    print_all_subsequences(a)
    print(all_subsequence(a))
