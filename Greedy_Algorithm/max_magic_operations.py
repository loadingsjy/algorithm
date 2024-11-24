
# 给一个包含n个整数元素的集合a，应该包含m个整数元素的集合b
# 定义magic操作为：从一个集合中取出一个元素，放到另一个集合中，且操作过后每个集合的平均值都大于操作前的平均值
# 注意一下两点：
# 1)不可以把一个集合的元素取空，这样就没有平均值了
# 2)值为x的元素从集合b取出放入集合a，但集合a中已经有值为x的元素了，则a的平均值不变（因为集合元素不会重复），b的平均值可能会改变（因为x被取出了）
# 问最多可以执行多少次magic操作？


# 请保证arr1中无重复值，arr2中无重复值，且arr1和arr2中肯定有数字
def max_magic_operations(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    sum1, sum2 = sum(arr1), sum(arr2)
    if sum1/n1 == sum2/n2:      # 集合元素平均值相等，无法进行magic操作
        return 0
    
    if sum1/n1 > sum2/n2:
        arrmore, arrless = arr1, arr2
        summore, sumless = sum1, sum2
    else:
        arrmore, arrless = arr2, arr1
        summore, sumless = sum2, sum1
        
    moreSize = len(arrmore)
    lessSize = len(arrless)
    
    arrmore.sort()
    
    opt = 0
    less_set = set(arrless)         # 小集合元素集合
    for i in range(moreSize):
        if (summore/moreSize > float(arrmore[i]) > sumless/lessSize) and (arrmore[i] not in less_set):
            summore -= arrmore[i]
            moreSize -= 1
            sumless += arrmore[i]
            lessSize += 1
            less_set.add(arrmore[i])
            opt += 1
    return opt

if __name__ == '__main__':
    arr1 = [1,3,4,5]
    arr2 = [5,6,7,8,9,10,18,20]
    print('avg1:                 ',sum(arr1)/len(arr1))
    print('avg2:                 ',sum(arr2)/len(arr2))
    print('max magic operations: ',max_magic_operations(arr1, arr2))
            
    