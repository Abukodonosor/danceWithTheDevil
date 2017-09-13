import pygame
import random 


class Angel(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Angel, self).__init__(*groups)
        self.image = pygame.image.load('angel.png')
        self.rand_x = random.randrange(50, 550)
        self.rand_y = random.randrange(50,150)
        self.rect = pygame.rect.Rect((self.rand_x,self.rand_y),self.image.get_size())
        self.dy = 0

    def update(self, dt, game):

        self.dy = min(60, self.dy+17)
        self.rect.y += self.dy * dt 
        
        for cell in pygame.sprite.spritecollide(self, game.walls, True):
            self.make_new = 1
            game.angel.empty()
        
        if self.rect.y > 440 and self.make_new == 0:
           self.make_new = 1
           game.angel.empty()
           