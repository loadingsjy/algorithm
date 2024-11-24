
# pos是当前的位置
# pos之前的数字转化的结果已经计算出来了
# 计算pos之后有多少转化的结果
def process(str, pos):
    if pos == len(str):
        return 1
    if str[pos] == '0':
        return 0
    if str[pos] == '1':
        result = process(str, pos+1)
        if pos+1<len(str):
            result += process(str, pos+2)
        return result
    elif str[pos] == '2':
        result = process(str, pos+1)
        if pos+1<len(str) and str[pos+1] >= '0' and str[pos+1] <= '6':
            result += process(str, pos+2)
        return result
    return process(str, pos+1)


def num2char(num):
    num_str = str(num)
    num_list = list(num_str)
    result = process(num_str, 0)
    return result


if __name__ == '__main__':
    print(num2char(1253523))
    print(num2char(2523))
    print(num2char(112210201))