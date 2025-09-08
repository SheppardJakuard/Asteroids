import pygame, random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x,y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen , "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(split_angle)
            vector2 = self.velocity.rotate(-split_angle)
            new_radius= self.radius - ASTEROID_MIN_RADIUS
            self.spawn_a(new_radius,self.position, vector1)
            self.spawn_a(new_radius,self.position,vector2)
       
    def spawn_a(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity