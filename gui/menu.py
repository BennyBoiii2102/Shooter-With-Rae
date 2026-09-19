import pygame
import main_functions as func

def MenuDisplay(screen, background, font):
    menu_title = font.render("SHOOTER GAME", True, (255, 255, 255))
    play_text = font.render("PLAY", True, (255, 255, 255))

    title_pos = menu_title.get_rect(center=(640, 250))
    play_pos = play_text.get_rect(center=(640, 400))

    screen.blit(background, (0, 0))
    screen.blit(menu_title, title_pos)
    screen.blit(play_text, play_pos)

    pygame.display.flip()

    return screen, background, font
