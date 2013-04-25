from player import Player
from hunter import *

class World:

  def __init__(self):
    self.objects = []
    self.objects.append(Player())
    for i in range(100):
      self.objects.append(Hunter())
    
  def update(self, delta_time):
    for obj in self.objects:
      obj.update(delta_time)

  def draw(self, canvas):
    canvas.set_source_rgb(1, 1, 1)
    canvas.paint()

    for obj in self.objects:
      mtx = canvas.get_matrix()
      obj.draw(canvas)
      canvas.set_matrix(mtx)
