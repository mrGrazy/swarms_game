import pygame.draw as draw
import pygame.key as key

class Player:

  def __init__(self):
    self.color = (127, 127, 255)
    self.pos = (0, 0)
    self.radius = 8
    self.width = 3

  def update(self, dt):
    return

  def draw(self, surface):
    draw.circle(surface, self.color, self.pos, self.radius, self.width)

