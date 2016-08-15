from inputs import get_gamepad
from psonic import *
from threading import Thread
import time

def beat():
	while True:
		sample(DRUM_HEAVY_KICK)
		sleep(0.5)


while True:
    events = get_gamepad()
    for event in events:
        print(event.code, event.state)
        button = event.code
        print("The button pressed was ",button)
        #time.sleep(0.3)
        if button == "BTN_BASE3" and event.state == 1:
            print("SELECT")
            #time.sleep(0.1)
        elif button == "BTN_BASE4" and event.state == 1:
        	print("START")
        	beat_thread = Thread(target=beat)
        	beat_thread.start()
        	#time.sleep(0.1)
        elif button == "BTN_BASE" and event.state == 1:
        	print("X")
        	sample(LOOP_AMEN, amp=0.5)
        	#sleep(0.877)
        elif button == "BTN_THUMB2" and event.state == 1:
        	print("UP")
        	time.sleep(0.1)
        	use_synth(SAW)
        	play(60)
        	#sleep(0.1)
        elif button == "BTN_BASE2" and event.state == 1:
        	print("O")
        	timesleep(0.1)
        elif button == "BTN_TRIGGER" and event.state == 1:
        	print("LEFT")
        	play(62)
        	#sleep(0.1)
        elif button == "BTN_TOP" and event.state == 1:
        	print("RIGHT")
        	play(64)
        	#sleep(0.1)
        elif button == "BTN_TOP2" and event.state == 1:
        	print("TRIANGLE")
        	#time.sleep(0.1)
        elif button == "BTN_THUMB" and event.state == 1:
        	print("DOWN")
        	play(66)
        	#sleep(0.1)
        elif button == "BTN_PINKIE" and event.state == 1:
        	print("SQUARE")
        	#time.sleep(0.1)
