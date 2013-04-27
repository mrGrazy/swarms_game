import pygame.key
from pygame.locals import *
from agent import Agent
from vector2d import Vec2d

class Player(Agent):

  def __init__(self):
    super(Player, self).__init__(speed = 0, rot_speed = 0)
    self.r, self.g, self.b = 0, 127, 127

  def update(self, dt):
    super(Player, self).update(dt)

    pressed = pygame.key.get_pressed()

    if pressed[K_r]:
      self.pos = Vec2d(0, 0)
      return

    # set speeds based on input
    if pressed[pygame.K_LEFT]:
      self.rot_speed = -4
    elif pressed[pygame.K_RIGHT]:
      self.rot_speed = 4
    else:
      self.rot_speed = 0

    if pressed[pygame.K_UP]:
      self.speed = 100
    elif pressed[pygame.K_DOWN]:
      self.speed = -100
    else:
      self.speed = 0

    # update rotation
    self.facing += self.rot_speed * dt

    # update velocity  
    self.velocity = Vec2d(0, self.speed * dt)
    self.velocity.angle = self.facing

    # update position
    self.pos += self.velocity

