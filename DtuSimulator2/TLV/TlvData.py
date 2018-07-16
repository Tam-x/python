'''
created by tanxing in 2018/07/06
'''

from TLV.PumpHouse import PumpHouse
from TLV.CRC8 import crc8
from TLV.TlvHelper import *
'''
生产消息帧
'''

HEAD = [170, 254]
VERSION = 2
LEN = [] # 2bytes
PROJECT_PUMP = 33 # 0010_0001
PROJECT_METER = 34 # 0010_0010
USER = 0
IP = [] # 4bytes
CODE = 1
TIME = [] # 6bytes
MESSAGE = []
TAIL = [221, 238]



class TlvData:
    def create_tlv_data(self, type, ip, message):
        data = []
        MESSAGE = message
        length = len(MESSAGE)+18+3
        LEN = value_to_bytes(length, 2)
        IP = value_to_bytes(ip, 4)
        TIME = time_to_bytes()
        data.extend(HEAD)
        data.append(VERSION)
        data.extend(LEN)
        if (type == Config.MESSAGE_PUMP_HOUSE):
            data.append(PROJECT_PUMP)
        else:
            data.append(PROJECT_METER)
        data.append(USER)
        data.extend(IP)
        data.append(CODE)
        data.extend(TIME)
        data.extend(MESSAGE)
        crc = crc8()
        crc.update(bytearray(data))
        data.append(int(crc.hexdigest(),16))
        data.extend(TAIL)
        return data


# m = TlvData()
# m.create_tlv_data(Config.MESSAGE_PUMP_HOUSE, 506)