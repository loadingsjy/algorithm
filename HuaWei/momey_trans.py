trans = {"CNY": 100, "JPY": 1825, "HKD": 123, "EUR": 14, "GBP": 12}


YuanToFen = {
    "fen": "CNY",
    "cents": "HKD",
    "sen": "JPY",
    "eurocents": "EUR",
    "pence": "GBP",
}


def momey_transform(s):

    nums1 = []
    string1 = []
    nums2 = []
    string2 = []

    i = len(s) - 1
    flag = False

    while i >= 0:
        if s[i].islower():
            string2.insert(0, s[i])
            i -= 1
            flag = True
        elif s[i].isdigit() and flag:
            nums2.insert(0, s[i])
            i -= 1
        elif s[i].isupper():
            string1.insert(0, s[i])
            i -= 1
            flag = False
        elif s[i].isdigit() and not flag:
            nums1.insert(0, s[i])
            i -= 1

    n1 = "".join(nums1)
    s1 = "".join(string1)

    n2 = "".join(nums2)
    s2 = "".join(string2)
    # print(n1,s1,n2,s2)

    res = 0.0
    if s1:
        res += trans["CNY"] / trans[s1] * float(n1)
    if s2:
        res += trans["CNY"] / trans[YuanToFen[s2]] * float(n2)

    return int(res)


if __name__ == "__main__":

    s = "3000fen"
    print(momey_transform(s))
    s = "123HKD"
    print(momey_transform(s))
    s = "20CNY53fen"
    print(momey_transform(s))
    s = "53HKD87cents"
    print(momey_transform(s))
