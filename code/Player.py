import pygame.image
from pygame import Surface

from code.Const import W_HEIGHT, W_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


        self.frames = [pygame.image.load(f'./asset/{name}{i}.png') for i in range(8)]

        self.current_frame = 0
        self.rect = self.frames[self.current_frame].get_rect(left=position[0], top= position[1])
        self.vel_y = 0
        self.vel_x = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.grounded = True



    def jump(self):
        if self.grounded:
            self.vel_y = self.jump_strength
            self.grounded = False
            self.current_frame = 1

    def move(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        self.rect.x += self.vel_x

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > W_WIDTH:
            self.rect.right = W_WIDTH

        if self.rect.bottom >= W_HEIGHT - 0:
            self.rect.bottom = W_HEIGHT - 0
            self.vel_y = 0
            self.vel_x = 0
            self.grounded = True
            self.current_frame = 0

        if not self.grounded:
            if self.vel_y < 5:
                self.current_frame = 2
            elif self.vel_y < 0:
                self.current_frame = 3
            elif self.vel_y > 0:
                self.current_frame = 5
        self.surf = self.frames[self.current_frame]

    def set_horizontal_velocity(self, velocity: int):
        self.vel_x = velocity

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def check_collision(self, obstacle):
        if self.rect.colliderect(obstacle.rect):
            print("Colisão detectada!")
            return True
        return False