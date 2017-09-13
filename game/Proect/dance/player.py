import pygame
from angel import Angel


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('devil.png')
        # self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())
        self.resting = False
        self.dy = 0

    def update(self, dt, game):
        last = self.rect.copy()
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
             self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
             self.rect.x += 300 * dt
        # if key[pygame.K_UP]:
        #      self.rect.y -= 300 * dt
        # if key[pygame.K_DOWN]:
        #      self.rect.y += 300 * dt

        if self.resting and key[pygame.K_SPACE]:
            self.dy = -300
        self.dy = min(300, self.dy+17)
        
        self.rect.y += self.dy * dt 

        new = self.rect
        self.resting = False
        # check if we colide whit walls if we colide, reset to last position
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom >cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0 
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0

        for cell in pygame.sprite.spritecollide(self, game.angel, True):
            how = len(game.angel.sprites())
            if how == 0:
                game.counter += 1
                if game.counter % 8 == 0:
                    if game.spawn_time != 0.3:
                        print("Djoka")
                        game.spawn_time -= 0.1


        for cell in pygame.sprite.spritecollide(self, game.anvil, False):
            game.game_run = 0

        if self.rect.y > 480:
            game.game_run = 0