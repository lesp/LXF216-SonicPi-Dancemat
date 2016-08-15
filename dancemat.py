from inputs import get_gamepad
from psonic import *
from threading import Thread

def beat():
	while True:
		sample(DRUM_HEAVY_KICK)
		sleep(0.5)

def Amen():
	while True:
		sample(LOOP_AMEN, amp=0.5)
		sleep(1.753)


while True:
    events = get_gamepad()
    for event in events:
        print(event.code, event.state)
        button = event.code
        print("The button pressed was ",button)
        use_synth(PROPHET)
        if button == "BTN_BASE3" and event.state == 1:
            print("SELECT")
            Amen_thread = Thread(target=Amen)
            Amen_thread.start()   
        elif button == "BTN_BASE4" and event.state == 1:
        	print("START")
        	beat_thread = Thread(target=beat)
        	beat_thread.start()
        elif button == "BTN_BASE" and event.state == 1:
        	print("X")
        	sample(DRUM_CYMBAL_CLOSED, amp=0.5)
        elif button == "BTN_THUMB2" and event.state == 1:
        	print("UP")
        	play(60)
        elif button == "BTN_BASE2" and event.state == 1:
        	print("O")
        	sample(DRUM_SNARE_SOFT, amp=0.5)
        elif button == "BTN_TRIGGER" and event.state == 1:
        	print("LEFT")
        	play(62)
        elif button == "BTN_TOP" and event.state == 1:
        	print("RIGHT")
        	play(64)
        elif button == "BTN_TOP2" and event.state == 1:
        	print("TRIANGLE")
        	sample(DRUM_SNARE_HARD, amp=0.5)
        elif button == "BTN_THUMB" and event.state == 1:
        	print("DOWN")
        	play(66)
        elif button == "BTN_PINKIE" and event.state == 1:
        	print("SQUARE")
        	sample(DRUM_BASS_HARD, amp=0.5)

