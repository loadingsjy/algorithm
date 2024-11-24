from functools import lru_cache


# 2元, 3元, 5元的零钱凑成总金额的方案数
@lru_cache()
def change_money(total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total - 2) + change_money(total - 3) + change_money(total - 5)


if __name__ == '__main__':
    print(change_money(25))
