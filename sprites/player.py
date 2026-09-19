import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

         pygame.draw.rect(
            self.image,
            (50, 50, 50),
            (20, 20, 24, 35)
        )

        pygame.draw.circle(
            self.image,
            (255, 200, 150),
            (32, 15),
            12
        )

        pygame.draw.rect(
            self.image,
            (100, 100, 100),
            (42, 27, 18, 6)
        )

        self.rect = self.image.get_rect(center=(640, 360))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5

        if keys[pygame.K_s]:
            self.rect.y += 5

        if keys[pygame.K_a]:
            self.rect.x -= 5

        if keys[pygame.K_d]:
            self.rect.x += 5
