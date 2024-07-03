import pyvisa
import os
import time
import numpy as np
import datetime
import serial


print("hi")
# ser = serial.Serial('COM3', 115200) # controller

# StartTime = datetime.datetime.now()

# multim_1 = "192.168.1.132"
# multim_2 = "192.168.1.61"

# response = os.system("ping -n 1 " + multim_1)
# response = os.system("ping -n 1 " + multim_2)

# m_1_adr = "TCPIP::"+ multim_1 + "::inst0::INSTR"
# m_2_adr = "TCPIP::"+ multim_2 + "::inst0::INSTR"

# rm = pyvisa.ResourceManager("@py")


# try:
#     meas_d1 = rm.open_resource(m_1_adr)
# except pyvisa.errors.VisaIOError as e:
#     print("ERROR:")
#     print(e)
#     exit(1)

# try:
#     meas_d2 = rm.open_resource(m_2_adr)
# except pyvisa.errors.VisaIOError as e:
#     print("ERROR:")
#     print(e)
#     exit(1)

# # meas_d1.write(":SYST:COMM:ENAB OFF,USB")
# # time.sleep(1)
# # meas_d1.write(":SYST:COMM:ENAB ON,USB")
# #err = meas_d1.query("SYST:ERR?")
# #meas_d1.write("VOLTage:APERture:ENABled 1")
# #meas_d1.write("VOLTage:RANGe 10")
# #meas_d1.write("VOLTage:NPLC 10")


# meas_d1.query("MEAS:TEMP? RTD,85")
# meas_d2.query("MEAS:VOLT:DC? 10,0.001")


# with open('test.xls', 'a') as f:
#     try:
#         counter = 0
#         last_temp = 0
#         cool_or_hot = 0
#         while 1:
#             temp_mag = ser.readline()           
#             msmt_hall = meas_d1.query("READ?") # multimeter
#             temp = (float(msmt_hall))
#             msmt_hall = meas_d2.query("READ?") # multimeter
#             volt = (float(msmt_hall))
             
#             f.write("Mult1=\t{0}\tMult2=\t{1}\t{2}\t{3}\n".format(temp, volt, (temp_mag), datetime.datetime.now()))
#             print("Mult1=\t{0}\tMult2=\t{1}\t{2}".format(temp, volt, str(temp_mag)))
#             counter += 1


#     except KeyboardInterrupt:
#         FinishTime = datetime.datetime.now()       
#         DeltaTime = 3600 * (FinishTime.hour - StartTime.hour) + 60 * (FinishTime.minute-StartTime.minute) + (FinishTime.second-StartTime.second)        
#         print("Time {:d} sec".format(DeltaTime)) 
#         f.close()
#         rm.close()
#         ser.close()
#         exit(1)



# def MultiplexerInputs(ser):
#     text = str(input())
#     ser.write(text.encode('ascii'))

# #f = open('../../../measurements.txt', 'a')
# ##f.write('smthx10')
# #f.close()
# #f = open('measurements.txt', 'r')

# #print(f.read())
# #f.close()

