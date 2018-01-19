# log.py

# Authors: Iker García Ferrero and Eritz Yerga

from sys import stdout
global log_file
log_file = []

def openlog():
	global log_file
	log_file = open("log.txt", "w")

def output(string):
	global log_file
	log_file.write(string)
	stdout.write(string)

def log(string):
	global log_file
	log_file.write(string)

def closelog():
	global log_file
	log_file.close()