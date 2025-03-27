import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import W_WIDTH, C_GREEN_DARK, MENU_OPTION, C_GRAY, C_RED, C_WHITE_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.write_text(45, 'JumpQuest', C_GREEN_DARK, ((W_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.write_text(25, MENU_OPTION[i], C_RED, ((W_WIDTH / 2), 200 + 25 * i))
                else:
                    self.write_text(25, MENU_OPTION[i], C_WHITE_BLUE, ((W_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def write_text(self, text_size: int, text:str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Gill Sans', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)