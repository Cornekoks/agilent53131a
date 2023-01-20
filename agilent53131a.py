import pyvisa

class Agilent53131a():
    def __init__(self):
        self.rm = pyvisa.ResourceManager()#'C:\Windows\System32\\visa64.dll')
        print(self.rm.list_resources())
        return

    def open_device(self, devicename):
        self.inst=self.rm.open_resource(devicename)
        return

    def close_device(self):
        self.inst.clear()
        return

    def get_data(self):
        countrate=self.inst.query(':Calculate:DATA?')
        return countrate

