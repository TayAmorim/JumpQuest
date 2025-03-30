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
    'Obstacle1': 2,
    'Obstacle2': 2,
    'Obstacle3': 2,
    'Candle1': 1,
    'Level2Bg0': 2,
    'Level2Bg1': 3,
    'Level2Bg2': 4,
    'Player1': 3,

}

SCORE_POS = {
    'Title': (W_WIDTH / 2, 50),
    'EnterName': (W_WIDTH / 2, 90),
    'Label': (W_WIDTH / 2, 90),
    'Name': (W_WIDTH / 2, 110),
    0: (W_WIDTH / 2, 110),
    1: (W_WIDTH / 2, 130),
    2: (W_WIDTH / 2, 150),
    3: (W_WIDTH / 2, 170),
    4: (W_WIDTH / 2, 190),
    5: (W_WIDTH / 2, 210),
    6: (W_WIDTH / 2, 230),
    7: (W_WIDTH / 2, 250),
    8: (W_WIDTH / 2, 270),
    9: (W_WIDTH / 2, 290),
}

EVENT_OBSTACLE = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2


TIMEOUT_STEP = 100
SPAWN_TIME = 1800
TIMEOUT_LEVEL = 10000