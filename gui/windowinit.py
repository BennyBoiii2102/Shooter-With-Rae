import pygame
import main_functions as func
from   time           import sleep

def WindowInit():
    running = True
    func.init("display")
    func.init("font")

    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Shooter Game Made With Rae Heedick")
    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((10, 10, 10))

    font = pygame.font.SysFont("arial", 36)

    text = font.render("Welcome to our game!", True, (255, 255, 255))
    textpos = text.get_rect()
    textpos.center = background.get_rect().center

    screen.blit(background, (0, 0))
    screen.blit(text, textpos)
    pygame.display.flip()

    sleep(1)

    for i in range(255, 9, -5):
        text_surface = font.render(
            "Welcome to our game!",
            True,
            (i, i, i)
        )

        screen.blit(background, (0, 0))
        screen.blit(text_surface, textpos)

        pygame.display.flip()
        pygame.time.delay(20)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    return screen, clock, background, font