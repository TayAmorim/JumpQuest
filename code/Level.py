import random
import sys

import pygame.mixer_music
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION, EVENT_OBSTACLE, SPAWN_TIME, C_RED, W_HEIGHT, W_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Obstacle import Obstacle
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.build_entity(self.name + 'Bg'))
        self.obstacle_spacing = 0

        self.player = EntityFactory.build_entity('Player', (10, W_HEIGHT - 50))

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

                if isinstance(ent, Obstacle):
                    self.player.check_collision(ent)

            self.player.move()
            self.player.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                    if event.key == pygame.K_LEFT:
                        self.player.set_horizontal_velocity(-2)
                    elif event.key == pygame.K_RIGHT:
                        self.player.set_horizontal_velocity(2)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.player.jump()
                        if event.key == pygame.K_LEFT:
                            self.player.set_horizontal_velocity(-2)
                        elif event.key == pygame.K_RIGHT:
                            self.player.set_horizontal_velocity(2)
                    elif event.type == pygame.KEYUP:
                        if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                            self.player.set_horizontal_velocity(0)

                if event.type == EVENT_OBSTACLE:
                    choice = random.choice(( 'Obstacle1', 'Obstacle2'))
                    self.obstacle_spacing += random.randint(10, 50)
                    new_position = (W_WIDTH, W_HEIGHT - 35 - self.obstacle_spacing)
                    self.entity_list.append(EntityFactory.build_entity(choice, new_position))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def game_over(self):
        self.level_text(50, "Game Over", C_RED, (W_WIDTH // 2, W_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        sys.exit()