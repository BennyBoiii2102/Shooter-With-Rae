import pygame
import Loop
import main_functions as func

def WindowInit():
    running = True
    func.init("display")
    func.init("time")
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Shooter Game Made With Rae Heedick')
    clock = pygame.time.Clock()


def MainLoop():
    while True:
        quit = Loop.Game()

        if quit == True:
            break


WindowInit()
MainLoop()
