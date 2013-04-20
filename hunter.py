import pygame.draw

class Hunter:
  
  def __init__(self):
    self.x = 300
    self.y = 300


  def update(self, delta_time):
    return

  def draw(self, surface):
    pygame.draw.circle(surface, (0,0,0), (self.x, self.y), 10, 1)