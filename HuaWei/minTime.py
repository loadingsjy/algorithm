# 现在有n个容器服务，服务的启动可能有一定的依赖性(有些服务启动没有依赖)，其次服务自身启动加载会消耗些时间。
# 给你一个nxn的二维矩阵useTime,其中useTime=10表示服务i自身启动加载需要消耗10s，use Timeli[]=1表示服务i启动依赖服
# 务i启动完成，useTimei[k]=0, 表示服务i启动不依赖服务k其实0<=ij, k<n。服务之间启动没有循环依赖(不会出现环)，若想对任
# 意一个服务进行集成测试(服务追身也需要加载)，求最少需要等待多少时间。
# 输入描述
# 第一行输入服务总量n.
# 之后的n行表示服务启动的依赖关系以及自身启动加载耗时
# 最后输入k表示计算需要等待多少时间后可以对服务k进行集成测试
# 其中1 <=k<=n.1<=n<=100
# 输出描述
# 最少需要等待多少时间(s)后可以对服务k进行集成测试
# 示例1
# 输入:
# 3
# 5 0 0
# 1 5 0
# 0 1 5
# 输出:
# 15

from collections import defaultdict


class info(object):
    def __init__(self):
        self.indgree = 0
        self.next_nodes = []


def update_node_info(idx, nodes_dict):
    for to in nodes_dict[idx].next_nodes:
        nodes_dict[to].indgree -= 1
    nodes_dict[idx].next_nodes = []
    return nodes_dict


def construct_nodes_dict(mat):
    n = len(mat)
    nodes_dict = defaultdict(info)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 and i != j:
                nodes_dict[j].next_nodes.append(i)
                nodes_dict[i].indgree += 1
    return nodes_dict


def minTime(mat, target):
    visited = []
    nodes_dict = defaultdict(info)
    total_time = 0
    nodes_dict = construct_nodes_dict(mat)

    while True:
        last_visited_len = len(visited)
        for idx, node_info in nodes_dict.items():
            if node_info.indgree == 0 and idx not in visited:
                visited.append(idx)
                total_time += mat[idx][idx]
                if idx == target:
                    return total_time
                nodes_dict = update_node_info(idx, nodes_dict)
                break
        if last_visited_len == len(visited):
            return -1  # 图中有环，或者target不存在或者不在连通分支里
    # if visited[-1] != target:
    #     return -1


if __name__ == "__main__":
    # n = 3
    # target = 3
    # mat = [[5, 0, 0], [1, 5, 0], [0, 1, 5]]
    # print(minTime(mat, target - 1))

    n = 3
    target = 3
    mat = [[5, 0, 0, 0], 
           [1, 5, 0, 1], 
           [0, 1, 5, 0], 
           [0, 1, 0, 5]]
    print(minTime(mat, target - 1))
