from code.Background import Background
from code.Const import W_WIDTH


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