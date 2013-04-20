import pygame.draw as draw
import pygame.key as key
from vector2d import Vec2d

class Player:

  def __init__(self):
    self.color = (127, 127, 255)
    self.position = Vec2d(0, 0)
    self.velocity = Vec2d(0, 0)
    self.radius = 8
    self.width = 3

  def update(self, dt):
    if key.get_pressed(key.K_UP):
      self.velocity.length = 1
    elif key.get_pressed(K_DOWN):
      self.velocity.length = -1
    else:
      self.velocity *= 0

    if key.get_pressed(K_LEFT):
      self.velocity.rotate_ip(0.15)
    elif key.get_pressed(K_RIGHT):
      self.velocity.rotate_ip(-0.15)

    self.position = self.velocity

  def draw(self, surface):
    surface.rotate(self.velocity.get_angle())
    surface.translate(self.position.x, self.position.y)

    surface.rectangle(-5,-5,10,10)
    surface.set_source_rgb(0, 0, 0)
    surface.stroke()

  def _get_position(self):
    return (int(self.position.x), int(self.position.y))

