import pygame.draw
from vector2d import Vec2d

class Hunter:
  
  def __init__(self):
    self.pos = Vec2d(0,0)
    self.facing = 1
    self.speed = 0.1


  def update(self, delta_time):
    velo = Vec2d(1,1)
    velo.length = self.speed
    velo.angle = self.facing
    self.pos = self.pos + (self.velo * delta_time)
    pass

  def draw(self, surface):
    surface.translate(self.pos.x, self.pos.y)
    surface.rotate(self.velo.get_angle())
    surface.rectangle(-5,-5,10,10)
    surface.set_source_rgb(0, 0, 0)
    surface.stroke()