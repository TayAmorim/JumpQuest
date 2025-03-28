from code.Background import Background
from code.Const import W_WIDTH, W_HEIGHT
from code.Obstacle import Obstacle


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

            case 'Obstacle1':
                obstacle_width = 46
                obstacle_height = 66

                x_pos = W_WIDTH - obstacle_width / 2
                y_pos = W_HEIGHT - obstacle_height - 0
                return Obstacle('Obstacle1', (x_pos , y_pos))
            case 'Obstacle2':
                obstacle_width = 89
                obstacle_height = 62

                x_pos = W_WIDTH - obstacle_width / 2
                y_pos = W_HEIGHT - obstacle_height - 0
                return Obstacle('Obstacle2', (x_pos, y_pos))

            case 'Obstacle3':
                obstacle_width = 64
                obstacle_height = 64

                x_pos = W_WIDTH - obstacle_width / 2
                y_pos = W_HEIGHT - obstacle_height + 15
                return Obstacle('Obstacle3', (x_pos, y_pos))