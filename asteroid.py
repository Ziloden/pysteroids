import pygame
import random

from circleshape import CircleShape
from constants import (
    ASTEROID_COLOR,
    ASTEROID_KINDS,
    ASTEROID_LINE_WIDTH,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_DESTROYED_ANGLE,
    ASTEROID_MIN_DESTROYED_ANGLE,
    ASTEROID_MAX_SPLIT,
    ASTEROID_MIN_SPLIT,
    ASTEROID_ACCELERATION
)

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, ASTEROID_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        velocity_angle_change = random.uniform(ASTEROID_MIN_DESTROYED_ANGLE, ASTEROID_MAX_DESTROYED_ANGLE)
        velocity_left = self.velocity.rotate(-velocity_angle_change)
        velocity_right = self.velocity.rotate(velocity_angle_change)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroids = []
        
        # For funsises spawn a variable number of asteroids
        # TODO: make their velocity angles variable beyond the 2
        num_spawn = round(random.uniform(ASTEROID_MIN_SPLIT, ASTEROID_MAX_SPLIT))
        for i in range(0, num_spawn):
            asteroids.append(Asteroid(self.position.x, self.position.y, new_radius))
            if i % 2 == 0:
                asteroids[i].velocity = velocity_right * ASTEROID_ACCELERATION
            else:
                asteroids[i].velocity = velocity_left * ASTEROID_ACCELERATION