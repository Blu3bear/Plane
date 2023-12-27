import serial
import pynmea2

ser = serial.Serial('COM4')
print(ser.name)
isGA = False
while not isGA:
    sentence = ser.readline().decode('utf-8').strip()
    isGA = sentence.startswith('$GPGGA')
    if isGA:
        msg = pynmea2.parse(sentence)
        lat = msg.latitude
        lon = msg.longitude
        alt = msg.altitude
        print(f"lat: {lat}, lon: {lon}, altitude: {alt}")

ser.close()