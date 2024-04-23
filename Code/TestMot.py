import machine
import time

go = machine.PWM(machine.Pin(16))
go.freq(490)
Led = machine.Pin("LED", machine.Pin.OUT)
#4100 low 8500(?) high
go.duty_u16(8500)
time.sleep_ms(5000)
go.duty_u16(800)

"""
while True:
    for duty in range(5000, 6000):
        go.duty_u16(duty)
        time.sleep(0.001)
	
    #for duty in range(7803, 1950, -1):
        #go.duty_u16(duty)
        #time.sleep(0.0006)
    go.duty_u16(1950)
    Led.toggle()
    time.sleep_ms(500)
    print("done")
    """