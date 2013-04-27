from player import Player
from hunter import *
#from quadtree import QuadTree, draw_qtree
from collision import update_collisions

class World:

  def __init__(self, rect):
    self.objects = []
    self.objects.append(Player())
    for i in range(100):
      self.objects.append(Hunter())

    self.qtree = QuadTree(rect, maxDepth=8)
    self.qtree.insert(self.objects)

  def update(self, delta_time):
    for obj in self.objects:
      obj.update(delta_time)

    update_collisions(self.qtree, self.objects)

  def draw(self, canvas):
    canvas.set_source_rgb(1, 1, 1)
    canvas.paint()

    draw_qtree(canvas, self.qtree)

    for obj in self.objects:
      mtx = canvas.get_matrix()
      obj.draw(canvas)
      canvas.set_matrix(mtx)

