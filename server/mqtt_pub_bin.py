from mqtt import mqtt_publisher
from scheduler import start_schedule
import time
import struct

# start_schedule()

bin_data = struct.pack('<ddddddddddddddddddddddddddd',
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464,
        1.1233131,
        2.313133, 
        3.446464
     )

while True:
    mqtt_publisher(bin_data)
    time.sleep(1)
