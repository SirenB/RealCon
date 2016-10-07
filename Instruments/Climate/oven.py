import time
import pyvisa
import epydoc

class Oven(object):
    """
    Here should be description what device this library is used for

    Here summarise what service this library provide
    """

    def __init__(self, com, baud_rate=19200):
        """
        Constructor of this class

        This device should be connected by serial port, the constructor let user to input port number and baud rate
        @param com: Serial port number. like: COM5
        @param baud_rate: Serial baud rate. default value is 19200. Baud rate should keep same with device setting
        """
        ov = pyvisa.ResourceManager()
        self.dev = ov.open_resource(com)    # SUCH AS:"COM4"
        self.dev.baud_rate = baud_rate      # SUCH AS: "19200"
        # print self.dev.query("CONVERTER VERSION?")
        if self.dev.query("CONVERTER VERSION?") == "STEN TO GWS CONVERTER, VER:1.00":
            print ("The oven is connected!")
        # else:
        #     print ("Connected failed, please check!")

    def get_temperature(self):
        """
        Get current temperature value in device

        @return: temperature value
        """
        print ("The temperature you get as bellow:")
        temp = self.dev.query("TEMP?")
        temp = temp.split(',', 3)
        return temp[0]

    def set_temperature(self, temp):
        """
        Set target temperature to device.

        @param temp: target temperature value
        @return: None
        """
        self.dev.write("TEMP,S%f" % temp)

    def get_humidity(self):
        """
        Get current humidity value in device

        @return: humidity value
        """
        print ("The humidity you get as bellow:")
        humi = self.dev.query("HUMI?")
        humi = humi.split(',', 3)
        return humi[0]

    def set_humidity(self, humidity):
        """
        Set target humidity to device

        @param humidity: target humidity value
        @return: None
        """
        self.dev.write("HUMI,S%d" % humidity)


"""Example"""
# oven_dean = Oven("COM4", 19200)      # Instantiation
"""*****"""
# get_temp = oven_dean.get_temperature()
# print get_temp
#
# time.sleep(2)
# get_humi = oven_dean.get_humidity()
# print get_humi
