import os, sys
import pygame
from pygame.locals import *
from world import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Swarms')
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

if pygame.font:
  font = pygame.font.Font(None, 36)
  text = font.render("Hello, World", 1, (10, 10, 10))
  textpos = text.get_rect(centerx=background.get_width()/2)
  background.blit(text, textpos)

world = World()
clock = pygame.time.Clock()

quit = False

while not quit:
  clock.tick()

  world.update(clock.get_time())

  world.draw(background)

  screen.blit(background, (0,0))
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == QUIT:
      quit = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      quit = True

    #elif event.type == MOUSEBUTTONDOWN:
    #elif event.type == MOUSEBUTTONUP:

