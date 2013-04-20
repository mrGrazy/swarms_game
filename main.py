import os, sys
import pygame
from pygame.locals import *
from world import *
#import numpy
import cairo
import math

print(pygame.version.ver)

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Swarms')
pygame.mouse.set_visible(1)

pixels = pygame.surfarray.pixels2d(screen)
cairo_surface = cairo.ImageSurface.create_for_data(pixels.data, cairo.FORMAT_RGB24, width, height)

#background = pygame.Surface(screen.get_size())
#background = background.convert()
#background.fill((255, 255, 255))

# if pygame.font:
#   font = pygame.font.Font(None, 36)
#   text = font.render("Hello, World", 1, (10, 10, 10))
#   #textpos = text.get_rect(centerx=background.get_width()/2)
#   #background.blit(text, textpos)

context = cairo.Context(cairo_surface)


world = World()
clock = pygame.time.Clock()

quit = False

while not quit:
  clock.tick()

  world.update(clock.get_time() / 1000.0)

  context = cairo.Context(cairo_surface)
  context.translate(width/2, height/2)
  world.draw(context)

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == QUIT:
      quit = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      quit = True

    #elif event.type == MOUSEBUTTONDOWN:
    #elif event.type == MOUSEBUTTONUP:

del pixels
del cairo_surface
