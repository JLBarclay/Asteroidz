import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    groupUpdate = pygame.sprite.Group()
    groupDraw = pygame.sprite.Group()
    groupAsteroids = pygame.sprite.Group()

    Player.containers = (groupUpdate, groupDraw)
    Asteroid.containers = (groupAsteroids, groupUpdate, groupDraw)
    AsteroidField.containers = (groupUpdate)


    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
 



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Fill screen background with black
        screen.fill("Black")


        for object in groupUpdate:
            object.update(dt)

        for object in groupDraw:
            object.draw(screen)

        #Refresh screen
        pygame.display.flip()

        #Pause refresh for 1/60th of a second and return delta time in seconds
        dt = gameClock.tick(60) / 1000


if __name__ == "__main__":
    main()