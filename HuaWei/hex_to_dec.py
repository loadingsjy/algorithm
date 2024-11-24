# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。1<=n<=2^31-1。
import sys


def hex_to_dec(s):
    alpha_map  = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    if s[:2] == '0x' or s[:2] == '0X' or s[:2] == 'Ox' or s[:2] == 'OX':
        s = s[2:]
    
    length = len(s)
    
    res = 0
    for i in range(length - 1, -1, -1):
        if s[i] not in alpha_map:
            res += (int(s[i])) * (16 ** (length - i - 1))
        else:
            res += alpha_map[s[i]] * (16 ** (length - i - 1))
    return res



if __name__ == '__main__':

    for line in sys.stdin:
        if not line.strip():
            break
        a = str(line.strip())
    
    res = hex_to_dec(str(a))
    sys.stdout.write(str(res) + '\n')


