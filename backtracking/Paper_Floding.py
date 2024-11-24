

def paper_folding(n):
    printProcess(1, n, True)


def printProcess(i, n, down):
    if i > n:
        return
    printProcess(i + 1, n, True)
    if down:
        print("凹折痕")
    else:
        print("凸折痕")
    printProcess(i + 1, n, False)


if __name__ == "__main__":
    paper_folding(5)
