#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Thu Feb 23 02:01:37 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/3x10e8/Documents/GitHub/COGS189Project/stim/Test_experiment_232202_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
Introduction = visual.TextStim(win=win, name='Introduction',
    text='Welcome to our experiment. \n\nPlease sit still and follow the instructions.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
listen_instr = visual.TextStim(win=win, name='listen_instr',
    text='You will listen to a piece of music. \nPlease fixate on the cross while listening.\n\nPress SPACE to continue.\n\nPress ESC at any time to exit.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
key_continue = keyboard.Keyboard()

# --- Initialize components for Routine "Fixate" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.01,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)

# --- Initialize components for Routine "Listening" ---
beat1 = sound.Sound('audio/beat1.wav', secs=-1, stereo=True, hamming=True,
    name='beat1')
beat1.setVolume(1.0)
cue = sound.Sound('audio/metronome.wav', secs=-1, stereo=True, hamming=True,
    name='cue')
cue.setVolume(1.0)
cross_listen = visual.ShapeStim(
    win=win, name='cross_listen', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.01,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "Response_Instr" ---
resp_instr = visual.TextStim(win=win, name='resp_instr',
    text='Next you will listen to the piece again. Please tap along with the music beats by pressing the space key. Be as precise as you can.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_wait = keyboard.Keyboard()

# --- Initialize components for Routine "Response__Listening_" ---
key_resp = keyboard.Keyboard()
cue_resp = sound.Sound('audio/metronome.wav', secs=-1, stereo=True, hamming=True,
    name='cue_resp')
cue_resp.setVolume(1.0)
cross_resp = visual.ShapeStim(
    win=win, name='cross_resp', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.01,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
beat1_resp = sound.Sound('audio/beat1.wav', secs=-1, stereo=True, hamming=True,
    name='beat1_resp')
beat1_resp.setVolume(1.0)

# --- Initialize components for Routine "Imag_Instr" ---
imag_instr = visual.TextStim(win=win, name='imag_instr',
    text='Next, you will imagine the previous piece in your mind. Please tap along with the music beats that you are imagining by pressing the SPACE key. Be as precise as you can. \n\nPlease start after the metronome. \n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_cont_i = keyboard.Keyboard()

# --- Initialize components for Routine "Response_Imagining" ---
key_resp_i = keyboard.Keyboard()
cue_resp_i = sound.Sound('audio/metronome.wav', secs=-1, stereo=True, hamming=True,
    name='cue_resp_i')
cue_resp_i.setVolume(1.0)
cross_imag = visual.ShapeStim(
    win=win, name='cross_imag', vertices='cross',
    size=(0.01, 0.01),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.01,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "End" ---
Ending = visual.TextStim(win=win, name='Ending',
    text='This is the end of the experiment. Thank you. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_continue.keys = []
key_continue.rt = []
_key_continue_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Introduction, listen_instr, key_continue]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Introduction* updates
    if Introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Introduction.frameNStart = frameN  # exact frame index
        Introduction.tStart = t  # local t and not account for scr refresh
        Introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Introduction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Introduction.started')
        Introduction.setAutoDraw(True)
    if Introduction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Introduction.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            Introduction.tStop = t  # not accounting for scr refresh
            Introduction.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Introduction.stopped')
            Introduction.setAutoDraw(False)
    
    # *listen_instr* updates
    if listen_instr.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        listen_instr.frameNStart = frameN  # exact frame index
        listen_instr.tStart = t  # local t and not account for scr refresh
        listen_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(listen_instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'listen_instr.started')
        listen_instr.setAutoDraw(True)
    
    # *key_continue* updates
    waitOnFlip = False
    if key_continue.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_continue.frameNStart = frameN  # exact frame index
        key_continue.tStart = t  # local t and not account for scr refresh
        key_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_continue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_continue.started')
        key_continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_continue.status == STARTED and not waitOnFlip:
        theseKeys = key_continue.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_continue_allKeys.extend(theseKeys)
        if len(_key_continue_allKeys):
            key_continue.keys = _key_continue_allKeys[-1].name  # just the last key pressed
            key_continue.rt = _key_continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_continue.keys in ['', [], None]:  # No response was made
    key_continue.keys = None
thisExp.addData('key_continue.keys',key_continue.keys)
if key_continue.keys != None:  # we had a response
    thisExp.addData('key_continue.rt', key_continue.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Fixate" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
FixateComponents = [cross]
for thisComponent in FixateComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Fixate" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cross* updates
    if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross.frameNStart = frameN  # exact frame index
        cross.tStart = t  # local t and not account for scr refresh
        cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cross.started')
        cross.setAutoDraw(True)
    if cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            cross.tStop = t  # not accounting for scr refresh
            cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.stopped')
            cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Fixate" ---
for thisComponent in FixateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Listening" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
beat1.setSound('audio/beat1.wav', secs=8, hamming=True)
beat1.setVolume(1.0, log=False)
cue.setSound('audio/metronome.wav', secs=4, hamming=True)
cue.setVolume(1.0, log=False)
# keep track of which components have finished
ListeningComponents = [beat1, cue, cross_listen]
for thisComponent in ListeningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Listening" ---
while continueRoutine and routineTimer.getTime() < 12.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop beat1
    if beat1.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        beat1.frameNStart = frameN  # exact frame index
        beat1.tStart = t  # local t and not account for scr refresh
        beat1.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('beat1.started', tThisFlipGlobal)
        beat1.play(when=win)  # sync with win flip
    if beat1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > beat1.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            beat1.tStop = t  # not accounting for scr refresh
            beat1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'beat1.stopped')
            beat1.stop()
    # start/stop cue
    if cue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cue.frameNStart = frameN  # exact frame index
        cue.tStart = t  # local t and not account for scr refresh
        cue.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('cue.started', tThisFlipGlobal)
        cue.play(when=win)  # sync with win flip
    if cue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cue.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            cue.tStop = t  # not accounting for scr refresh
            cue.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue.stopped')
            cue.stop()
    
    # *cross_listen* updates
    if cross_listen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross_listen.frameNStart = frameN  # exact frame index
        cross_listen.tStart = t  # local t and not account for scr refresh
        cross_listen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross_listen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cross_listen.started')
        cross_listen.setAutoDraw(True)
    if cross_listen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross_listen.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            cross_listen.tStop = t  # not accounting for scr refresh
            cross_listen.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_listen.stopped')
            cross_listen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ListeningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Listening" ---
for thisComponent in ListeningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
beat1.stop()  # ensure sound has stopped at end of routine
cue.stop()  # ensure sound has stopped at end of routine
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-12.000000)

# --- Prepare to start Routine "Response_Instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_wait.keys = []
key_wait.rt = []
_key_wait_allKeys = []
# keep track of which components have finished
Response_InstrComponents = [resp_instr, key_wait]
for thisComponent in Response_InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response_Instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resp_instr* updates
    if resp_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_instr.frameNStart = frameN  # exact frame index
        resp_instr.tStart = t  # local t and not account for scr refresh
        resp_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp_instr.started')
        resp_instr.setAutoDraw(True)
    
    # *key_wait* updates
    waitOnFlip = False
    if key_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_wait.frameNStart = frameN  # exact frame index
        key_wait.tStart = t  # local t and not account for scr refresh
        key_wait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_wait, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_wait.started')
        key_wait.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_wait.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_wait.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_wait.status == STARTED and not waitOnFlip:
        theseKeys = key_wait.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_wait_allKeys.extend(theseKeys)
        if len(_key_wait_allKeys):
            key_wait.keys = _key_wait_allKeys[-1].name  # just the last key pressed
            key_wait.rt = _key_wait_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response_InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response_Instr" ---
for thisComponent in Response_InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_wait.keys in ['', [], None]:  # No response was made
    key_wait.keys = None
thisExp.addData('key_wait.keys',key_wait.keys)
if key_wait.keys != None:  # we had a response
    thisExp.addData('key_wait.rt', key_wait.rt)
thisExp.nextEntry()
# the Routine "Response_Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response__Listening_" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
cue_resp.setSound('audio/metronome.wav', secs=4, hamming=True)
cue_resp.setVolume(1.0, log=False)
beat1_resp.setSound('audio/beat1.wav', secs=8, hamming=True)
beat1_resp.setVolume(1.0, log=False)
# keep track of which components have finished
Response__Listening_Components = [key_resp, cue_resp, cross_resp, beat1_resp]
for thisComponent in Response__Listening_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response__Listening_" ---
while continueRoutine and routineTimer.getTime() < 12.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.stopped')
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
    # start/stop cue_resp
    if cue_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cue_resp.frameNStart = frameN  # exact frame index
        cue_resp.tStart = t  # local t and not account for scr refresh
        cue_resp.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('cue_resp.started', tThisFlipGlobal)
        cue_resp.play(when=win)  # sync with win flip
    if cue_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cue_resp.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            cue_resp.tStop = t  # not accounting for scr refresh
            cue_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_resp.stopped')
            cue_resp.stop()
    
    # *cross_resp* updates
    if cross_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross_resp.frameNStart = frameN  # exact frame index
        cross_resp.tStart = t  # local t and not account for scr refresh
        cross_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cross_resp.started')
        cross_resp.setAutoDraw(True)
    if cross_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross_resp.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            cross_resp.tStop = t  # not accounting for scr refresh
            cross_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_resp.stopped')
            cross_resp.setAutoDraw(False)
    # start/stop beat1_resp
    if beat1_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        beat1_resp.frameNStart = frameN  # exact frame index
        beat1_resp.tStart = t  # local t and not account for scr refresh
        beat1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('beat1_resp.started', tThisFlipGlobal)
        beat1_resp.play(when=win)  # sync with win flip
    if beat1_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > beat1_resp.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            beat1_resp.tStop = t  # not accounting for scr refresh
            beat1_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'beat1_resp.stopped')
            beat1_resp.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response__Listening_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response__Listening_" ---
for thisComponent in Response__Listening_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
cue_resp.stop()  # ensure sound has stopped at end of routine
beat1_resp.stop()  # ensure sound has stopped at end of routine
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-12.000000)

# --- Prepare to start Routine "Imag_Instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_cont_i.keys = []
key_cont_i.rt = []
_key_cont_i_allKeys = []
# keep track of which components have finished
Imag_InstrComponents = [imag_instr, key_cont_i]
for thisComponent in Imag_InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Imag_Instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *imag_instr* updates
    if imag_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imag_instr.frameNStart = frameN  # exact frame index
        imag_instr.tStart = t  # local t and not account for scr refresh
        imag_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imag_instr, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'imag_instr.started')
        imag_instr.setAutoDraw(True)
    
    # *key_cont_i* updates
    waitOnFlip = False
    if key_cont_i.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_cont_i.frameNStart = frameN  # exact frame index
        key_cont_i.tStart = t  # local t and not account for scr refresh
        key_cont_i.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_cont_i, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_cont_i.started')
        key_cont_i.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_cont_i.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_cont_i.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_cont_i.status == STARTED and not waitOnFlip:
        theseKeys = key_cont_i.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_cont_i_allKeys.extend(theseKeys)
        if len(_key_cont_i_allKeys):
            key_cont_i.keys = _key_cont_i_allKeys[-1].name  # just the last key pressed
            key_cont_i.rt = _key_cont_i_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Imag_InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Imag_Instr" ---
for thisComponent in Imag_InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_cont_i.keys in ['', [], None]:  # No response was made
    key_cont_i.keys = None
thisExp.addData('key_cont_i.keys',key_cont_i.keys)
if key_cont_i.keys != None:  # we had a response
    thisExp.addData('key_cont_i.rt', key_cont_i.rt)
thisExp.nextEntry()
# the Routine "Imag_Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Response_Imagining" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_i.keys = []
key_resp_i.rt = []
_key_resp_i_allKeys = []
cue_resp_i.setSound('audio/metronome.wav', secs=4, hamming=True)
cue_resp_i.setVolume(1.0, log=False)
# keep track of which components have finished
Response_ImaginingComponents = [key_resp_i, cue_resp_i, cross_imag]
for thisComponent in Response_ImaginingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Response_Imagining" ---
while continueRoutine and routineTimer.getTime() < 12.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_i* updates
    waitOnFlip = False
    if key_resp_i.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_resp_i.frameNStart = frameN  # exact frame index
        key_resp_i.tStart = t  # local t and not account for scr refresh
        key_resp_i.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_i, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_i.started')
        key_resp_i.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_i.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_i.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_i.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_i.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_i.tStop = t  # not accounting for scr refresh
            key_resp_i.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_i.stopped')
            key_resp_i.status = FINISHED
    if key_resp_i.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_i.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_i_allKeys.extend(theseKeys)
        if len(_key_resp_i_allKeys):
            key_resp_i.keys = _key_resp_i_allKeys[-1].name  # just the last key pressed
            key_resp_i.rt = _key_resp_i_allKeys[-1].rt
    # start/stop cue_resp_i
    if cue_resp_i.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cue_resp_i.frameNStart = frameN  # exact frame index
        cue_resp_i.tStart = t  # local t and not account for scr refresh
        cue_resp_i.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('cue_resp_i.started', tThisFlipGlobal)
        cue_resp_i.play(when=win)  # sync with win flip
    if cue_resp_i.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cue_resp_i.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            cue_resp_i.tStop = t  # not accounting for scr refresh
            cue_resp_i.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cue_resp_i.stopped')
            cue_resp_i.stop()
    
    # *cross_imag* updates
    if cross_imag.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cross_imag.frameNStart = frameN  # exact frame index
        cross_imag.tStart = t  # local t and not account for scr refresh
        cross_imag.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cross_imag, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'cross_imag.started')
        cross_imag.setAutoDraw(True)
    if cross_imag.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cross_imag.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            cross_imag.tStop = t  # not accounting for scr refresh
            cross_imag.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross_imag.stopped')
            cross_imag.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Response_ImaginingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Response_Imagining" ---
for thisComponent in Response_ImaginingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_i.keys in ['', [], None]:  # No response was made
    key_resp_i.keys = None
thisExp.addData('key_resp_i.keys',key_resp_i.keys)
if key_resp_i.keys != None:  # we had a response
    thisExp.addData('key_resp_i.rt', key_resp_i.rt)
thisExp.nextEntry()
cue_resp_i.stop()  # ensure sound has stopped at end of routine
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-12.000000)

# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [Ending]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ending* updates
    if Ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ending.frameNStart = frameN  # exact frame index
        Ending.tStart = t  # local t and not account for scr refresh
        Ending.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ending, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Ending.started')
        Ending.setAutoDraw(True)
    if Ending.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Ending.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Ending.tStop = t  # not accounting for scr refresh
            Ending.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ending.stopped')
            Ending.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
