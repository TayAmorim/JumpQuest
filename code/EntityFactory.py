from code.Background import Background
from code.Const import W_WIDTH, W_HEIGHT
from code.Obstacle import Obstacle
from code.Player import Player


class EntityFactory:
    @staticmethod
    def build_entity(entity_name: str, position=(0, 0)):

        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range (8):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                    list_bg.append(Background(f'Level1Bg{i}', (W_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level2Bg{i}', position))
                    list_bg.append(Background(f'Level2Bg{i}', (W_WIDTH, 0)))
                return list_bg

            case 'Obstacle1':
                obstacle_width = 32
                obstacle_height = 32

                x_pos = W_WIDTH - obstacle_width / 2
                y_pos = W_HEIGHT - obstacle_height + 10
                return Obstacle('Obstacle1', (x_pos , y_pos))
            case 'Obstacle2':
                obstacle_width = 32
                obstacle_height = 32

                x_pos = W_WIDTH - obstacle_width / 2
                y_pos = W_HEIGHT - obstacle_height + 10
                return Obstacle('Obstacle2', (x_pos, y_pos))


            case 'Player':
                return Player('Player', position)