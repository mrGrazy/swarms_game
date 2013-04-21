import pygame.draw
from vector2d import Vec2d
import math
import random

class Hunter:
  
  def __init__(self):
    self.pos = Vec2d(random.randint(-200,200),random.randint(-200,200))
    self.facing = 0
    self.speed = 50
    self.rot_speed = random.uniform(-1,1)

  def update(self, delta_time):
    self.facing += self.rot_speed*delta_time
    self.velo = Vec2d(0,self.speed * delta_time)
    self.velo.angle = self.facing
    self.pos = self.pos + self.velo

  def draw(self, surface):
    surface.translate(self.pos.x, self.pos.y)
    surface.rotate(self.facing)
    surface.set_line_width(1.5)
    surface.move_to(10,0)
    surface.line_to(-10,5)
    surface.line_to(-10,-5)
    surface.line_to(10,0)
    surface.set_source_rgb(255, 0, 0)
    surface.stroke()
    