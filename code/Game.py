import pygame

from code.Const import W_WIDTH, W_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH , W_HEIGHT))

    def run (self, ):
        player_score = 0
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return, player_score)
                player_score = level.run(player_score)
                if player_score:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    player_score = level.run(player_score)
                    if player_score:
                        score.save (player_score, 'YOU WIN!!')

            elif menu_return == MENU_OPTION[1]:
                score.show()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
