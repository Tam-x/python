'''
created by tanxing in 2018/07/05
'''
class Config:
    VERSION  = '2.1.0'
    TOPIC_BASE = 'dtu/simulator/%s/%s/'
    USER = 'admin'
    PWD = 'password'
    TOPIC_L1_SWATER = 'swater'
    TOPIC_L1_SECS = 'secs'
    TOPIC_L1_DEFAULT = TOPIC_L1_SWATER
    TOPIC_L2_DEFAULT = 'default'
    TOPIC_L3_DEFAULT = '0.0.0.0'
    BROKER = 'iot.eclipse.org'

    WMETER_OBJECTS = ['1、泵', '1、蓄水池', '1、环境', '1、电表', '1、水表', '1、泵PLC采集','1、蓄水池水质',
                     '1、水表基础数据','1、水表核心数据','1、水表维护数据']

    SECS_OBJECTS = ['2、环境数据', '2、电表数据', '2、相变温度']


    FunctionCodeMap = {'0000':1, '0001':1, '0010':1, '0011':2, '0100':2, '0101':4, '0110':4, '0111':8, '1000':8,
                       '1001':4, '1010':8, '1011':6, '1100':-1, '1101':-1,}

    MESSAGE_PUMP_HOUSE = 0x01
    MESSAGE_METER_WATER = 0x02

    PROJECT_SWATER_STR = '1 水务二期'
    PROJECT_SECS_STR = '2 SECS热能'

    PROJECTS = [PROJECT_SWATER_STR, PROJECT_SECS_STR]

    DATA_MAP = {PROJECT_SWATER_STR:WMETER_OBJECTS, PROJECT_SECS_STR:SECS_OBJECTS}