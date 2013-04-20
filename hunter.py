import pygame.draw
from pygame.math import Vector2

class Hunter:
  
  def __init__(self):
    self.pos = Vector2(0,0)
    self.velo = Vector2(0.1,0.1)


  def update(self, delta_time):
    #self.pos = self.pos + self.velo
    pass

  def draw(self, surface):
    surface.set_source_rgb(0, 0, 0)
    surface.translate(self.pos.x, self.pos.y)
    surface.rectangle(-5,-5,10,10)
    surface.stroke()