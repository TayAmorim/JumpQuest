import random
import sys

import pygame.mixer_music
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION, EVENT_OBSTACLE, SPAWN_TIME, C_RED, W_HEIGHT, W_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.build_entity(self.name + 'Bg'))
        self.obstacle_spacing = 0

        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == EVENT_OBSTACLE:
                    choice = random.choice(('Obstacle1', 'Obstacle2', 'Obstacle3'))
                    self.obstacle_spacing += 20
                    new_position = (W_WIDTH, W_HEIGHT - 35 - self.obstacle_spacing)
                    self.entity_list.append(EntityFactory.build_entity(choice, new_position))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)