# import curses, GPIO and time
import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
x = 0
# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == ord('1'):
                x = 0.3
            elif char == ord('2'):
                x = 0.5
           
            elif char == ord('w'):
                
               
            elif char == ord('d'):
                                
                 
                 
                 
                 
            def forword():
                
                
                    
                def blackword():
                    
            
                    
                    def turnleft():
                        
                        
                        
                        
                        def turnright():
                            
                                                
                            
                            def right():
                                
                                
                                
                                
                                def left():
                                    
                                    
                
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

