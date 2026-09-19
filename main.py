import pygame
import game.Loop as Loop
import main_functions as func
from gui.windowinit import WindowInit as winit 
from gui.menu import MenuDisplay as dispMenu

def MainLoop(screen, background):
    while True:
        exit, screen, background = Loop.Game(screen, background)
        pygame.display.flip()

        if exit == True:
            break


screen, clock, background, font = winit()
screen, background, font = dispMenu(screen, background, font)
MainLoop(screen, background)
