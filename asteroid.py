import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vectorOne = self.position.rotate(random_angle)
            vectorTwo = self.position.rotate(-random_angle)

            newRadius = self.radius - ASTEROID_MIN_RADIUS

            newAsteroidOne = Asteroid(self.position.x,self.position.y,newRadius)
            newAsteroidTwo = Asteroid(self.position.x,self.position.y,newRadius)

            newAsteroidOne.velocity = vectorOne * 1.2
            newAsteroidTwo.velocity = vectorTwo
