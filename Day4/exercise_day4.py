#!/usr/bin/env python

"""
Python course EBC 2016
Day 4 - Exercise instructions
Lucas Sinclair <lucas.sinclair@me.com>

* Write a program in a file called "exercise_day4.py"
* You have until the start of the next course at 13h00 tomorrow to finish it.
* Once the program is done, upload it in your github repository "python_homework" in a directory named "day4".

#######################################################################################################################################################################






### Each Song object should have these attributes:

* title
The title of the song as a string.

* artist
The artist of the song as a string.

* duration
The title of the song as an integer in seconds.

When creating new Song instances:

-> If the duration of a song is not a number, set it to 0, but issue a warning.
-> If the duration of a song is negative, raise an Exception and stop the program.

### Each Song object should have these methods:

* pretty_duration(self)
Returns a nice string describing the duration. For instance if the duration is 3611, this methods takes no input and returns "01 hours 00 minutes 11 seconds" as a string.

* play(self)
Automatically opens a webpage on your computer with a youtube search for the title.

Once your program is ready the following four lines of code should run without errors. (After you have removed the negative duration song!).
"""
import os
import warnings
import webbrowser

class Song(object):
	""" A class describing songs """

	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		self.duration = duration

		try:
			self.duration = int(duration)
		except:
			warnings.warn("Song duration was not a number - setting to 0")
			self.duration = 0

		if self.duration < 0:
			warnings.warn("Song duration is negative - setting to 0")
			self.duration = 0

	def pretty_duration(self):
		min, sec = divmod(self.duration, 60)
		hr, min = divmod(min, 60)
		return "Song duration is %d:%02d:%02d" % (hr, min, sec)

	def play(self):
		# Open youtube
		url = "https://www.youtube.com/results?search_query=%s%s" % (self.artist.replace(" ", "+"), self.title.replace(" ", "+"))
		webbrowser.open(url)


path = os.environ["HOME"]
music_file = open(path + "/lulu_mix_16.csv", "r")

songs = []

for line in music_file:
	if line.startswith("Name, Artist"): continue	
	title, artist, duration = line.split(",")		
	current_song = Song(title, artist, duration)	
	print current_song.title, current_song.artist, current_song.duration
	songs.append(current_song)						

for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()










