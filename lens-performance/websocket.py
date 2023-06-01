import os
import asyncio
from websockets.server import serve
import json
import serial
import time

os.system("clear")
# Set up the Serial connection to capture the Microbit communications
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "/dev/cu.usbmodem212302"
ser.timeout = 0.1  # Set a timeout value to make readline non-blocking
ser.open()
print("ok1")

async def getData(websocket):
    while True:
        microbitdata = str(ser.readline())  # Remove trailing newline characters
        if microbitdata:
            print("ok5")
            print(microbitdata)
            await websocket.send(json.dumps(microbitdata))

async def main():
    print("ok2")
    async with serve(getData, "localhost", 13001):
        print("ok3")
        await asyncio.Future()

asyncio.run(main())

# Close the serial connection
ser.close()
