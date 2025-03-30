import pygame

C_GREEN_DARK = (42, 82, 60)
C_GRAY = (128, 128, 128)
C_RED = (84, 43, 58)
C_WHITE_BLUE = (235, 245, 250)



W_WIDTH = 576
W_HEIGHT = 324


MENU_OPTION = ( 'START',
                'SCORE',
                'EXIT'
                )


ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 6,
    'Level1Bg6': 6,
    'Level1Bg7': 6,
    'Obstacle1': 1,
    'Obstacle2': 1,
    'Obstacle3': 1,
    'Candle1': 1,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Player1': 3,

}

EVENT_OBSTACLE = pygame.USEREVENT + 1

SPAWN_TIME = 3000