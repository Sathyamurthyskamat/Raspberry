#Importing Library
import RPi.GPIO as Gpio # Insted of Gpio you can use any word.
import time
Gpio.setmode(Gpio.BOARD)#Raspberry pi have BCM(BroadCom) and Board modes.
Gpio.setwarnings(False)
Gpio.setup(8,Gpio.OUT)
  
#set Gpio Pins
Gpio_TRIGGER = 10
Gpio_ECHO = 12
 
#set Gpio direction (IN / OUT)
Gpio.setup(Gpio_TRIGGER, Gpio.OUT)
Gpio.setup(Gpio_ECHO, Gpio.IN)
 
def distance():
    # set Trigger to HIGH
    Gpio.output(Gpio_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    Gpio.output(Gpio_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while Gpio.input(Gpio_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while Gpio.input(Gpio_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            #if you want do some thing you can do from below
            '''if dist<10:
                Gpio.output(8,Gpio.HIGH)
                time.sleep(3)
                Gpio.output(8,Gpio.LOW)
                time.sleep(1)'''
                
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        Gpio.cleanup()