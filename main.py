import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables,drawables)
    AsteroidField.containers = (updatables,)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatables.update(dt)

        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    


if __name__ == "__main__":
    main()
