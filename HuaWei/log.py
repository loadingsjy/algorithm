# 题目描述
# 日志采集是运维系统的的核心组件。日志是按行生成，每行记做一条，由采集系统分批上报。
# 如果上报太频繁，会对服务端造成压力;如果上报太晚，会降低用户的体验，如果一次上报的条数太多，会导致超时失败。为此，项目
# 组设计了如下的上报策略:
# 1、 每成功上报一条日志，奖励1分
# 2、每条日志每延迟上报1秒，扣1分
# 3、积累日志达到100条，必须立即上报
# 给出日志序列，根据该规则，计算首次上报能获得的最多积分数
# 输入描述:
# 按时序产生的日志条数T1.2...n,.其中1<=n<=1000, 0<=Ti<=100
# 输出描述:
# 首次上报最多能获得的积分数
# 示例1输入输出示例仅供调试，后台判题数据般不包含示例
# 1 98 1
# 输出
# 98
# 说明:
# T1时刻上报得1分
# T2时刻上报得98分，最大
# T3时刻上报得0分
# 示例2输入输出示例仅供调试，后台判题数据一般不包含示例
# 输入
# 3 7 40 10 60
# 输出
# 37
# 说明:
# T1时刻上报得3分
# T2时刻上报得7分
# T3时刻上报得37分，最大
# T4时刻上报得-3分
# T5时刻上报，因为已经超了100条的限制，所以只能上报100条，得-23分


def cal_pre_sum(arr):
    '''计算前缀和'''
    n = len(arr)
    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + arr[i - 1]
    return pre_sum


def cal_max_score(logs):
    max_score = 0
    pre_sum = cal_pre_sum(logs)
    pre_sum_pre_sum = cal_pre_sum(pre_sum)
    
    for i in range(len(pre_sum)):
        max_score = max(max_score, pre_sum[i]-pre_sum_pre_sum[i])
        if pre_sum[i] >= 100:
            break
    return max_score

if __name__ == "__main__":
    logs = [3,7,40,10,60]
    print(cal_max_score(logs))
    
    logs = [2,17,4,42,18,23,10]
    print(cal_max_score(logs))
