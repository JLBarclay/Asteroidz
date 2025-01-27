import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("Black")
        player.draw(screen)

        #Refresh screen
        pygame.display.flip()

        #Pause refresh for 1/60th of a second and return delta time in seconds
        dt = gameClock.tick(60) / 1000


if __name__ == "__main__":
    main()