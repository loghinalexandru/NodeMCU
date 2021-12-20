import serial
import wmi
import time

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
node = serial.Serial("COM3", 115200)

while True:
    temp_value = ""
    cpu_found = False
    gpu_found = False
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.Name == "GPU Hot Spot" and gpu_found == False:
            temp_value += "GPU" + " " + str(round(sensor.Value,1))
            gpu_found = True
            temp_value += "\n"
        if sensor.Name == "CPU Package" and cpu_found == False:
            temp_value += "CPU" + " " + str(round(sensor.Value,1))
            cpu_found = True
    node.write(temp_value.encode())
    time.sleep(1)