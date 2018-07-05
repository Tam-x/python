'''
created by tanxing in 2018/07/05
'''

from TLV import TlvHelper

'''
生产泵房数据
'''
class PumpHouse:
    '''
    生产泵数据
    @abnormal 异常控制标志
    '''
    def creat_pump_data(self):
        data = self.create_pump_temp()
        data.extend(self.create_pump_amplitude())
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
    def create_waterpool_data(self):
        data = self.create_waterpool_ph()
        data.extend(self.create_waterpool_turbidity())
        data.extend(self.create_waterpool_chlorine())
        data.extend(self.create_waterpool_waterlevel())
        data.extend(self.create_waterpool_inpress())
        data.extend(self.create_waterpool_outpress())
        data.extend(self.create_waterpool_flow())
        data.extend(self.create_waterpool_flows())
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
    def create_enveriment_data(self):
        data = self.create_env_temp()
        data.extend(self.create_env_humi())
        data.extend(self.create_env_noise())
        data.extend(self.create_env_somke())
        data.extend(self.create_env_ponding())
        data.extend(self.create_env_door())
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
    def create_electric_data(self):
        data = self.create_elc_avoltage()
        data.extend(self.create_elc_bvoltage())
        data.extend(self.create_elc_cvoltage())
        data.extend(self.create_elc_acurrent())
        data.extend(self.create_elc_bcurrent())
        data.extend(self.create_elc_ccurrent())
        data.extend(self.create_elc_ct())
        data.extend(self.create_elc_pt())
        data.extend(self.create_elc_hz())
        data.extend(self.create_elc_powers())
        data.extend(self.create_elc_repowers())
        data.extend(self.create_elc_factors())
        data.extend(self.create_elc_degrees())
        data.extend(self.create_elc_redegrees())
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
    生产水表基础数据
    '''
    def create_watermeter_data(self):
        data = self.create_watermeter_flow()
        data.extend(self.create_watermeter_press())
        return data

    #水表流量读数，tag#51
    def create_watermeter_flow(self, abnormal=False):
        return TlvHelper.create_data(51, '0110', 3, 11209, 0, abnormal)

    #水表压力，tag#52
    def create_watermeter_press(self, abnormal=False):
        return TlvHelper.create_data(52, '0100', 3, 2, 0, abnormal)

    '''生产泵PLC采集数据 TAG(37-50)'''
    def create_pumpplc_data(self):
        data = self.create_pumpplc_status()

    #泵运行状态，tag#53
    def create_pumpplc_status(self, abnormal=False):
        return TlvHelper.create_data(53, '0010', 0, 1, 0, abnormal)

    #泵运行状态，tag#53
    def create_pumpplc_status(self, abnormal=False):
        return TlvHelper.create_data(53, '0010', 0, 1, 0, abnormal)

p = PumpHouse()

for i in range(10):
    print(p.create_watermeter_data())
