import pygame
import random
from time import sleep as wait

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
dRed = (190, 0, 0)
green = (0, 255, 0)
dGreen = (0, 190, 0)
grey = (100,100,100)
yellow = (255, 255, 0)
dYellow = (190, 190, 0)

FPS = 25
clock = pygame.time.Clock()

width, height = 800,600

pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
screen = gameDisplay
pygame.display.set_caption("Asteroids")

lead_x = 50

lead_y = height/2
move_y = 0

laserExists = False
asterExists = False

laserX, asterX, laserY, asterY = 0,0,0,0

ship = pygame.image.load("ship.png")

pygame.display.set_icon(ship)

font = {
	20:pygame.font.Font("font.otf", 20),
	30:pygame.font.Font("font.otf", 30),
	60:pygame.font.Font("font.otf", 60),
	90:pygame.font.Font("font.otf", 90)
}

def makeLaser(): # Spawns a laser
	global laserX
	global laserY
	global laserExists
	laserX = 80
	laserY = lead_y+10
	laserExists = True

def spawnAsteroid(): # Spawns an asteroid
	global asterX
	global asterY
	global asterExists
	asterX = 750
	asterY = random.randrange(0,height-50)
	asterExists = True

def text_objects(text,color,font):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message(msg, color, pos, size, centered=True): # Displays text
	if centered:
		textSurface, textRect = text_objects(msg, color, font[size])
		textRect.center = pos[0], pos[1]
		gameDisplay.blit(textSurface, textRect)
	else:
		text = font[size].render(msg, True, color)
		gameDisplay.blit(screenText, pos)

scoreFactor = 1

def controls():
	global scoreFactor
	
	exit = (50, 500, 100, 50)
	factor1 = (150, 350, 100, 50)
	factor2 = (350, 350, 100, 50)
	factor5 = (550, 350, 100, 50)
	
	gameDisplay.fill(white)
	message("Controls", red, (width/2, (height/2)-200), 90)
	message("Use the up down arrows to move the ship", black, (width/2, (height/2)-100), 20)
	message("Use the space key to fire the laser", black, (width/2, (height/2)-75), 20)
	message("If the asteroid is hit by the laser, it will be desroyed", black, (width/2, (height/2)-50), 20)
	message("If the asteroid makes it to the cyan line, you will lose.", black, (width/2, (height/2)-25), 20)
	message("You can change the difficulty by increasing the score multiplyer", black, (width/2, (height/2)), 20)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit
				quit()
		if hover(exit):
			pygame.draw.rect(screen,red,exit)
			if pressed(exit):
				gameDisplay.fill(white)
				message("Asteroids!", red, (width/2, (height/2)-200), 90)
				return None
		else: 
			pygame.draw.rect(screen,dRed,exit)
		if hover(factor1):
			pygame.draw.rect(screen,green,factor1)
			if pressed(factor1):
				scoreFactor = 1
		else: 
			if scoreFactor == 1:
				pygame.draw.rect(screen,dGreen,factor1)
			else:
				pygame.draw.rect(screen,grey,factor1)
		
		if hover(factor2):
			pygame.draw.rect(screen,yellow,factor2)
			if pressed(factor2):
				scoreFactor = 2
		else: 
			if scoreFactor == 2:
				pygame.draw.rect(screen,dYellow,factor2)
			else:
				pygame.draw.rect(screen,grey,factor2)
		
		if hover(factor5):
			pygame.draw.rect(screen,red,factor5)
			if pressed(factor5):
				scoreFactor = 5
		else:
			if scoreFactor == 5:
				pygame.draw.rect(screen,dRed,factor5)
			else:
				pygame.draw.rect(screen,grey,factor5)
		
		message("Back", white, (exit[0]+(exit[2]/2), exit[1]+(exit[3]/2)), 30)
		message("1x", white, (factor1[0]+(factor1[2]/2), factor1[1]+(factor1[3]/2)), 30)
		message("2x", white, (factor2[0]+(factor2[2]/2), factor2[1]+(factor2[3]/2)), 30)
		message("5x", white, (factor5[0]+(factor5[2]/2), factor5[1]+(factor5[3]/2)), 30)
		
		pygame.display.update()

def endGame():
	global score
	score = round(score*100)
	end = False
	gameDisplay.fill(white)
	message("You lost!", red, (width/2, (height/2)-200), 90)
	message("Your score is {}".format(str(score-100)), black, (width/2, (height/2)-125), 30)
	pygame.display.update()
	pygame.mixer.music.load("death.mp3")
	pygame.mixer.music.play(-1)
	start = (width/2-250,height/2,500,50)
	home = (width/2-250, height/2+100, 500, 50)
	exit = (width/2-250,height/2+200,500,50)
	
	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		if hover(exit):
			pygame.draw.rect(screen,red,exit)
			if pressed(exit):
				wait(.125)
				pygame.quit()
				quit()
		else: 
			pygame.draw.rect(screen,dRed,exit)
		message("Quit :(", white, (exit[0]+(exit[2]/2), exit[1]+(exit[3]/2)), 30)
		if hover(start):
			pygame.draw.rect(screen,green,start)
			if pressed(start):
				pygame.mixer.music.stop()
				pygame.mixer.music.load("Tetris.mp3")
				pygame.mixer.music.play(-1)
				return False
		else: 
			pygame.draw.rect(screen,dGreen,start)
		message("Play Again!", white, (start[0]+(start[2]/2), start[1]+(start[3]/2)), 30)
		if hover(home):
			pygame.draw.rect(screen,yellow,home)
			if pressed(home):
				pygame.mixer.music.stop()
				wait(.125)
				startScreen()
		else: 
			pygame.draw.rect(screen,dYellow,home)
		message("Start Screen", white, (home[0]+(home[2]/2), home[1]+(home[3]/2)), 30)
		pygame.display.update()
		
def hover(pos):
	if pygame.mouse.get_pos()[0] >= pos[0] and pygame.mouse.get_pos()[1] >= pos[1]:
		if pygame.mouse.get_pos()[0] <= pos[0]+pos[2] and pygame.mouse.get_pos()[1] <= pos[1]+pos[3]:
			return True
	return False
	
def pressed(pos):
	if hover(pos):
		if bool(pygame.mouse.get_pressed()[0]):
			return True
	return False

score = 1

def game():	
	global score
	global laserExists
	global asterExists
	global lead_x
	global lead_y
	global laserX
	global laserY
	global asterX
	global asterY
	global move_y
	
	pygame.mixer.music.load("Tetris.mp3")
	pygame.mixer.music.play(-1)
	while True: # Main game loop
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, (0,255,255), (90, 0, 20, 600))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					move_y = -20
				elif event.key == pygame.K_DOWN:
					move_y = 20
				if event.key == pygame.K_SPACE:
					makeLaser()
				#if event.key == pygame.K_a:
				#	spawnAsteroid()
			elif event.type == pygame.KEYUP:
				if not event.key == pygame.K_SPACE:
					move_x = 0
					move_y = 0
		
		if laserExists:
			laserX += 50
			pygame.draw.rect(gameDisplay, red, (laserX, laserY, 30, 10))
		
		if asterExists:
			asterX -= 10*score
			pygame.draw.rect(gameDisplay, grey, (asterX, asterY, 50, 50))
			if asterX <= 100:
				asterExists = False
				endGame()
				score = 1
		else:
			spawnAsteroid()
		
		if lead_y == 0 and move_y == -20:
			move_y = 0
		if lead_y >= 560 and move_y == 20:
			move_y = 0
		lead_y += move_y
		
		if laserX+30 >= asterX and asterY in range(int(laserY-50), int(laserY+50)):
			asterExists, laserExists = False, False
			score += .01*scoreFactor
		
		gameDisplay.blit(ship, (lead_x, lead_y))
		pygame.display.update()
		clock.tick(FPS)

def startScreen():
	pygame.mixer.music.load("sans.mp3")
	pygame.mixer.music.play(-1)
	gameDisplay.fill(white)
	start = (width/2-250,height/2,500,50)
	exit = (width/2-250,height/2+200,500,50)
	info = (width/2-250,height/2+100,500,50)
	#pygame.draw.rect(screen,black,(395,295,10,10)) #middle
	
	message("Asteroids!", red, (width/2, (height/2)-200), 90)
	pygame.display.update()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();
				quit()
		if hover(exit):
			pygame.draw.rect(screen,red,exit)
			if pressed(exit):
				pygame.quit()
				quit()
		else: 
				pygame.draw.rect(screen,dRed,exit)
		message("Quit :(", white, (exit[0]+(exit[2]/2), exit[1]+(exit[3]/2)), 30)
		if hover(start):
			pygame.draw.rect(screen,green,start)
			if pressed(start):
				game()
		else: 
			pygame.draw.rect(screen,dGreen,start)
		message("Play!", white, (start[0]+(start[2]/2), start[1]+(start[3]/2)), 30)
		if hover(info):
			pygame.draw.rect(screen,yellow,info)
			if pressed(info):
				controls()
		else:
			pygame.draw.rect(screen,dYellow,info)
		message("Controls", white, (info[0]+(info[2]/2), info[1]+(info[3]/2)), 30)
		pygame.display.update()

startScreen()
