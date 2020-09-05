from picamera import PiCamera , Color
from time import sleep
import curses
import RPi.GPIO as GPIO
valsv = 4.5
GPIO.setmode(GPIO.BOARD)
x = 0
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin
p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
p.start(2.5)# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key respo
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
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
                x = 0.3
               
            elif char == ord('2'):
                x = 0.5
            elif char == ord('i'):
                valsv += 0.05
                p.ChangeDutyCycle(valsv)  # Move servo to 0 degrees
                
                print(valsv)
            elif char == ord('t'):
                camera = PiCamera()
                camera.brightness = 45
                camera.rotation = 90
                camera.resolution = (1280,720)
                camera.framerate = 24
                camera.annotate_background = Color('orange')
                camera.annotate_foreground = Color('yellow')
                camera.annotate_text = "photo by bot varis"
                camera.annotate_text_size = 50
                #camera.start_preview()
                camera.start_recording("/home/pi/Desktop/botph/(numca).h264")
     
                sleep(200)
                camera.stop_recording()
               #camera.capture("/home/pi/Desktop/pic.jpg")
               #camera.stop_preview()

            elif char == ord('k'):
                valsv -= 0.05
                p.ChangeDutyCycle(valsv)  # Move servo to 0 degrees
                
                print(valsv)                
            elif char == ord('f'):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
           
            elif char == ord('w'):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
                GPIO.output(8,True)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,True)
                
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
            elif char == ord('s'):
                
                
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,True)
                GPIO.output(12,True)
                GPIO.output(16,False)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
            elif char == ord('d'):
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
                GPIO.output(8,False)
                GPIO.output(10,True)
                GPIO.output(12,False)
                GPIO.output(16,True)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
            elif char == ord('a'):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
                GPIO.output(8,True)
                GPIO.output(10,False)
                GPIO.output(12,True)
                GPIO.output(16,False)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
                
                
                
                
                
                
            elif char == ord('q'):
                
                
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
                GPIO.output(8,False)
                GPIO.output(10,True)
                GPIO.output(12,True)
                GPIO.output(16,False)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
                
                
            elif char == ord('e'):
                
                
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
                GPIO.output(8,True)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,True)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
            
            
            elif char == ord('t'):
                
                
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,True)
                GPIO.output(12,False)
                GPIO.output(16,False)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
            
            
            elif char == ord('r'):
                
                
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,True)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
                sleep(x)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
                GPIO.output(12,False)
                GPIO.output(16,False)
                
                
                
            elif char == 10:
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    



