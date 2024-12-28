import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updatables, drawables)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for updatable in updatables:
			updatable.update(dt)
		screen.fill(000)
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__=="__main__":
	main()
