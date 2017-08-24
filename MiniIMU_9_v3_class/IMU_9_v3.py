

#this is the basic template for the IMU class for rasberry pi
#IMU class for the Mini IMU v3
class IMU(self):

    #constrctor for the IMU
    def __init__(self):

        self.accelerometer = [[0],
                              [0],
                              [0]]
        self.gyroscope = [[0],
                         [0],
                         [0]]
        self.magnetometer = [[0],
                             [0],
                             [0]]
    #first these i2c functions need to be implemented

    #this fucntion writes a value according to the specify address
    def i2c_write(self,address,value):

    #this function reads a value according to the specify address
    def i2c_read(self,address):

    #this is the principlal IMU read function that read all the raw data
    def read_IMU(self):
        return imu_val[[self.accelerometer],[self.gyroscope],
                        [self.magnetometer]]
