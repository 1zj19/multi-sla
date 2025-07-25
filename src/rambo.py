import time

import serial


def send_message(serial_port, command):
    command = command.strip().encode() + b"\n"
    serial_port.reset_input_buffer()  # Clear garbage before sending
    serial_port.write(command)
    while True:
        line = serial_port.readline().decode().strip()
        print(line)
        if not line:
            break


def main():

    # Open the serial port with timeout
    # ser = serial.Serial("/dev/tty.usbmodem141101", 250000, timeout=1.0)
    ser = serial.Serial("/dev/tty.usbmodem21101", 250000, timeout=1.0)

    # Give the device some time to initialize
    time.sleep(1)
    print("Device Ready")
    try:
        while True:
            command = input("Enter command (or 'Ctrl+c' to quit): ")
            if command.lower() == "exit":
                break
            send_message(ser, command)
    finally:
        ser.close()


if __name__ == "__main__":
    main()

