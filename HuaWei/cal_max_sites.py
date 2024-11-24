


def dfs(mat, n, site_set):
    '''从n站点出发找到所有的站点site_set'''
    for i in range(len(mat)):
        if i in site_set:
            continue
        if n != i and mat[n][i] == 1:
            site_set.add(i)
            dfs(mat, i, site_set)


def cal_max_sites(mat, n):
    res = 0
    site_set = set()
    for i in range(n):
        if i in site_set:
            continue
        temp = set()
        dfs(mat, i, temp)
        site_set |= temp
        res = max(res, len(temp))
    return res
        
        
if __name__ == '__main__':
    n = 4
    mat = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    print(cal_max_sites(mat, n))
    
