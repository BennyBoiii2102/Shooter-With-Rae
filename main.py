import pygame
import Loop
import main_functions as func

def WindowInit():
    running = True
    func.init("display")
    func.init("font")
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Shooter Game Made With Rae Heedick')
    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((10, 10, 10))

    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to our game!", 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    
    return screen, clock, background


def MainLoop():
    while True:
        quit = Loop.Game()

        if quit == False:
            break


screen, clock, background = WindowInit()
MainLoop()
