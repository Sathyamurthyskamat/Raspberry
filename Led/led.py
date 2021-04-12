#Importing Library
import RPi.GPIO as Gpio # Insted of Gpio you can use any word.
import time

#Setup Pin, Modes etc...
Gpio.setmode(Gpio.BCM) #Raspberry pi have BCM(BroadCom) and Board modes.
Gpio.setwarnings(False)# while executing programs neglect warnings.
Gpio.setup(3,Gpio.OUT) #Setup pin as Output pin.

#Printing 'LED ON' and 'LED OFF' with GPIO pins.
print("LED ON")
Gpio.output(3,Gpio.HIGH)
print("LED OFF")
Gpio.output(3,Gpio.LOW)

#If you want continues blinking remove the (''') both the side.
'''while(1): # Or You can Use 'True'
    print("LED ON")
    Gpio.output(3,Gpio.HIGH)
    print("LED OFF")
    Gpio.output(3,Gpio.LOW)'''