import pygame

def init(package):
    try:
        # Checks if the attribute exists within Pygame
        module = getattr(pygame, package)
 
        if hasattr(module, 'init') and callable(module.init):
            module.init()
            print(f"Successfully initialized: pygame.{package}")
        else:
            print(f"Note: pygame.{package} is available but does not require initialization.")
 
    except AttributeError:
        # Quite self-explanatory. If pygame doesn't have the attribute called the package, then it won't be able to initialize it.
        print(f"Error: 'pygame' has no sub-module named '{package}'")
    except Exception as e:
        # e being the error message that you would get otherwise
        print(f"Failed to initialize pygame.{package}: {e}")

def ClearScreen(screen, DefaultScreen):
    screen.blit(DefaultScreen, (0, 0))
    screen.display.flip()
