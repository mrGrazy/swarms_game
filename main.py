import os, sys
import pygame
from pygame.locals import *
from world import *
import numpy
from PIL import Image
import cairo
import math

def bgra_surf_to_rgba_string(cairo_surface):
    # We use PIL to do this
    img = Image.frombuffer(
        'RGBA', (cairo_surface.get_width(),
                 cairo_surface.get_height()),
        cairo_surface.get_data(), 'raw', 'BGRA', 0, 1)
 
    return img.tostring('raw', 'RGBA', 0, 1)

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
print(pygame.display.Info())
pygame.display.set_caption('Swarms')
pygame.mouse.set_visible(1)

pixels = numpy.empty(width * height * 4, dtype=numpy.int8)
cairo_surface = cairo.ImageSurface.create_for_data(pixels, cairo.FORMAT_RGB24, width, height, width*4)

context = cairo.Context(cairo_surface)


w_rect = Rect(screen.get_rect())
w_rect.x -= w_rect.width/2
w_rect.y -= w_rect.height/2


world = World(w_rect)
clock = pygame.time.Clock()

quit = False

while not quit:
  clock.tick()

  world.update(clock.get_time() / 1000.0)

  context = cairo.Context(cairo_surface)
  matrix = context.get_matrix()

  context.translate(width/2, height/2)
  world.draw(context)

  context.set_matrix(matrix)

  context.set_font_size(12); 
  context.set_source_rgb(0,0,0)
  context.select_font_face("Courier");
  context.move_to(2,12)
  context.show_text("fps: " + str(round(clock.get_fps(),2)))

  data_string = bgra_surf_to_rgba_string(cairo_surface)
  pygame_surface = pygame.image.frombuffer(data_string, (width, height), 'RGBA')

  screen.blit(pygame_surface, (0,0))
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
