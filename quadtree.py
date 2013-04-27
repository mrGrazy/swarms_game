# "inspired" by Mike Chambers' JavaScript implementation
# https://github.com/mikechambers/

from pygame import Rect

class QuadTree:

  # bounds    Rect (x, y, width, height)
  # pointQuad Whether the QuadTree will contain points (true), or items with bounds 
  #           (width / height)(false). Default value is false.
  def __init__(self, bounds, pointQuad=False, maxDepth=4, maxChildren=4):
    if not pointQuad:
      self.root = BoundsNode(bounds, 0, maxDepth, maxChildren)
    else:
      self.root = Node(bounds, 0, maxDepth, maxChildren)

  # Object|Array item The item or Array of items to be inserted into the QuadTree. The item should expose x, y 
  #              properties that represents its position in 2D space.
  def insert(self, item):
    if type(item) is list:
      for i in item:
        self.root.insert(i.rect if hasattr(i, 'rect') else i)
    else:
      self.root.insert(item.rect if hasattr(item, 'rect') else item)

  def clear(self):
    self.root.clear()

  # Retrieves all items / points in the same node as the specified item / point. If the specified item
  # overlaps the bounds of a node, then all children in both nodes will be returned.
  # Object item An object representing a 2D coordinate point (with x, y properties), or a shape
  #             with dimensions (x, y, width, height) properties.
  def retrieve(self, item):
    # take a slice
    return self.root.retrieve(item)[:]


class Node(object):
  TOP_LEFT = 0
  TOP_RIGHT = 1
  BOTTOM_LEFT = 2
  BOTTOM_RIGHT = 3

  def __init__(self, bounds, depth=0, maxDepth=4, maxChildren=4):
    self._bounds = bounds
    self.children = []
    self.nodes = {}

    self._maxChildren = maxChildren
    self._maxDepth = maxDepth
    self._depth = depth

  def insert(self, item):
    if len(self.nodes):
      index = self._findIndex(item)
      self.nodes[index].insert(item)
      return

    self.children.append(item)

    if self._depth < self._maxDepth and len(self.children) > self._maxChildren:
      self.subdivide()

      for child in self.children:
        self.insert(child)

      del self.children[:]

  def retrieve(self, item):
    if len(self.nodes):
      index = self._findIndex(item)
      return self.nodes[index].retrieve(item)

    return self.children

  def _findIndex(self, item):
    b = self._bounds
    left = False if item.x > b.x + b.width / 2 else True
    top = False if item.y > b.y + b.height / 2 else True

    if left:
      if top:
        return Node.TOP_LEFT
      else:
        return Node.BOTTOM_LEFT
    else:
      if top:
        return Node.TOP_RIGHT
      else:
        return Node.BOTTOM_RIGHT

  def subdivide(self):
    depth = self._depth + 1

    bx = self._bounds.x
    by = self._bounds.y

    # floor the values
    b_w_h = (self._bounds.width / 2)|0
    b_h_h = (self._bounds.height / 2)|0
    bx_b_w_h = bx + b_w_h
    by_b_h_h = by + b_h_h

    self.nodes[Node.TOP_LEFT] = Node(Rect(bx, by, b_w_h, b_h_h), depth)
    self.nodes[Node.TOP_RIGHT] = Node(Rect(bx_b_w_h, by, b_w_h, b_h_h), depth)
    self.nodes[Node.BOTTOM_LEFT] = Node(Rect(bx, by_b_h_h, b_w_h, b_h_h), depth)
    self.nodes[Node.BOTTOM_RIGHT] = Node(Rect(bx_b_w_h, by_b_h_h, b_w_h, b_h_h), depth)

  def clear(self):
    del self.children[:]

    for node in self.nodes:
      self.nodes[node].clear()

    self.nodes.clear()


class BoundsNode(Node):

  def __init__(self, bounds, depth=0, maxChildren=4, maxDepth=4):
    super(BoundsNode, self).__init__(bounds, depth, maxChildren, maxDepth)
    self._stuckChildren = []
    self._out = []

  def insert(self, item):
    if len(self.nodes):
      index = self._findIndex(item)
      node = self.nodes[index]

      if (item.x >= node._bounds.x and
        item.x + item.width <= node._bounds.x + node._bounds.width and
        item.y >= node._bounds.y and
        item.y + item.height <= node._bounds.y + node._bounds.height):
        self.nodes[index].insert(item)
      else:
        self._stuckChildren.append(item)
      return

    self.children.append(item)

    if self._depth < self._maxDepth and len(self.children) > self._maxChildren:
      self.subdivide()

      for child in self.children:
        self.insert(child)

      del self.children[:]

  def getChildren(self):
    return self.children + self._stuckChildren

  def retrieve(self, item):
    out = self._out
    del out[:]
    if len(self.nodes):
      index = self._findIndex(item)
      out.extend(self.nodes[index].retrieve(item))

    out.extend(self._stuckChildren)
    out.extend(self.children)
    return out

  def clear(self):
    del self._stuckChildren[:]
    del self.children[:]

    if not len(self.nodes):
      return

    for node in self.nodes:
      self.nodes[node].clear()

    self.nodes.clear()

def draw_qtree(surface, qtree):
  surface.set_line_width(1)
  surface.set_source_rgb(0, 0, 0)

  draw_node(surface, qtree.root)
  surface.stroke()

def draw_node(surface, node):
  bounds = node._bounds


  surface.move_to(bounds.x, bounds.y)
  surface.line_to(bounds.x + bounds.width, bounds.y)
  surface.line_to(bounds.x + bounds.width, bounds.y + bounds.height)
  surface.line_to(bounds.x, bounds.y + bounds.height)
  surface.line_to(bounds.x, bounds.y)

#  pygame.draw.rect(
#    abs(bounds.x)  + 0.5,
#    abs(bounds.y) + 0.5,
#    bounds.width,
#    bounds.height
#  )

  for i in node.nodes:
    draw_node(surface, node.nodes[i])

