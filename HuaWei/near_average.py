import math


# 所有像素加上offset后的平均值
def after_offset_avg(arr, offset):
    n = len(arr)
    s = 0
    for num in arr:
        t = num + offset
        if t < 0:
            s += 0
        elif t > 255:
            s += 255
        else:
            s += t
    return s / n


# 计算多余的offset
def cal_over_offset(arr, offset):
    over_offset = 0
    count = 0
    if offset < 0:
        for num in arr:
            t = num + offset
            if t < 0:
                over_offset += t
                count += 1

        # # 将本身会成为负数的数变成的0以后平均值的增长分配到其他数上
        # return offset + (over_offset / (len(arr) - count))
    else:
        for num in arr:
            t = num + offset
            if t > 255:
                over_offset += t - 255
                count += 1
    return offset + (over_offset / (len(arr) - count))


def near_average(arr):
    n = len(arr)
    avg = sum(arr) / n
    last_offset = 128 - avg

    last_avg = after_offset_avg(arr, last_offset)

    while 1:
        new_offset = cal_over_offset(arr, last_offset)
        new_avg = after_offset_avg(arr, new_offset)
        if abs(new_avg - 128) < abs(last_avg - 128):
            last_offset = new_offset
            last_avg = new_avg
            # print(last_offset, last_avg) 
            continue
        else:
            break

    floor_offset = int(last_offset)
    ceil_offset = floor_offset + 1

    if abs(after_offset_avg(arr, floor_offset) - 128) <= abs(after_offset_avg(arr, ceil_offset) - 128):
        return floor_offset
    else:
        return ceil_offset


def new_array(arr, offset):
    res = []
    for num in arr:
        t = num + offset
        if t < 0:
            res.append(0)
        elif t > 255:
            res.append(255)
        else:
            res.append(t)
    return res


def getCount(nums, offset):
    count = 0
    for num in nums:
        temp = num + offset
        if (temp < 0 or temp > 255):
            count+=1
    return count


# 官方解答
def fix0ffset(nums, offset, count):
    if (count == 0):
        return offset
    offsetOld = offset
    for num in nums :
        temp = num + offsetOld
        if (temp < 0):
            offset += temp / (len(nums) - count)
        elif (temp > 255):
            offset += (temp -255) / (len(nums) - count)
    return fix0ffset(nums, offset, getCount(nums, offset) - count)



if __name__ == "__main__":
    arr = [230, 167, 138, 12, 245, 9, 235, 198]
    offset = near_average(arr)
    print("final offset: ", offset)
    new_arr = new_array(arr, offset)
    print("new array: ", new_arr, sum(new_arr)/len(new_arr))
    print('after offset avg: ',after_offset_avg(arr, offset))
    print()

    
    offset = 128 - sum(arr)/len(arr)
    offset = fix0ffset(arr,offset,getCount(arr,offset))
    if abs(after_offset_avg(arr, int(offset)) - 128) <= abs(after_offset_avg(arr, int(offset)+1) - 128):
        offset =  int(offset)
    else:
        offset = int(offset) + 1
        
        
    print("final offset: ", offset)
    new_arr = new_array(arr, offset)
    print("new array: ", new_arr, sum(new_arr)/len(new_arr))
    print('after offset avg: ',after_offset_avg(arr, offset))
    print()
    

    
    
    arr = [34, 38, 21, 2, 8, 198, 234]
    offset = near_average(arr)
    print("final offset: ", offset)
    new_arr = new_array(arr, offset)
    print("new array: ", new_arr, sum(new_arr)/len(new_arr))
    print('after offset avg: ',after_offset_avg(arr, offset))
    print()


    offset = 128 - sum(arr)/len(arr)
    offset = fix0ffset(arr,offset,getCount(arr,offset))
    if abs(after_offset_avg(arr, int(offset)) - 128) <= abs(after_offset_avg(arr, int(offset)+1) - 128):
        offset =  int(offset)
    else:
        offset = int(offset) + 1
        
        
    print("final offset: ", offset)
    new_arr = new_array(arr, offset)
    print("new array: ", new_arr, sum(new_arr)/len(new_arr))
    print('after offset avg: ',after_offset_avg(arr, offset))
    print()
