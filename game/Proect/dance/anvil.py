import pygame
import random


class Anvil(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Anvil, self).__init__(*groups)
        self.image = pygame.image.load('anvil1.png')
        self.rand_x = random.randrange(50, 550)
        self.rand_y = random.randrange(50, 70)
        self.rect = pygame.rect.Rect((self.rand_x, self.rand_y), self.image.get_size())
        self.dy = 0

    def update(self, dt, game):
        self.dy = min(80, self.dy + 34)
        self.rect.y += self.dy * dt


        if game.new_anvil == 0 and game.time_dt > game.spawn_time:
            game.new_anvil = 1

        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.kill()



