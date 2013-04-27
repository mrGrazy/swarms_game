import pygame.draw
from pygame import Rect
from vector2d import Vec2d
import math
import random

class Agent(object):
  
  def __init__(self, pos=Vec2d(0,0), facing=0, speed=0, rot_speed=0):
    self.pos = pos
    self.facing = facing
    self.speed = speed
    self.rot_speed = rot_speed
    self.r, self.g, self.b = 255, 0, 0
    self.colliding = False

  @property
  def x(self):
    return self.pos.x

  @property
  def y(self):
    return self.pos.y

  @property
  def width(self):
    return 20

  @property
  def height(self):
    return 20

  @property
  def right(self):
    return self.x + self.width

  @property
  def bottom(self):
    return self.y + self.height

  def update(self, delta_time):
    self.colliding = False

  def draw(self, surface):
    surface.set_line_width(1.5)
    surface.set_source_rgb(self.r, self.g, self.b)

    surface.translate(self.pos.x, self.pos.y)

    if self.colliding:
      surface.move_to(-10, -10)
      surface.line_to(10, -10)
      surface.line_to(10, 10)
      surface.line_to(-10, 10)
      surface.line_to(-10, -10)

    surface.rotate(self.facing)
    surface.move_to(10,0)
    surface.line_to(-10,5)
    surface.line_to(-10,-5)
    surface.line_to(10,0)
    surface.stroke()

