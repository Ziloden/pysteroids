import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # General Groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    
    # Specific Groups
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add Classes to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Create Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game clock
    game_clock = pygame.time.Clock()
    dt = 0

    # Create Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create Asteroid Field
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(SCREEN_COLOR)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print(GAME_OVER_TEXT)
                exit(0)
        for game_object in drawable:
            game_object.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(TICK_DELAY) / 1000


if __name__ == "__main__":
    main()
