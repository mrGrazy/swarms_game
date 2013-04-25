import pygame.key
from pygame.locals import *
from vector2d import Vec2d

class Player:

  def __init__(self):
    self.position = Vec2d(0, 0)
    self.facing = 0
    self.speed = 0
    self.rot_speed = 0
    self.radius = 8
    self.width = 3

  def update(self, dt):
    pressed = pygame.key.get_pressed()

    # set speeds based on input
    if pressed[pygame.K_LEFT]:
      self.rot_speed = -4
    elif pressed[pygame.K_RIGHT]:
      self.rot_speed = 4
    else:
      self.rot_speed = 0

    if pressed[pygame.K_UP]:
      self.speed = 100
    elif pressed[pygame.K_DOWN]:
      self.speed = -100
    else:
      self.speed = 0

    # update rotation
    self.facing += self.rot_speed * dt

    # update velocity  
    self.velocity = Vec2d(0, self.speed * dt)
    self.velocity.angle = self.facing

    # update position
    self.position += self.velocity

  def draw(self, surface):
    surface.translate(self.position.x, self.position.y)
    surface.rotate(self.facing)
    surface.set_line_width(1.5)
    surface.move_to(10,0)
    surface.line_to(-10,5)
    surface.line_to(-10,-5)
    surface.line_to(10,0)
    surface.set_source_rgb(0, 127, 127)
    surface.stroke()

