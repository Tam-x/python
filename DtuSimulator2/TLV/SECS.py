'''
created by tanxing in 2018/07/12
'''

from TLV import TlvHelper
from Config.Config import Config

'''
生产热能数据
'''
class Secs:
    '''
        生产热能数据
    '''
    def create_secs_data(self, list, abnormal):
        data =[]
        for value in list:
            if value == Config.SECS_OBJECTS[0]:
                data.extend(self.create_env_data(abnormal))
            elif value == Config.SECS_OBJECTS[1]:
                data.extend(self.create_emeter_data(abnormal))
            elif value == Config.SECS_OBJECTS[2]:
                data.extend(self.create_v_temp(abnormal))
        return data

    '''
    设备/环境数据
    '''
    def create_env_data(self, abnormal=False):
        data = self.create_env_intemp(abnormal)
        data.extend(self.create_env_outtemp(abnormal))
        data.extend(self.create_env_inpress(abnormal))
        data.extend(self.create_env_outpress(abnormal))
        data.extend(self.create_env_inflow(abnormal))
        data.extend(self.create_env_outflow(abnormal))
        data.extend(self.create_env_saveheat(abnormal))
        data.extend(self.create_env_loseheat(abnormal))
        data.extend(self.create_env_house_intemp(abnormal))
        data.extend(self.create_env_house_outtemp(abnormal))
        return data

    #进水管温度
    def create_env_intemp(self, abnormal=False):
        return TlvHelper.create_data(11, '0100', 1, 30, 150, abnormal)

    #出水管温度
    def create_env_outtemp(self, abnormal=False):
        return TlvHelper.create_data(12, '0100', 1, 30, 150, abnormal)

    #进水管压力
    def create_env_inpress(self, abnormal=False):
        return TlvHelper.create_data(13, '0100', 1, 2, 200, abnormal)

    #进水管压力
    def create_env_outpress(self, abnormal=False):
        return TlvHelper.create_data(14, '0100', 1, 2, 200, abnormal)

    #进水管流速
    def create_env_inflow(self, abnormal=False):
        return TlvHelper.create_data(15, '0110', 1, 5, 500, abnormal)

    #出水管流速
    def create_env_outflow(self, abnormal=False):
        return TlvHelper.create_data(16, '0110', 1, 5, 500, abnormal)

    #储热量
    def create_env_saveheat(self, abnormal=False):
        return TlvHelper.create_data(17, '0110', 2, 1000, 0, abnormal)

    #放热量
    def create_env_loseheat(self, abnormal=False):
        return TlvHelper.create_data(18, '0110', 2, 800, 0, abnormal)

    # 室内温度
    def create_env_house_intemp(self, abnormal=False):
        return TlvHelper.create_data(19, '0100', 1, 25, 100, abnormal)

    # 室外温度
    def create_env_house_outtemp(self, abnormal=False):
        return TlvHelper.create_data(20, '0100', 1, 20, 100, abnormal)

    '''
    电表数据
    '''
    def create_emeter_data(self, abnormal=False):
        data = self.create_emeter_avoltage(abnormal)
        data.extend(self.create_emeter_bvoltage(abnormal))
        data.extend(self.create_emeter_cvoltage(abnormal))
        data.extend(self.create_emeter_acurrent(abnormal))
        data.extend(self.create_emeter_bcurrent(abnormal))
        data.extend(self.create_emeter_ccurrent(abnormal))
        data.extend(self.create_emeter_hz(abnormal))
        data.extend(self.create_emeter_apower(abnormal))
        data.extend(self.create_emeter_bpower(abnormal))
        data.extend(self.create_emeter_cpower(abnormal))
        data.extend(self.create_emeter_powers(abnormal))
        data.extend(self.create_emeter_reapower(abnormal))
        data.extend(self.create_emeter_rebpower(abnormal))
        data.extend(self.create_emeter_recpower(abnormal))
        data.extend(self.create_emeter_repowers(abnormal))
        data.extend(self.create_emeter_afactor(abnormal))
        data.extend(self.create_emeter_bfactor(abnormal))
        data.extend(self.create_emeter_cfactor(abnormal))
        data.extend(self.create_emeter_factors(abnormal))
        data.extend(self.create_emeter_elctrics(abnormal))
        data.extend(self.create_emeter_jianelctric(abnormal))
        data.extend(self.create_emeter_fengelctric(abnormal))
        data.extend(self.create_emeter_pingelctric(abnormal))
        data.extend(self.create_emeter_guelctric(abnormal))
        return data

    #A相电压
    def create_emeter_avoltage(self, abnormal=False):
        return TlvHelper.create_data(21, '0100', 2, 220, 1000, abnormal)

    #B相电压
    def create_emeter_bvoltage(self, abnormal=False):
        return TlvHelper.create_data(22, '0100', 2, 220, 1000, abnormal)

    #C相电压
    def create_emeter_cvoltage(self, abnormal=False):
        return TlvHelper.create_data(23, '0100', 2, 220, 1000, abnormal)

    #A相电流
    def create_emeter_acurrent(self, abnormal=False):
        return TlvHelper.create_data(24, '0110', 2, 2, 1000, abnormal)

    #B相电流
    def create_emeter_bcurrent(self, abnormal=False):
        return TlvHelper.create_data(25, '0110', 2, 2, 1000, abnormal)

    #C相电流
    def create_emeter_ccurrent(self, abnormal=False):
        return TlvHelper.create_data(26, '0110', 2, 2, 1000, abnormal)

    #频率
    def create_emeter_hz(self, abnormal=False):
        return TlvHelper.create_data(27, '0100', 2, 50, 5000, abnormal)

    #A相有功功率
    def create_emeter_apower(self, abnormal=False):
        return TlvHelper.create_data(28, '0101', 2, 5000, 0, abnormal)

    #B相有功功率
    def create_emeter_bpower(self, abnormal=False):
        return TlvHelper.create_data(29, '0101', 2, 5000, 0, abnormal)

    #C相有功功率
    def create_emeter_cpower(self, abnormal=False):
        return TlvHelper.create_data(30, '0101', 2, 5000, 0, abnormal)

    # 总有功功率
    def create_emeter_powers(self, abnormal=False):
        return TlvHelper.create_data(31, '0101', 2, 15000, 0, abnormal)

    # A相无功功率
    def create_emeter_reapower(self, abnormal=False):
        return TlvHelper.create_data(32, '0101', 2, 5000, 0, abnormal)

    # B相无功功率
    def create_emeter_rebpower(self, abnormal=False):
        return TlvHelper.create_data(33, '0101', 2, 5000, 0, abnormal)

    # C相无功功率
    def create_emeter_recpower(self, abnormal=False):
        return TlvHelper.create_data(34, '0101', 2, 5000, 0, abnormal)

    # 总无功功率
    def create_emeter_repowers(self, abnormal=False):
        return TlvHelper.create_data(35, '0101', 2, 15000, 0, abnormal)

    # A相功率因数
    def create_emeter_afactor(self, abnormal=False):
        return TlvHelper.create_data(36, '0011', 3, 1, 10000, abnormal)

    # B相功率因数
    def create_emeter_bfactor(self, abnormal=False):
        return TlvHelper.create_data(37, '0011', 3, 1, 10000, abnormal)

    # C相功率因数
    def create_emeter_cfactor(self, abnormal=False):
        return TlvHelper.create_data(38, '0011', 3, 1, 10000, abnormal)

    # 总功率因数
    def create_emeter_factors(self, abnormal=False):
        return TlvHelper.create_data(39, '0011', 3, 3, 30000, abnormal)

    # 总电量
    def create_emeter_elctrics(self, abnormal=False):
        return TlvHelper.create_data(40, '0110', 1, 40000, 0, abnormal)

    # 尖电量
    def create_emeter_jianelctric(self, abnormal=False):
        return TlvHelper.create_data(41, '0110', 1, 10000, 0, abnormal)

    # 峰电量
    def create_emeter_fengelctric(self, abnormal=False):
        return TlvHelper.create_data(42, '0110', 1, 10000, 0, abnormal)

    # 平电量
    def create_emeter_pingelctric(self, abnormal=False):
        return TlvHelper.create_data(43, '0110', 1, 10000, 0, abnormal)

    # 谷电量
    def create_emeter_guelctric(self, abnormal=False):
        return TlvHelper.create_data(44, '0110', 1, 10000, 0, abnormal)

    '''相变温度'''
    def create_v_temp(self, abnormal):
        data = []
        for i in range(51, 131):
            data.extend(TlvHelper.create_data(i, '0100', 1, 27, 1000, abnormal))
        return data