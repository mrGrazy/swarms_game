import os, sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Swarms')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

if pygame.font:
  font = pygame.font.Font(None, 36)
  text = font.render("Hello, World", 1, (10, 10, 10))
  textpos = text.get_rect(centerx=background.get_width()/2)
  background.blit(text, textpos)

quit = False

while not quit:

  for event in pygame.event.get():
    if event.type == QUIT:
      quit = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      quit = True

    #elif event.type == MOUSEBUTTONDOWN:
    #elif event.type == MOUSEBUTTONUP:

