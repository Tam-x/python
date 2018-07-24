from Config import Config

class TlvParser:
    def checkFrame(self, frame):
        data = frame[18:-3]
        return True, data

    def parse_tlv(self, data, offset):
        if(offset < len(data) - 4):
            channel = data[offset+1]&0xFF
            tag = data[offset+2]&0xFF
            type = data[offset+3]&0xFF
            vtype = self.get_value_type(type)
            vlen = self.get_value_length(type)
            precision = self.get_value_precision(type)
            values = []
            if vlen:
                for i in range(vlen):
                    values.append(data[offset+4+i])
                value = self.calc_value(vtype,precision,values)
                if channel > 0:
                    if Config.TASK_VALUE.get(channel):
                        val = Config.TASK_VALUE.get(channel)
                        val.update({tag: str(value)})
                        Config.TASK_VALUE.update({channel: val})
                    else:
                        Config.TASK_VALUE.update({channel: {tag: str(value)}})
                else:
                    if tag == 11 or tag == 12:
                        if value == 1:
                            Config.SYS_VALUE.update({tag: '正常'})
                        elif value == 0:
                            Config.SYS_VALUE.update({tag: '异常'})
                        else:
                            Config.SYS_VALUE.update({tag: '-'})
                    else:
                        Config.SYS_VALUE.update({tag: str(value)})
                self.parse_tlv(data, offset+4+vlen)

    def get_value_type(self, b):
        return (b & 0xF0) >> 4

    def get_value_length(self, b):
        vlen = self.get_value_type(b)
        if vlen == 0:   return 1
        elif vlen == 1: return 1
        elif vlen == 2: return 1
        elif vlen == 3: return 2
        elif vlen == 4: return 2
        elif vlen == 5: return 4
        elif vlen == 6: return 4
        elif vlen == 7: return 8
        elif vlen == 8: return 8
        elif vlen == 9: return 4
        elif vlen == 10: return 8

    def get_value_precision(self, b):
        return b &0x07

    def calc_value(self, type, precision, data):
        p = 1
        if precision == 2:
            p = 100
        elif precision == 3:
            p = 1000
        elif precision == 7:
            p = 10000000
        if type == 2:
            return self.byte_to_unsigned_char(data[0])
        elif type == 4:
            return self.byte_to_unsigned_short(data[0],data[1]) / p
        elif type == 6:
            return self.byte_to_unsigned_int(data[0],data[1],data[2],data[3]) / p


    def byte_to_unsigned_char(self, value):
        return value&0xff

    def byte_to_unsigned_short(self, value1, value2):
        return ((value1&0xff)<< 8) | (value2&0xff)

    def byte_to_unsigned_int(self, value1, value2, value3, value4):
        return ((value1&0xff)<< 24) | ((value2&0xff) << 16)|((value3&0xff<< 8)) | (value4&0xff)
