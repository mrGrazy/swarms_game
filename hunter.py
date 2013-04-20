import pygame.draw
from vector2d import Vec2d
import math

class Hunter:
  
  def __init__(self):
    self.pos = Vec2d(0,0)
    self.facing = 0
    self.speed = 1


  def update(self, delta_time):
    #self.facing += 0.1*delta_time
    self.velo = Vec2d(1,1)
    self.velo.length = self.speed * delta_time
    self.velo.angle = self.facing
    self.pos = self.pos + self.velo
    pass

  def draw(self, surface):
    surface.translate(self.pos.x, self.pos.y)
    surface.rotate(self.facing)
    surface.move_to(10,0)
    surface.line_to(-10,5)
    surface.line_to(-10,-5)
    surface.line_to(10,0)
    surface.set_source_rgb(0, 0, 0)
    surface.stroke()

    surface.select_font_face("Courier");

    surface.set_font_size(60);

    surface.show_text(str(self.velo))