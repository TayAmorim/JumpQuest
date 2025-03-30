from datetime import datetime
import sys

import pygame.image
from pygame import surface, Surface, Rect, KEYDOWN, K_RETURN, K_ESCAPE, K_BACKSPACE
from pygame.font import Font

from code.Const import C_RED, SCORE_POS, C_WHITE_BLUE, C_GREEN_DARK
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def save(self, player_score: int, text_title: str):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.text(50, text_title, C_RED, SCORE_POS['Title'])
            score = player_score
            self.text(25, 'Enter Player name (4 characters):', C_GREEN_DARK, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.text(25, name, C_RED, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.text(48, 'TOP 10 SCORE', C_RED, SCORE_POS['Title'])
        self.text(20, 'NAME ---- SCORE ---- DATE', C_RED, SCORE_POS['Label'])

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i, player_score in enumerate(list_score):
            id_,name,score,date = player_score
            formatted_score = f'{score:03d}'
            self.text(20, f'{name} ---- {formatted_score} ---- {date}', C_GREEN_DARK, SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def text(self, text_size: int, text:str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Gill Sans', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime('%d/%m/%y')
    return f'{current_date}'