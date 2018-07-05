'''
created by tanxing in 2018/07/05
'''

import random, struct
from Config.Config import Config

'''
生产数据
@tag 数据TAG值
@type 数据类型
@digis 小数位数
@normalValueBase 正常数据基值
@abnormalValueBase 异常数据基值
@abnormal 数据异常控制标志
'''
def create_data(tag, type, digis, normalValueBase, abnormalValueBase, abnormal):
    data = [tag]
    code = type
    batch = '0'
    len2 = 0
    b = random.randint(2, 30)
    if (b < 6):  # 1/6概率发布多条数据
        batch = '1'
        len2 = b
    data.append(get_len1(code, batch, digis))
    data.append(len2)
    if (len2 == 0):
        len2 = 1
    valueLen = Config.FunctionCodeMap.get(code)
    for i in range(len2):
        base = normalValueBase
        if abnormal:
            base = abnormalValueBase
        scal = 1
        if(digis == 0):# 小数控制
            digi = 0
        elif(digis == 1):
            digi = random.randint(0, 9)
            scal = 10
        elif(digis == 2):
            digi = random.randint(10, 29)
            scal = 100
        elif(digis == 3):
            digi = random.randint(100, 299)
            scal = 1000
        elif(digis == 4):
            digi = random.randint(1000, 2990)
            scal = 10000
        else:
            #待定义
            pass
        data.extend(value_to_bytes(base*scal+digi, valueLen))
    return data

'''
获取TLV格式第一个长度值
@type 数据类型
@batch 批量传输位
@precision 精度位
'''
def get_len1(type, batch, precision):
    p = str(bin(precision))[2:][-3:]
    if (len(p) == 1):
        p = '00' + p
    elif (len(p) == 2):
        p = '0' + p
    bit = type + batch + p
    return int(bit, 2)

'''
数字转字节数组
@value 待转数值
@len 字节长度
'''
def value_to_bytes(value, len):
    values = []
    if(len > 7):
        values.append((value >> 56) & 0xFF)
        values.append((value >> 48) & 0xFF)
        values.append((value >> 40) & 0xFF)
        values.append((value >> 32) & 0xFF)
    if(len > 3):
        values.append((value >> 24) & 0xFF)
        values.append((value >> 16) & 0xFF)
    if(len > 1):
        values.append((value >> 8) & 0xFF)
    values.append(value & 0xFF)
    return values