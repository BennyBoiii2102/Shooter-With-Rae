import pygame
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

    font = pygame.font.SysFont("arial", 36)
    text = font.render("Welcome to our game!", True, (255, 255, 255))
    textpos = text.get_rect()
    textpos.center = background.get_rect().center

    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    return screen, clock, background, font, text
