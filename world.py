#from player import Player
from hunter import *

class World:

  def __init__(self):
    self.objects = []
    #self.objects.append(Player())
    self.objects.append(Hunter())

  def update(self, delta_time):
    for obj in self.objects:
      obj.update(delta_time)

  def draw(self, canvas):
    for obj in self.objects:
      obj.draw(canvas)
