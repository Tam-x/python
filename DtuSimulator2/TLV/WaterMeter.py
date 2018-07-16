'''
created by tanxing in 2018/07/12
'''

from TLV import TlvHelper, TlvData
from Config.Config import Config

'''
生产水表数据
'''
class WaterMeter:

    def create_water_meter_data(self):
        data = self.create_base_data()
        data.extend(self.create_core_data())
        data.extend(self.create_maintenance())
        return data

    '''
    设备基础数据
    '''
    def create_base_data(self):
        data = self.create_base_suppler()
        data.extend(self.create_base_meternum())
        # data.extend(self.create_base_sim())#数据长度字段定义 在哪个字段 本身数据类型是btyearray???
        # data.extend(self.create_base_imei())
        # data.extend(self.create_base_imsi())
        data.extend(self.create_base_operator())
        data.extend(self.create_base_protocal())
        data.extend(self.create_base_derection())
        data.extend(self.create_base_powersupply())
        data.extend(self.create_base_safevoltage())
        return data

    #设备供应商编号
    def create_base_suppler(self, suppler=0):
        return TlvHelper.create_data(101, '0100', 0, suppler, suppler, False)

    #水表设备ID
    def create_base_meternum(self, num=0):
        return TlvHelper.create_data(102, '0110', 0, num, num, False)

    def create_base_sim(self, sim = '13438879512'):
            return TlvHelper.create_bcd_data(104, 6, sim)

    #IMSI号
    def create_base_imsi(self, imsi='460001234567890'):
        return TlvHelper.create_bcd_data(105, 8, imsi)

    #IMEI
    def create_base_imei(self, imei='345001234567890'):
        return TlvHelper.create_bcd_data(106, 8, imei)

    #网络运营商
    def create_base_operator(self, abnormal=False):
        import random
        return TlvHelper.create_data(107, '0010', 0, random.randint(1, 3), 1, False)

    #水表通讯协议
    def create_base_protocal(self, abnormal=False):
        import random
        return TlvHelper.create_data(108, '0010', 0, random.randint(0, 3), 1, False)

    #水表安装方向
    def create_base_derection(self, abnormal=False):
        return TlvHelper.create_data(109, '0000', 0, 0, 1, False)

    #设备供电方式
    def create_base_powersupply(self, abnormal=False):
        import random
        return TlvHelper.create_data(110, '0010', 0, random.randint(0, 1), 1, False)

    #最低安全运行电压
    def create_base_safevoltage(self, abnormal=False):
        return TlvHelper.create_data(111, '0100', 2, 4, 1, False)

    '''
    设备动态核心数据
    '''
    def create_core_data(self, abnormal):
        data =[]
        # data.extend(self.create_core_collected_time())
        # data.extend(self.create_core_upload_time())
        data.extend(self.create_core_total_flows(abnormal))
        data.extend(self.create_core_forward_tflows(abnormal))
        data.extend(self.create_core_reverse_tflows(abnormal))
        data.extend(self.create_core_press(abnormal))
        return data

    def create_core_collected_time(self):
        return TlvHelper.create_date_data(112)

    def create_core_upload_time(self):
        return TlvHelper.create_date_data(113)

    def create_core_total_flows(self, abnormal=False):
        return TlvHelper.create_data(114, '0110', 3, 123456, 0, abnormal)

    #正向累计流量
    def create_core_forward_tflows(self, abnormal=False):
        return TlvHelper.create_data(115, '0110', 3, 123466, 0, abnormal)

    #倒转累计流量
    def create_core_reverse_tflows(self, abnormal=False):
        return TlvHelper.create_data(116, '0110', 3, 10, 0, abnormal)

    #压力值
    def create_core_press(self, abnormal=False):
        return TlvHelper.create_data(117, '0100', 3, 2, 100, abnormal)

    '''
    设备动态维护数据
    '''
    def create_maintenance(self, abnormal=False):
        data = self.create_maintenance_vlotage(abnormal)
        data.extend(self.create_maintenance_alarm())
        return data

    #实时电压
    def create_maintenance_vlotage(self, abnormal=False):
        return TlvHelper.create_data(118, '0100', 2, 5, 1000, abnormal)

    #设备运行告警
    def create_maintenance_alarm(self, abnormal=False):
        import random
        return TlvHelper.create_data(118, '0100', 0, random.randint(0,5), 0, False)

# import paho.mqtt.publish as publish
# Config.BROKER = '182.61.25.208'
# m = WaterMeter()
# print(m.create_maintenance_alarm())
# data = TlvData.TlvData.create_tlv_data(1,Config.MESSAGE_PUMP_HOUSE,506,m.create_base_data())
# print(data)
# publish.single("dtu/up/phouse/0.0.1.250/deivces", bytearray(TlvData.TlvData.create_tlv_data(1,Config.MESSAGE_PUMP_HOUSE,506,m.create_base_data())), hostname=Config.BROKER, auth = {'username':"<username>", 'password':"<password>"})