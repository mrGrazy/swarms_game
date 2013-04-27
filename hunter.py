from agent import Agent
from vector2d import Vec2d
import random

class Hunter(Agent):
  
  def __init__(self):
    super(Hunter, self).__init__(pos = Vec2d(random.randint(-200,200),random.randint(-200,200)),
                                 speed = random.randint(30, 70),
                                 rot_speed = random.uniform(-1,1))

  def update(self, delta_time):
    super(Hunter, self).update(delta_time)

    self.facing += self.rot_speed*delta_time
    self.velo = Vec2d(0,self.speed * delta_time)
    self.velo.angle = self.facing
    self.pos = self.pos + self.velo
    #pass

