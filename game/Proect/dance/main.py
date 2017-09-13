import pygame
from player import Player
from angel import Angel
from anvil import Anvil
import math


class Game(object):

    def game_intro(self, screen):
        intro = True
        # load image
        background = pygame.image.load("satan.jpg")
        background = pygame.transform.scale(background, (640, 480))
        #message
        myfont = pygame.font.SysFont('Comic Sans MS', 45)
        playFont = pygame.font.SysFont(None, 30)
        textsurface = myfont.render("Dance with the devil !!!", False, (255, 255, 255))
        play = playFont.render("PLAY!", False, (255, 255, 255))

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # close button on the window
                if event.type == pygame.QUIT:
                    return
                # key down presing keydown on keyBord and Escape key
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # mouse coordinates
            mouse = pygame.mouse.get_pos()
            # mouse click options [l,m,r]
            click = pygame.mouse.get_pressed()
            dx = math.fabs(mouse[0] - 320)
            dy = math.fabs(mouse[1] - 240)
            if dx+dy <= 40:
                color = (20, 20, 20)
                if click[0] == 1:
                    self.main(screen)

            else:
                color = (0, 0, 0)

            screen.blit(background, (0, 0))
            screen.blit(textsurface, (100, 20))
            pygame.draw.circle(screen, color, (320, 240), 40)
            screen.blit(play, (290, 230))
            pygame.display.flip()

    def main(self, screen):
        # enemy spawn
        self.time_dt = 0
        self.spawn_time = 0.9
        # game loop:
        self.game_run = 1
        # game clock
        clock = pygame.time.Clock()
        # counter and font
        self.counter = 0
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        # load image
        background = pygame.image.load("h1.jpg")
        # scale background image
        background = pygame.transform.scale(background, (640, 480))
        # new angel idicator
        self.make_new = 0

        # new anvil inicator
        self.new_anvil = 0

        # players sprites
        sprites = pygame.sprite.Group()
        self.player = Player(sprites)

        # angel spiters
        self.angel = pygame.sprite.Group()
        ang = Angel(self.angel)
        sprites.add(self.angel)

        # anvil sprites
        self.anvil = pygame.sprite.Group()
        anvi = Anvil(self.anvil)
        sprites.add(self.anvil)

        # walls
        self.walls = pygame.sprite.Group()
        block = pygame.image.load('block1.png')
        for x in range(0, 640, 32):
            for y in range(0, 480, 32):
                if x in (0, 640-32) or y in (0, 480-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = block
                    wall.rect = pygame.rect.Rect((x,y), block.get_size())
        sprites.add(self.walls)
        self.anvil.add(self.walls)

        # game loop
        while self.game_run:
            # tick 30 times per second (render)
            # time betwine 2 ticks clock.tick()
            dt = clock.tick(30)

            # event handeling
            for event in pygame.event.get():
                # close button on the window
                if event.type == pygame.QUIT:
                    return
                # key down presing keydown on keyBord and Escape key
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            
            # update player and his data
            sprites.update(dt/1000, self)
            # update angel and his data
            ang.update(dt/1000, self)

            self.time_dt += dt/1000

            if self.new_anvil == 1:
                ang = Anvil(self.anvil)
                sprites.add(self.anvil)
                self.new_anvil = 0
                self.time_dt = 0

            if len(self.angel.sprites()) == 0 or self.make_new == 1:
                ang = Angel(self.angel)
                sprites.add(self.angel)
                self.make_new = 0



            textsurface = myfont.render(str(self.counter), False, (255, 255, 255))
            # farbamo pozadinu
            # screen.fill((0,0,0))
            # screen.blit(image,(320,240))
            screen.blit(background, (0, 0))
            screen.blit(textsurface, (50, 50))
            sprites.draw(screen)
            # update the display - display screen buffer
            pygame.display.flip() 


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.mixer.music.load('D - Devils - Dance With The Devil.mp3')
    pygame.mixer.music.play(-1)
    Game().game_intro(screen)
