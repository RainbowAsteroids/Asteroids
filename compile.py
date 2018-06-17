"""This file is for freezing your edited source code for when you edit it"""
import cx_Freeze # For freezing the source code

executables = [cx_Freeze.Executable("asteroids.py")] # Tells cx_Freeze to freeze that file.

cx_Freeze.setup(
	name="Asteroids", # Meta data
	options={
		"build_exe":{"packages":["pygame", "random", "time"],  # Adds in some important modules
		"include_files":["ship.png","Tetris.mp3", "death.mp3", "sans.mp3","font.otf"] # Includes important files (e.g. songs, sprites, fonts)
	}},
	description = "Asteroids Game", # Meta Data
	executables = executables
)
