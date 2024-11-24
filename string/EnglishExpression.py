def num1To19(num):
    if num < 1 or num > 19:
        return ""
    names = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    return names[num - 1]


def num10To99(num):
    if num < 1 or num > 99:
        return ""
    if num < 20:
        return num1To19(num)
    tens = num // 10
    ones = num % 10
    
    tyNames = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    return tyNames[tens - 2] + " " + num1To19(ones)


def num1To999(num):
    if num < 1 or num > 999:
        return ""
    if num < 100:
        return num10To99(num)
    hundreds = num // 100
    rest = num % 100
    if hundreds == 0:
        return num10To99(rest)
    else:
        return num1To19(hundreds) + " Hundred " + num10To99(rest)
    
    
def english_expression(num):

    if num == 0:
        return "zero"
    if num < 0:
        return "minus " + english_expression(-num)
    if num < 1000:
        return num1To999(num)
    else:
        return english_expression(num // 1000) + " Thousand " + num1To999(num % 1000)
    
    
if __name__ == "__main__":
    print(english_expression(1234))
