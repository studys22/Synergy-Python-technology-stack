import pygame  # as pg
from map import Map
import utils
import settings
from tileset import Tileset

# Background color
BACKGROUND = (0, 0, 0)
TEXTCOLOUR = (200, 100, 0)


class Game(object):
    def __init__(self):
        self.points = 0
        self.text = ""

        tileset = Tileset()
        self.map = Map(tileset)
        self.map.generate_river(10)
        self.map.generate_river(10)
        self.map.generate_trees(15)
        self.map.generate_buildings()
        self.map.update_tilemaps()

    def processEvents(self):
        for event in pygame.event.get():
            # print(event.type)
            if event.type == pygame.QUIT:
                return True
            # #Get keyboard input and move player accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.map.helico.start_go("Left")
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.map.helico.start_go("Right")
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.map.helico.start_go("Up")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.map.helico.start_go("Down")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.map.helico.stop_go("Left")
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.map.helico.stop_go("Right")
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.map.helico.stop_go("Up")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.map.helico.stop_go("Down")

        return False

    def runLogic(self):
        # Update player movement and collision logic
        # self.player.update()
        self.map.helico.go()
        self.points = self.map.processing_helico(self.points)
        self.map.processing_fire()
        self.map.update_tilemaps()
        self.text = "Tank: {water}/{water_capacity}. Lives: {lives}. Points: {points}".format(
            water=self.map.helico.water,
            water_capacity=self.map.helico.water_capacity,
            points=self.points,
            lives=self.map.helico.lives
        )

    # Draw level, player, overlay
    def draw(self, screen, font):
        # self.map.update_tilemaps()
        screen.fill(BACKGROUND)
        self.map.draw(screen)
        # screen.blit(self.overlay, [0, 0])
        text = font.render(self.text, True, TEXTCOLOUR, None)
        screen.blit(text, (0, (settings.SIZE[1] + 1) * settings.TILE_SIZE))
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (
            (settings.SIZE[0] + 2) * settings.TILE_SIZE,
            (settings.SIZE[1] + 2) * settings.TILE_SIZE + settings.TEXT_HEIGHT,
        ),
    )
    pygame.display.set_caption(settings.CAPTION)
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 28)
    clock = pygame.time.Clock()
    done = False
    game = Game()

    while not done:
        done = game.processEvents()
        game.runLogic()
        game.draw(screen, font)
        clock.tick(settings.FPS)

    pygame.quit()


main()
