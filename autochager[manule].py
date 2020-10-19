from picamera import PiCamera , Color
import time 
import curses
import RPi.GPIO as GPIO


x = 100


     # Declaring GPIO 21 as output pin
# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key respo
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)#m1
GPIO.setup(38,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)#m4
GPIO.setup(36,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)#m2
GPIO.setup(23,GPIO.OUT)#m3



pwm40 = GPIO.PWM(40,100)
pwm24 = GPIO.PWM(24,100)
pwm37 = GPIO.PWM(37,100)
pwm23 = GPIO.PWM(23,100)
pwm24.start(0)
pwm40.start(0)
pwm37.start(0)
pwm23.start(0)


screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
    while True:   
        char = screen.getch()
        if char == ord('o'):
             break
           
        elif char == ord('1'):
             x = 10
             pwm40.ChangeDutyCycle(x)
             pwm37.ChangeDutyCycle(x)
             pwm24.ChangeDutyCycle(x)
             pwm23.ChangeDutyCycle(x)
                
             print(x)
        elif char == ord('2'):
             x = 50
             pwm40.ChangeDutyCycle(x)
             pwm37.ChangeDutyCycle(x)
             pwm24.ChangeDutyCycle(x)
             pwm23.ChangeDutyCycle(x)
             
             print(x)
        elif char == ord('3'):
             x = 100
             pwm40.ChangeDutyCycle(x)
             pwm37.ChangeDutyCycle(x)
             pwm24.ChangeDutyCycle(x)
             pwm23.ChangeDutyCycle(x)
             
             print(x)
           
                
           
           
        if char == ord('s'):
             print(x)
             print('backward')
             GPIO.output(38,True)
             GPIO.output(36,False)
             GPIO.output(32,True)
             GPIO.output(26,False)
             GPIO.output(35,True)
             GPIO.output(33,False)
             GPIO.output(31,True)
             GPIO.output(29,False)
             time.sleep(0.1)
             GPIO.output(38,False)
             GPIO.output(36,False)
             GPIO.output(32,False)
             GPIO.output(26,False)
             GPIO.output(35,False)
             GPIO.output(33,False)
             GPIO.output(31,False)
             GPIO.output(29,False)
            
       
        if char == ord('w'):
             print(x)
             print('forward')
             GPIO.output(38,False)
             GPIO.output(36,True)
             GPIO.output(32,False)
             GPIO.output(26,True)
             GPIO.output(35,False)
             GPIO.output(33,True)
             GPIO.output(31,False)
             GPIO.output(29,True)
             time.sleep(0.1)
             GPIO.output(38,False)
             GPIO.output(36,False)
             GPIO.output(32,False)
             GPIO.output(26,False)
             GPIO.output(35,False)
             GPIO.output(33,False)
             GPIO.output(31,False)
             GPIO.output(29,False)
            
       
      
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

