import pygame
from circleshape import CircleShape
from constants import (
    SHOT_COLOR,
    SHOT_LINE_WIDTH,
    SHOT_RADIUS
)

class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, SHOT_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt