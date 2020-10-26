import machine
import time
import dht

DHT = dht.DHT11(machine.Pin(13))

while True:
    DHT.measure()
    print('Temp:', DHT.temperature(), 'Hum:', DHT.humidity())
    time.sleep_ms(1000)




