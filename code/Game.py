import pygame

from code.Const import W_WIDTH, W_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH , W_HEIGHT))


    def run (self, ):
        menu = Menu(self.window)
        menu_return = menu.run()
        pass
