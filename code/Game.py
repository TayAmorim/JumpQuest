import pygame

from code.Const import W_WIDTH, W_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH , W_HEIGHT))


    def run (self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                leve_return = level.run()
                if not leve_return:
                    menu = Menu(self.window)
                    menu.run()
                if leve_return:
                    level = Level(self.window, 'Level2', menu_return)
                    leve_return = level.run()
                    if not leve_return:
                        menu = Menu(self.window)
                        menu.run()

