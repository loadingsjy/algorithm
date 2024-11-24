# 一、题目描述：
# 小王在进行游戏大闯关，有一个关卡需要输入一个密码才能通过。密码获得的条件如下：
# 在一个密码本中，每一页都有一个由26个小写字母组成的若干位密码，每一页的密码不同，需要从这个密码本中寻找这样一个最长的密码，
# 从它的末尾开始依次去掉一位得到的新密码也在密码本中存在。
# 请输出符合该要求的密码，如果有多个符合要求的密码，则返回字典序最大的密码。若没有符合要求的密码，则返回空字符串。

# 输入描述：
# 密码本由一个字符串数组组成，不同元素之间使用空格隔开，每一个元素代表密码本每一页的密码
# 输出描述：
# 一个字符串

# 示例1
# 输入
# h he hel hell hello
# 输出
# hello
# 说明:
# ＂hello＂从末尾依次去掉一位得到的"hell"，"hel"，"he"和"h"在密码本中都存在。
# 示例2
# 输入
# eredderd bw bww bwwl bwwlm bwwln
# 输出
# bwwln
# 说明:
# ＂bwwlm＂和＂bwwln＂从末尾开始依次去掉一位得到密码在密码本中都存在。但是＂bwwln＂比＂bwwlm＂字典序排序大，所以应该返回＂bwwln＂



def get_mima(str_list):
    '''思路：
    将所有字符串按照长度排序，依次遍历，如果长度为最短长度，则直接加入答案，
    如果长度大于最短长度，则去掉他最后一个字符的子串在答案中，则他自己也在答案中，并更新最大长度
    '''
    substring_set = set()
    str_list.sort(key=lambda x : len(x))
    min_len = len(str_list[0])
    max_len = min_len
    
    for s in str_list:
        length = len(s)
        if length == min_len:
            substring_set.add(s)
        else:
            if s[:-1] in substring_set:
                substring_set.add(s)
                if length > max_len:
                    max_len = length
    # print(substring_set)
                    
    ans = []             
    for s in substring_set:
        if len(s) == max_len:
            ans.append(s)
    ans.sort()
    # print(ans)
    return ans[-1]
            
        
           
if __name__ == '__main__':
    input_str = 'h he hel hell hello'
    str_list =  list(input_str.split())
    print(get_mima(str_list))
    
    
    input_str = 'h he hel hell hello k ka kas kasf kasfd helld'
    str_list =  list(input_str.split())
    print(get_mima(str_list))

    
    input_str = 'eredderd bw bww bwwl bwwlm bwwln'
    str_list =  list(input_str.split())
    print(get_mima(str_list))