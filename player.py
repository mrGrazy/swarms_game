import pygame.draw as draw
import pygame.key as key
from pygame.math import Vector2

class Player:

  def __init__(self):
    self.color = (127, 127, 255)
    self.position = Vector2(0, 0)
    self.velocity = Vector2(0, 0)
    self.radius = 8
    self.width = 3

  def update(self, dt):
    if key.get_pressed(key.K_UP):
      self.velocity.scale_to_length(1)
    elif key.get_pressed(K_DOWN):
      self.velocity.scale_to_length(-1)
    else:
      self.velocity *= 0

    if key.get_pressed(K_LEFT):
      self.velocity.rotate_ip(0.15 * dt)
    elif key.get_pressed(K_RIGHT):
      self.velocity.rotate_ip(-0.15 * dt)

    self.position = self.velocity

  def draw(self, surface):
    draw.circle(surface, self.color, self.position, self.radius, self.width)

  def _get_position(self):
    return (int(self.position.x), int(self.position.y))

