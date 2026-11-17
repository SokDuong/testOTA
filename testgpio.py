from misc import ADC
from machine import Pin
import utime

adc = ADC()
adc.open()                      # returns 0 on success
gpio44 = Pin(Pin.GPIO44, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio5 = Pin(Pin.GPIO5, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio6 = Pin(Pin.GPIO6, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio9 = Pin(Pin.GPIO9, Pin.IN, Pin.PULL_DISABLE, 0)
gpio44.value(1)                 # set GPIO44 high to enable GPS 
gpio5.value(1)                  # set GPIO5 high
gpio6.value(0)                  # set GPIO6 low

while True:
    mv = adc.read(ADC.ADC0)     # voltage in mV, or -1 on failure
    print("ADC0:", mv, "mV")
    print("GPIO9:", gpio9.read())
    gpio5.value(not gpio5.value())  # set GPIO5 high
    gpio6.value(not gpio6.value())  # set GPIO6 low
    utime.sleep_ms(500)

adc.close()