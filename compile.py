import cx_Freeze

executables = [cx_Freeze.Executable("asteroids.py")]

cx_Freeze.setup(
	name="Asteroids",
	options={"build_exe":{"packages":["pygame", "random", "time"], "include_files":["ship.png","Tetris.mp3", "death.mp3", "sans.mp3"]}},
	description = "Asteroids Game",
	executables = executables
)
