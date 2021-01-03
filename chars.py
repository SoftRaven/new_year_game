import pygame
import const
import map

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(const.RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0
        self.speedy = 0
        self.speedIncrement = 10

    def update(self, collidable):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -self.speedIncrement
        elif keystate[pygame.K_RIGHT]:
            self.speedx = self.speedIncrement
        elif keystate[pygame.K_UP]:
            self.speedy = -self.speedIncrement
        elif keystate[pygame.K_DOWN]:
            self.speedy = self.speedIncrement

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        collision_list = pygame.sprite.spritecollide(self, collidable, False)
        if collision_list:
            for collided_object in collision_list:
                if isinstance(collided_object, map.Tree):
                    if self.speedx < 0:
                        self.rect.left = collided_object.rect.right
                    elif self.speedx > 0:
                        self.rect.right = collided_object.rect.left
                    elif self.speedy < 0:
                        self.rect.top = collided_object.rect.bottom
                    elif self.speedy > 0:
                        self.rect.bottom = collided_object.rect.top

        if self.rect.right > const.WIDTH:
            self.rect.right = const.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > const.HEIGHT:
            self.rect.bottom = const.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


