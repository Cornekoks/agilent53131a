import pyvisa

__version__ = '0.0'

class Agilent53131a():
    def __init__(self):
        self.rm = pyvisa.ResourceManager()#for me, it need to name the full path, probably not always necesarry 'C:\Windows\System32\\visa64.dll')
        print(self.rm.list_resources())
        return

    def open_device(self, devicename):
        "enter the devicename as a string, it is one of the researches, see self.rm.list_resources()"
        try:
            self.inst=self.rm.open_resource(devicename)
        except Exception as e:
            print(e)
            print('Could not load system, choose one of these: ')
            print(self.rm.list_resources())
        return

    def close_device(self):
        "close device (only if loaded of course"
        self.inst.clear()
        return

    def get_counts(self):
        "get the counts in counter per second"
        countrate=self.inst.query(':Calculate:DATA?')
        return countrate

