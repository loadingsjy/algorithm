# 大众对垃圾短信深恶痛绝，希望能对垃圾短信发送者进行识别，为此，很多软件增加了垃圾短信的识别机制。经分析，发现正常用
# 户的短信通常具备交互性，而垃圾短信往往都是大量单向的短信，按照如下规则进行垃圾短信识别:
# 本题中，发送者A符合以下条件之一的， 则认为A是垃圾短信发送者:
# 1: A发送短信的接收者中，没有发过短信给A的人数L> 5;
# 2: A发送的短信数 - A接收的短信数M> 10;
# 3: 如果存在X，A发送给X的短信数 - A接收到X的短信数N >5.
# 输入描述
# 第一行是条目数，接下来几行是具体的条目，每个条目，是一对D，第一人数字是发送者ID,后面的数字是接收者ID，中间空格隔
# 开，所有的ID都为无符号整型Q，ID最大值为100:
# 同一个条目中，两个ID不会相同(即不会自己给自己发消息)
# 最后一行为指定的ID
# 输出描述
# 输出该ID是否为垃圾短信发送者，并且按序列输出L M的值(由于N值不唯一，不需要输出)输出均为字符串。
# 示例1:
# 输入
# 15
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
# 1 11
# 1 12
# 1 13
# 1 14
# 14 1
# 1 15
# 输出
# true 13 13
# 说明
# true表示1是垃圾短信发送者，两个数字，代表发送者1对应的L和M值。true 13 13中间以一个空格分割。注意true是字符电输出

from collections import defaultdict


def construct_SendAndReceive_dict(records):
    send_dict = defaultdict(list)
    receive_dict = defaultdict(list)
    for sender, receiver in records:

        send_dict[sender].append(receiver)
        receive_dict[receiver].append(sender)

    return send_dict, receive_dict


def count_messages(send_dict, receive_dict, sender, receiver):
    """计算sender给receiver发了多少短信"""
    count = 0
    for p in receive_dict[receiver]:
        if p == sender:
            count += 1
    return count


def cal_index(records, id):
    send_dict, receive_dict = construct_SendAndReceive_dict(records)
    L = 0
    for p in send_dict[id]:
        if not send_dict[p]:
            L += 1
    M = len(send_dict[id]) - len(receive_dict[id])

    N = False
    for person in send_dict.keys():
        if (
            count_messages(send_dict, receive_dict, id, person)
            - count_messages(send_dict, receive_dict, person, id)
            > 5
        ):
            N = True
            break

    return L, M, N


if __name__ == "__main__":
    records = [
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7),
        (1, 8),
        (1, 9),
        (1, 10),
        (1, 11),
        (1, 12),
        (1, 13),
        (1, 14),
        (14, 1),
        (1, 15),
    ]
    id = 1
    L, M, N = cal_index(records, id)
    if L > 5 or M > 10 or N:
        print("True ", L, " ", M)
    
    
    id = 2
    L, M, N = cal_index(records, id)
    if L > 5 or M > 10 or N:
        print("true ", L, " ", M)
    else:
        print('false ',L, ' ', M)
