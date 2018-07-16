'''
created by tanxing in 2018/07/05
'''

from TLV import TlvHelper
from Config.Config import Config

'''
生产泵房数据
'''
class PumpHouse:
    '''
        生产泵房数据
    '''
    def create_pumphouse_data(self):
        data = self.creat_pump_data()
        data.extend(self.create_waterpool_data())
        data.extend(self.create_enveriment_data())
        data.extend(self.create_electric_data())
        data.extend(self.create_waterpooladd_data())
        return data

    def create_pumphouse_data(self, list, abnormal):
        data = []
        for value in list:
            if value == Config.WMETER_OBJECTS[0]:
                data = self.creat_pump_data(abnormal)
            elif value == Config.WMETER_OBJECTS[1]:
                data.extend(self.create_waterpool_data(abnormal))
            elif value == Config.WMETER_OBJECTS[2]:
                data.extend(self.create_enveriment_data(abnormal))
            elif value == Config.WMETER_OBJECTS[3]:
                data.extend(self.create_electric_data(abnormal))
            elif value == Config.WMETER_OBJECTS[4]:
                data.extend(self.create_watermeter_data(abnormal))
            elif value == Config.WMETER_OBJECTS[5]:
                data.extend(self.create_pumpplc_data(abnormal))
            elif value == Config.WMETER_OBJECTS[6]:
                data.extend(self.create_waterpooladd_data(abnormal))
        return data

    '''
    生产泵数据
    @abnormal 异常控制标志
    '''
    def creat_pump_data(self, abnormal=False):
        data = self.create_pump_temp(abnormal)
        data.extend(self.create_pump_amplitude(abnormal))
        return data

    #泵表面温度，tag#58
    def create_pump_temp(self, abnormal=False):
        return TlvHelper.create_data(58, '0100', 2, 25, 70, abnormal)

    #泵表振幅，tag#59
    def create_pump_amplitude(self, abnormal=False):
        return TlvHelper.create_data(59, '0100', 2, 2, 20, abnormal)

    '''
    生产蓄水池数据
    @abnormal 异常控制标志
    '''
    def create_waterpool_data(self, abnormal):
        data = self.create_waterpool_ph(abnormal)
        data.extend(self.create_waterpool_turbidity(abnormal))
        data.extend(self.create_waterpool_chlorine(abnormal))
        data.extend(self.create_waterpool_waterlevel(abnormal))
        data.extend(self.create_waterpool_inpress(abnormal))
        data.extend(self.create_waterpool_outpress(abnormal))
        data.extend(self.create_waterpool_flow(abnormal))
        data.extend(self.create_waterpool_flows(abnormal))
        return data

    #PH值，tag#23
    def create_waterpool_ph(self, abnormal=False):
        return TlvHelper.create_data(23, '0100', 2, 7, 4, abnormal)

    #浊度，tag#24
    def create_waterpool_turbidity(self, abnormal=False):
        return TlvHelper.create_data(24, '0100', 3, 0, 10, abnormal)

    #余氯，tag#25
    def create_waterpool_chlorine(self, abnormal=False):
        return TlvHelper.create_data(25, '0100', 3, 0, 6, abnormal)

    #水位高度，tag#26
    def create_waterpool_waterlevel(self, abnormal=False):
        return TlvHelper.create_data(26, '0100', 2, 2, 0, abnormal)

    #蓄水池进水口压力，tag#27
    def create_waterpool_inpress(self, abnormal=False):
        return TlvHelper.create_data(27, '0100', 3, 1, 10, abnormal)

    #蓄水池出水口压力，tag#28
    def create_waterpool_outpress(self, abnormal=False):
        return TlvHelper.create_data(28, '0100', 3, 1, 10, abnormal)

    #管路流速，tag#29
    def create_waterpool_flow(self, abnormal=False):
        return TlvHelper.create_data(29, '0110', 3, 3, 30, abnormal)

    #管路累计流量，tag#30
    def create_waterpool_flows(self, abnormal=False):
        return TlvHelper.create_data(30, '0110', 3, 30, 0, abnormal)

    '''
    生产泵房环境数据
    TAG:31-36
    '''
    def create_enveriment_data(self, abnormal):
        data = self.create_env_temp(abnormal)
        data.extend(self.create_env_humi(abnormal))
        data.extend(self.create_env_noise(abnormal))
        data.extend(self.create_env_somke(abnormal))
        data.extend(self.create_env_ponding(abnormal))
        data.extend(self.create_env_door(abnormal))
        return data

    #环境温度，tag#31
    def create_env_temp(self, abnormal=False):
        return TlvHelper.create_data(31, '0011', 2, 20, 60, abnormal)

    #环境湿度，tag#32
    def create_env_humi(self, abnormal=False):
        return TlvHelper.create_data(32, '0100', 2, 60, 1, abnormal)

    #环境噪音，tag#33
    def create_env_noise(self, abnormal=False):
        return TlvHelper.create_data(33, '0100', 2, 60, 600, abnormal)

    #环境烟火感应，tag#34
    def create_env_somke(self, abnormal=False):
        return TlvHelper.create_data(34, '0010', 0, 0, 1, abnormal)

    #环境积水感应，tag#35
    def create_env_ponding(self, abnormal=False):
        return TlvHelper.create_data(35, '0010', 0, 0, 1, abnormal)

    #环境门禁感应，tag#36
    def create_env_door(self, abnormal=False):
        return TlvHelper.create_data(36, '0010', 0, 0, 1, abnormal)

    '''
    生产电表基础数据
    TAG:37-50
    '''
    def create_electric_data(self, abnormal):
        data = self.create_elc_avoltage(abnormal)
        data.extend(self.create_elc_bvoltage(abnormal))
        data.extend(self.create_elc_cvoltage(abnormal))
        data.extend(self.create_elc_acurrent(abnormal))
        data.extend(self.create_elc_bcurrent(abnormal))
        data.extend(self.create_elc_ccurrent(abnormal))
        data.extend(self.create_elc_ct(abnormal))
        data.extend(self.create_elc_pt(abnormal))
        data.extend(self.create_elc_hz(abnormal))
        data.extend(self.create_elc_powers(abnormal))
        data.extend(self.create_elc_repowers(abnormal))
        data.extend(self.create_elc_factors(abnormal))
        data.extend(self.create_elc_degrees(abnormal))
        data.extend(self.create_elc_redegrees(abnormal))
        return data

    #A相电压，tag#37
    def create_elc_avoltage(self, abnormal=False):
        return TlvHelper.create_data(37, '0100', 2, 220, 500, abnormal)

    #B相电压，tag#38
    def create_elc_bvoltage(self, abnormal=False):
        return TlvHelper.create_data(38, '0100', 2, 220, 500, abnormal)

    #C相电压，tag#39
    def create_elc_cvoltage(self, abnormal=False):
        return TlvHelper.create_data(39, '0100', 2, 220, 500, abnormal)

    #A相电流，tag#40
    def create_elc_acurrent(self, abnormal=False):
        return TlvHelper.create_data(40, '0100', 3, 3, 30, abnormal)

    #B相电流，tag#41
    def create_elc_bcurrent(self, abnormal=False):
        return TlvHelper.create_data(41, '0100', 3, 3, 30, abnormal)

    #C相电流，tag#42
    def create_elc_ccurrent(self, abnormal=False):
        return TlvHelper.create_data(42, '0100', 3, 3, 30, abnormal)

    #CT，tag#43
    def create_elc_ct(self, abnormal=False):
        return TlvHelper.create_data(43, '0100', 0, 50, 50, abnormal)

    #PT，tag#44
    def create_elc_pt(self, abnormal=False):
        return TlvHelper.create_data(44, '0100', 0, 10, 10, abnormal)

    #频率，tag#45
    def create_elc_hz(self, abnormal=False):
        return TlvHelper.create_data(45, '0100', 2, 50, 500, abnormal)

    #总有功功率，tag#46
    def create_elc_powers(self, abnormal=False):
        return TlvHelper.create_data(46, '0101', 2, 1000, 0, abnormal)

    #总无功功率，tag#47
    def create_elc_repowers(self, abnormal=False):
        return TlvHelper.create_data(47, '0101', 2, 5000, 0, abnormal)

    #功率因素总和，tag#48
    def create_elc_factors(self, abnormal=False):
        return TlvHelper.create_data(48, '0011', 3, 1, 1, abnormal)

    #有功电度总和，tag#49
    def create_elc_degrees(self, abnormal=False):
        return TlvHelper.create_data(49, '0110', 2, 92040, 0, abnormal)

    #无功电度总和，tag#50
    def create_elc_redegrees(self, abnormal=False):
        return TlvHelper.create_data(50, '0110', 2, 17209, 0, abnormal)

    '''
    生产水表基础数据TAG(51-52)
    '''
    def create_watermeter_data(self, abnormal):
        data = self.create_watermeter_flow(abnormal)
        data.extend(self.create_watermeter_press(abnormal))
        return data

    #水表流量读数，tag#51
    def create_watermeter_flow(self, abnormal=False):
        return TlvHelper.create_data(51, '0110', 3, 11209, 0, abnormal)

    #水表压力，tag#52
    def create_watermeter_press(self, abnormal=False):
        return TlvHelper.create_data(52, '0100', 3, 2, 0, abnormal)

    '''生产泵PLC采集数据 TAG(53-75)'''
    def create_pumpplc_data(self, abnormal):
        data = self.create_pumpplc_status(abnormal)
        data.extend(self.create_pumpplc_ua(abnormal))
        data.extend(self.create_pumpplc_la(abnormal))
        data.extend(self.create_pumpplc_powers(abnormal))
        data.extend(self.create_pumpplc_hz(abnormal))
        data.extend(self.create_pumpplc_temp(abnormal))
        data.extend(self.create_pumpplc_amplitude(abnormal))
        data.extend(self.create_pumpplc_runtime(abnormal))
        data.extend(self.create_pumpplc_flow(abnormal))
        data.extend(self.create_pumpplc_flows(abnormal))
        data.extend(self.create_pumpplc_inpress(abnormal))
        data.extend(self.create_pumpplc_outpress(abnormal))
        data.extend(self.create_pumpplc_broken(abnormal))
        data.extend(self.create_pumpplc_sethz(abnormal))
        data.extend(self.create_pumpplc_setpress(abnormal))
        data.extend(self.create_pumpplc_ub(abnormal))
        data.extend(self.create_pumpplc_uc(abnormal))
        data.extend(self.create_pumpplc_ib(abnormal))
        data.extend(self.create_pumpplc_ic(abnormal))
        data.extend(self.create_pumpplc_repowers(abnormal))
        data.extend(self.create_pumpplc_epowers(abnormal))
        data.extend(self.create_pumpplc_erepowers(abnormal))
        data.extend(self.create_pumpplc_factors(abnormal))
        return data

    #泵运行状态，tag#53
    def create_pumpplc_status(self, abnormal=False):
        return TlvHelper.create_data(53, '0010', 0, 1, 0, abnormal)

    #泵电压值Ua，tag#54
    def create_pumpplc_ua(self, abnormal=False):
        return TlvHelper.create_data(54, '0100', 2, 220, 800, abnormal)

    #泵电流值La，tag#55
    def create_pumpplc_la(self, abnormal=False):
        return TlvHelper.create_data(55, '0100', 3, 4, 40, abnormal)

    #泵运行总功功率，tag#56
    def create_pumpplc_powers(self, abnormal=False):
        return TlvHelper.create_data(56, '0100', 2, 1000, 0, abnormal)

    #泵运行频率，tag#57
    def create_pumpplc_hz(self, abnormal=False):
        return TlvHelper.create_data(57, '0100', 2, 49, 0, abnormal)

    #泵工作温度，tag#58
    def create_pumpplc_temp(self, abnormal=False):
        return TlvHelper.create_data(58, '0100', 2, 20, 80, abnormal)

    #泵工作振幅，tag#59
    def create_pumpplc_amplitude(self, abnormal=False):
        return TlvHelper.create_data(59, '0100', 2, 2, 80, abnormal)

    #泵运行时间，tag#60
    def create_pumpplc_runtime(self, abnormal=False):
        return TlvHelper.create_data(60, '0110', 2, 300, 0, abnormal)

    #泵水流速，tag#61
    def create_pumpplc_flow(self, abnormal=False):
        return TlvHelper.create_data(61, '0110', 3, 6, 100, abnormal)

    #泵累计流量，tag#62
    def create_pumpplc_flows(self, abnormal=False):
        return TlvHelper.create_data(62, '0110', 3, 23435, 0, abnormal)

    #泵进口压力，tag#63
    def create_pumpplc_inpress(self, abnormal=False):
        return TlvHelper.create_data(63, '0100', 3, 1, 0, abnormal)

    #泵出口压力，tag#64
    def create_pumpplc_outpress(self, abnormal=False):
        return TlvHelper.create_data(64, '0100', 3, 1, 0, abnormal)

    #泵故障次数，tag#65
    def create_pumpplc_broken(self, abnormal=False):
        return TlvHelper.create_data(65, '0100', 0, 0, 3, abnormal)

    #泵设定频率，tag#66
    def create_pumpplc_sethz(self, abnormal=False):
        return TlvHelper.create_data(66, '0100', 2, 50, 1, abnormal)

    #泵设定压力，tag#67
    def create_pumpplc_setpress(self, abnormal=False):
        return TlvHelper.create_data(67, '0100', 3, 2, 100, abnormal)

    #泵电压值Ub，tag#68
    def create_pumpplc_ub(self, abnormal=False):
        return TlvHelper.create_data(68, '0100', 2, 200, 1000, abnormal)

    #泵电压值Uc，tag#69
    def create_pumpplc_uc(self, abnormal=False):
        return TlvHelper.create_data(69, '0100', 2, 200, 1000, abnormal)

    #泵电压值Ib，tag#70
    def create_pumpplc_ib(self, abnormal=False):
        return TlvHelper.create_data(70, '0100', 3, 6, 1000, abnormal)

    #泵电压值Ic，tag#71
    def create_pumpplc_ic(self, abnormal=False):
        return TlvHelper.create_data(71, '0100', 3, 6, 1000, abnormal)

    #泵运行总无功功率，tag#72
    def create_pumpplc_repowers(self, abnormal=False):
        return TlvHelper.create_data(72, '0100', 2, 5000, 0, abnormal)

    #泵运行总有功电能，tag#73
    def create_pumpplc_epowers(self, abnormal=False):
        return TlvHelper.create_data(73, '0110', 2, 93454, 0, abnormal)

    #泵运行总无功电能，tag#74
    def create_pumpplc_erepowers(self, abnormal=False):
        return TlvHelper.create_data(74, '0110', 2, 93454, 0, abnormal)

    #泵总功率因数，tag#75
    def create_pumpplc_factors(self, abnormal=False):
        return TlvHelper.create_data(75, '0011', 3, 1, 0, abnormal)

    '''生产蓄水池水质补充参数[TAG:76-79]'''
    def create_waterpooladd_data(self, abnormal):
        data = self.create_waterpooladd_conductivity(abnormal)
        data.extend(self.create_waterpooladd_press(abnormal))
        data.extend(self.create_waterpooladd_temp(abnormal))
        data.extend(self.create_waterpooladd_door(abnormal))
        return data

    # 水质导电率，tag#76
    def create_waterpooladd_conductivity(self, abnormal=False):
        return TlvHelper.create_data(76, '0100', 2, 3, 0, abnormal)

    # 蓄水池管路设定压力，tag#77
    def create_waterpooladd_press(self, abnormal=False):
        return TlvHelper.create_data(77, '0100', 3, 2, 100, abnormal)

    # 水质温度，tag#78
    def create_waterpooladd_temp(self, abnormal=False):
        return TlvHelper.create_data(78, '0100', 2, 20, 100, abnormal)

    # 蓄水池门状态，tag#79
    def create_waterpooladd_door(self, abnormal=False):
        return TlvHelper.create_data(79, '0010', 0, 1, 0, abnormal)