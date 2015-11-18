"""
Tested on CodeSkulptor
www.codeskulptor.org

"Stopwatch: The Game"
Constructs a timer with an associated interval of 0.1 seconds. 
The timer can be started and stopped clicking the buttons - "Start" and "Stop". 
A game begins with the start of the timer and ends when the timer is stopped. 
Stopping a running timer at a whole second interval, earns a game point. 
A set of games can be played by (re)-starting the timer. 
Hitting the "Reset" button refreshes the stopwatch.
"""



import simplegui
import random 

# global states and variables
width = 300
height = 300
timer_position = [110, 150]
score_position = [250, 25]
interval = 100
sec = 0
min = 0
hr = 0
t0 = 0
game_win = 0
game_counter = 0
reset = False
timer_running = False


# helper functions
def convert(t):
    """
    keeps track of tenths of seconds and 
    converts to hours, minute and second
    """
    global sec, min, hr
    
    if t >= 9:
        sec = sec + 1
    
    if sec >= 60 and sec % 60 == 0:
        min = min + 1
        sec = sec - 60  
        
    if min >= 60 and min % 60 == 0:
        hr = hr + 1
        min = min - 60  
        
    
def format():
    """
    converts time (hour, minute, second and tenths of 
    second) into a formatted string A:BC.D
    """
    str_hr = "0" + str(hr)
    str_min = "0" + str(min)
    str_sec = "0" + str(sec)
    
    display_time = str_hr[-2:] + ":" + str_min[-2:]+ ":" + str_sec[-2:]+ "." + str(t0)   
     
    return display_time


def tick():
    global t0
    t0 += 1
    if t0 == 10:
        t0 = 0 
        
    convert(t0)
    format()
    
    
    
# draw functions
def draw_on_canvas(canvas):
    global reset, game_counter, game_win
   
    canvas.draw_text(format(), timer_position, 24, "White")
    
    if reset:
        timer.stop() 
    else: 
        game_score = str(game_win) + "/" + str(game_counter)
        canvas.draw_text(game_score, score_position, 24, "Red")
        
    reset = False
        
        
# handler function
def start_handler():
    global timer_running
    timer.start()
    timer_running = True
    frame.set_draw_handler(draw_on_canvas)
     
def stop_handler():
    global game_counter, game_win, timer_running
    timer.stop()
    if timer_running and t0 == 0:
        game_win += 1
        game_counter += 1
    if timer_running and t0 != 0: 
        game_counter += 1
    timer_running = False
           
def reset_handler():
    global t0, sec, min, reset, game_win, game_counter
    t0 = 0
    sec = 0
    min = 0
    game_win = 0
    game_counter = 0
    reset = True
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# define event handlers for buttons; 
# "Start", "Stop", "Reset"
frame.add_button('Start', start_handler, 100)
frame.add_button('Stop', stop_handler, 100)
frame.add_button('Reset',reset_handler, 100)

# Start frame
frame.start() 
frame.set_draw_handler(draw_on_canvas)

# Register event handlers   
timer = simplegui.create_timer(interval, tick)



