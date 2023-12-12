import pygame
from map import Map
import settings
from tileset import Tileset
import utils
import json

BACKGROUND = (0, 0, 0)
TEXTCOLOUR = (200, 100, 0)


class Game(object):
    def __init__(self, screen):
        self.points = 0
        self.text = ""
        self.screen = screen

        tileset = Tileset()
        self.map = Map(tileset)
        self.map.generate_river(10)
        self.map.generate_river(10)
        self.map.generate_trees(15)
        self.map.generate_buildings()
        self.map.update_tilemaps()

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.map.helico.start_go("Left")
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.map.helico.start_go("Right")
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.map.helico.start_go("Up")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.map.helico.start_go("Down")

                elif event.key == pygame.K_F2:
                    game_state = self.game_state()
                    with open("save.json", "w") as f:
                        json.dump(game_state, f)
                elif event.key == pygame.K_F3:
                    with open("save.json", "r") as f:
                        game_state = json.load(f)
                    self.game_load(game_state)

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

    def game_state(self):
        gamemap = self.map

        ts = gamemap.ground_tilemap.tileset
        tileset = {
            "file": ts.file,
            "size": ts.size,
            "margin": ts.margin,
            "spacing": ts.spacing,
        }

        sky_ends = self.get_list_from_dict_with_key_tuple(gamemap.sky_ends)
        start_of_fire = self.get_list_from_dict_with_key_tuple(gamemap.start_of_fire)

        result = {
            "points": self.points,
            "size": gamemap.size,
            "ground": gamemap.ground,
            "start_of_fire": start_of_fire,
            "sky": gamemap.sky,
            "sky_ends": sky_ends,
            "cur_time": pygame.time.get_ticks(),
            "helico": gamemap.helico.__dict__,
            "tileset": tileset,
        }

        return result

    def game_load(self, obj: dict):
        self.points = obj["points"]
        ts = obj["tileset"]
        tileset = Tileset(
            ts["file"],
            (ts["size"][0], ts["size"][1]),
            ts["margin"],
            ts["spacing"],
        )
        size = obj["size"]
        size = (size[0], size[1])
        if settings.SIZE != size:
            settings.SIZE = size
            self.screen = pygame.display.set_mode(
                (
                    (settings.SIZE[0] + 2) * settings.TILE_SIZE,
                    (settings.SIZE[1] + 2) * settings.TILE_SIZE,
                ),
            )
        self.map = Map(tileset, size)
        self.map.ground = obj["ground"]
        self.map.sky = obj["sky"]
        helico = obj["helico"]
        h = self.map.helico
        pos = helico["position"]
        pos = (pos[0], pos[1])
        h.position = pos
        h.size_of_map = size
        h.water = helico["water"]
        h.water_capacity = helico["water_capacity"]
        h.lives = helico["lives"]
        d_time = pygame.time.get_ticks() - obj["cur_time"]
        self.map.sky_ends = self.get_dict_with_key_tuple_from_tuple(
            obj["sky_ends"], d_time
        )
        self.map.start_of_fire = self.get_dict_with_key_tuple_from_tuple(
            obj["start_of_fire"], d_time
        )

    def get_list_from_dict_with_key_tuple(self, dict_with_key_tuple):
        result = []
        for key, value in dict_with_key_tuple.items():
            item = {"y": key[0], "x": key[1], "value": value}
            result.append(item)
        return result

    def get_dict_with_key_tuple_from_tuple(self, list, d):
        result = {}
        for elem in list:
            result[(elem["y"], elem["x"])] = elem["value"] + d
        return result

    def runLogic(self) -> bool:
        self.map.helico.go()
        self.points = self.map.processing_helico(self.points)
        self.map.processing_fire()
        self.map.processing_clouds()
        if self.map.helico.lives <= 0:
            self.text = "Game over!!! Points: {points}".format(points=self.points)
            return True
        else:
            self.map.update_tilemaps()
            self.text = "Tank: {water}/{water_capacity}. Lives: {lives}. Points: {points}".format(
                water=self.map.helico.water,
                water_capacity=self.map.helico.water_capacity,
                points=self.points,
                lives=self.map.helico.lives,
            )
            return False

    def draw(self, screen, font):
        screen.fill(BACKGROUND)
        self.map.draw(screen)
        text = font.render(self.text, True, TEXTCOLOUR, None)
        screen.blit(text, (0, (settings.SIZE[1] + 1) * settings.TILE_SIZE))
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (
            (settings.SIZE[0] + 2) * settings.TILE_SIZE,
            (settings.SIZE[1] + 2) * settings.TILE_SIZE,
        ),
    )
    pygame.display.set_caption(settings.CAPTION)
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 28)
    clock = pygame.time.Clock()
    done = False
    game = Game(screen)

    draw = True
    while not done:
        done = game.processEvents()
        gameover = game.runLogic()
        if draw:
            game.draw(game.screen, font)
        draw = not gameover
        clock.tick(settings.FPS)

    pygame.quit()


main()
