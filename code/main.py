from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join, dirname, abspath #for file handling OS
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pyboy-Blue')

        self.import_assets()

    def import_assets(self):
        BASE_DIR = dirname(abspath(__file__))
        map_path = join(BASE_DIR, '..', 'data', 'maps', 'world.tmx')
        self.tmx_maps = {'world': load_pygame(map_path)}
        print(self.tmx_maps)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()


