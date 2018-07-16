
from Config.Config import Config
from TLV.PumpHouse import PumpHouse
from TLV.WaterMeter import WaterMeter

class SmartWater:
    def create_smartwater_data(self, list, abnormal):
        dataPhouse = []
        dataWmeter = []
        phouse = PumpHouse()
        wmeter = WaterMeter()
        for value in list:
            if value == Config.WMETER_OBJECTS[0]:
                dataPhouse.extend(phouse.creat_pump_data(abnormal))
            elif value == Config.WMETER_OBJECTS[1]:
                dataPhouse.extend(phouse.create_waterpool_data(abnormal))
            elif value == Config.WMETER_OBJECTS[2]:
                dataPhouse.extend(phouse.create_enveriment_data(abnormal))
            elif value == Config.WMETER_OBJECTS[3]:
                dataPhouse.extend(phouse.create_electric_data(abnormal))
            elif value == Config.WMETER_OBJECTS[4]:
                dataPhouse.extend(phouse.create_watermeter_data(abnormal))
            elif value == Config.WMETER_OBJECTS[5]:
                dataPhouse.extend(phouse.create_pumpplc_data(abnormal))
            elif value == Config.WMETER_OBJECTS[6]:
                dataPhouse.extend(phouse.create_waterpooladd_data(abnormal))
            elif value == Config.WMETER_OBJECTS[7]:
                dataWmeter.extend(wmeter.create_base_data())
            elif value == Config.WMETER_OBJECTS[8]:
                dataWmeter.extend(wmeter.create_core_data(abnormal))
            elif value == Config.WMETER_OBJECTS[9]:
                dataWmeter.extend(wmeter.create_maintenance())
        return dataPhouse, dataWmeter