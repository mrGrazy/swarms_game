def update_collisions(qtree, objects):
  qtree.clear()
  qtree.insert(objects)

  for obj in objects:
    for item in qtree.retrieve(obj):
      if obj is item:
        continue

      if obj.colliding and item.colliding:
        continue

      colliding = _collision_test(obj, item)

      if not obj.colliding:
        obj.colliding = colliding

      if not item.colliding:
        item.colliding = colliding

def _collision_test(a, b):
  if abs(a.x - b.x) - 20 > 0:
    return False
  if abs(a.y - b.y) - 20 > 0:
    return False

  return True

def _abs(i):
  return -i if i < 0 else i

