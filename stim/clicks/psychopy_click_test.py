import psychopy
from psychopy import event, visual, core

# Following the coder tutorial here:
# https://psychopy.org/coder/codeStimuli.html

win = visual.Window(
	size=(1680, 1050), 
	fullscr=True
	)

WAIT_TIME_s = 5


message = visual.TextStim(win, text=f'Collect clicks for {WAIT_TIME_s}s')
message.autoDraw = True

# https://www.psychopy.org/api/event.html#psychopy.event.Mouse
mouse = event.Mouse(visible=True)

MOVE_TEST = not True
CLICK_TEST = True

# initialize mouse params for the test
if MOVE_TEST:
	pos = []
	times = []
	mouse.getPos() # writes to self.prevPos, see https://discourse.psychopy.org/t/event-mouse-mousemoved-failing/4125
elif CLICK_TEST:
	all_buttons = []
	all_times = []
	mouse.clickReset()

# Wait for mouse events to happen
clock = core.Clock()
while clock.getTime() < WAIT_TIME_s:
	win.flip()
	
	if MOVE_TEST:
		mouse.mouseMoved(reset=(0,0))
		if not mouse.mouseMoved():
			win.flip()
		if mouse.mouseMoved():
			times.append(mouse.mouseClock.getTime())
			pos.append(mouse.getPos())
			# mouse.setPos(newPos=(0, 0))
			win.flip()
	elif CLICK_TEST:
		# Note: we actually have to click (tap doesn't register)
		buttons, times = mouse.getPressed(getTime=True)
		if not times in all_times:
			all_buttons.append(buttons)
			all_times.append(times)

# Print results
if MOVE_TEST:
	for i in range(len(pos)):
		print(i, times[i], pos[i])
elif CLICK_TEST:
	for i in range(len(all_times)):
		print(all_buttons[i], all_times[i])