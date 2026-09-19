import pygame
import Loop
import main_functions as func
from gui.windowinit import WindowInit as winit 

def MainLoop():
    while True:
        quit = Loop.Game()

        if quit == False:
            break


screen, clock, background, font, text = winit()
MainLoop()
