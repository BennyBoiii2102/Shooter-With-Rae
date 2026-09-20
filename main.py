import pygame
import game.Loop      as Loop
import main_functions as func
from   gui.windowinit import WindowInit  as winit
from   gui.menu       import MenuDisplay as DispMenu

def MainLoop(screen, background) -> None:
    while True:
        exit, screen, background = Loop.Game(screen, background)
        pygame.display.flip()

        func.ClearScreen(screen, BlankScreen)

        if exit == True:
            break


screen, clock, background, font, BlankScreen = winit()
screen,        background, font              = DispMenu(screen, background, font)
MainLoop(screen, background)
