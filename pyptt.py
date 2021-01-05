#!/usr/bin/python3

""" Simple Push-To-Talk script controlling a PulseAudio server

Dependencies:
- pynput (install using PIP)
- PulseAudio and "pactl" command on the path

Setup:
- set PTT_KEY to the key that should control Push-To-Talk
- set SOURCES to a list of PulseAudio source names that should be muted/unmuted (find out using pactl list sources)

Copyright (C) 2021 Moritz Blei <orwell(ät)bleipb.de>
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
For a copy of the GNU General Public License, see <http://www.gnu.org/licenses/>.
"""

from pynput import keyboard
import os
from queue import Queue

PTT_KEY = keyboard.Key.ctrl_r
SOURCES = ["alsa_input.pci-0000_00_1f.3.analog-stereo"]


# upload tone samples to PA
os.system("pactl upload-sample mute.wav pyptt-mute")
os.system("pactl upload-sample unmute.wav pyptt-unmute")


lastState = False
queue = Queue()

def on_press(key):
	if key == PTT_KEY:
		#print('PTT key {0} pressed'.format(key))
		queue.put(True)

def on_release(key):
	if key == PTT_KEY:
		#print('PTT key {0} released'.format(key))
		queue.put(False)

def mute():
	for src in SOURCES:
		os.system("pactl set-source-mute "+src+" 1")
	#os.system("notify-send -t 500 'PTT: muted'")
	os.system("pactl play-sample pyptt-mute")

def unmute():
	#os.system("notify-send -t 500 'PTT: unmuted'")
	os.system("pactl play-sample pyptt-unmute")
	for src in SOURCES:
		os.system("pactl set-source-mute "+src+" 0")

listener = keyboard.Listener(
	on_press=on_press,
	on_release=on_release)
listener.start()

print("Listener is running. Press Ctrl-C to terminate")

try:
	mute()
	while True:
		state = queue.get()
		if state!=lastState:
			if state:
				unmute()
			else:
				mute()
		lastState = state
except KeyboardInterrupt:
	print("Ctrl-C pressed")

listener.stop()
unmute()
print("Exiting...")
