
PyPTT
=====
Simple Push-To-Talk script controlling a PulseAudio server

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

Sounds "mute.wav" and "unmute.wav":
Origin of these sounds is the Gajim project:
https://dev.gajim.org/gajim/gajim/
Copyright (C) 2017 Philipp Hörist <philipp AT hoerist.com>
