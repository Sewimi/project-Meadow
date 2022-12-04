import pygame
import sys
from pygame.locals import *
import world
import menu
import pygame_gui

pygame.init()

WORLD_SIZE = 20


class Game:

    def __init__(self, height,width) -> None:
        self.window_height = height
        self.widow_width = width
        self.screen = pygame.display.set_mode((self.widow_width, self.window_height))
        self.simulation_field = world.World(WORLD_SIZE,self.widow_width,self.window_height)
        self.menu = menu.Menu(self.screen,self)
        self.next_turn = False
        self.auto_play = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.simulation_field.draw(self.screen)
        self.menu.draw()
        pygame.display.flip()
    
    def update(self,dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                self.menu.handle_button_press(event)
            self.menu.manager.process_events(event)
        self.menu.manager.update(dt)

        if self.next_turn == True:
            self.simulation_field.update(dt)
            if self.auto_play == False:
                self.next_turn = False

    def game_loop(self):  
        fps = 10
        fpsClock = pygame.time.Clock() 
        dt = 1/fps 
        while True:
            self.update(dt)
            self.draw()
            dt = fpsClock.tick(fps)


if __name__ == '__main__':
    g=Game(800,1000)
    g.game_loop()

