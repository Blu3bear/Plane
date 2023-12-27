import serial
import pynmea2  # You can install this library using: pip install pynmea2

def read_gps_data(port, baudrate=9600, timeout=1):
    ser = serial.Serial(port, baudrate, timeout=timeout)
    try:
        # Open the serial port
        print(f"Connected to {port} at {baudrate} baud")

        while True:
            # Read data from the serial port
            data = ser.readline().decode('utf-8').strip()

            # Parse NMEA sentence for location
            if data.startswith('$GPGGA'):
                try:
                    posMsg = pynmea2.parse(data)
                    latitude = posMsg.latitude
                    longitude = posMsg.longitude
                    altitude = posMsg.altitude
                    print(f"Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude} meters")
                except pynmea2.ParseError as e:
                    print(f"Error parsing NMEA sentence: {e}")
            elif data.startswith('$GPVTG'):
                try:
                    groundMsg = pynmea2.parse(data)
                    groundSpeed = groundMsg.spd_over_grnd_kmph
                    track = groundMsg.true_track
                    print(f"Ground Speed: {groundSpeed}, True track: {track}")
                except pynmea2.ParseError as e:
                    print("{e}")
            elif data.startswith('$GPRMC'):
                try:
                    velocityMsg = pynmea2.parse(data)
                except pynmea2.ParseError as e:
                    print("{e}")

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        # Close the serial port when done
        if ser.is_open:
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    # Replace 'COM4' with the actual serial port on your system (e.g., '/dev/ttyUSB0' on Linux)
    gps_port = 'COM4'
    
    # You can adjust the baudrate and timeout values based on your device specifications
    read_gps_data(gps_port, baudrate=9600, timeout=1)
