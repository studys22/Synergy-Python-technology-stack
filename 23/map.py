import utils
import pygame
import settings
from helicopter import Helicopter
from tilemap import Tilemap

GROUND_ID = 1
RIVER_ID = 2
TREE_ID = 3
FIRE_ID = 4
STORE_ID = 5
HOSPITAL_ID = 6

TILE_TREE_ID = 94
TILE_FIRE_ID = 80
TILE_HELICO_ID = 101
TILE_HELICO_SHADOW_ID = 197
TILE_STORE_ID = 66
TILE_HOSPITAL_ID = 81

ground = "⬛🟫🟩🌲🟦🔥⛅🌪️🚁💗⭐"

possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]


class Map:
    def __init__(self, ts, size=(settings.WIDTH, settings.HEIGHT)) -> None:
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.ground = [
            [GROUND_ID for j in range(self.width + 2)] for i in range(self.height + 2)
        ]
        self.ground_tilemap = Tilemap(ts, True)
        self.onground_tilemap = Tilemap(ts)
        self.start_of_fire = {}
        self.helico = Helicopter(size)
        self.helico_tilemap = Tilemap(ts)

    def in_map(self, x: int, y: int) -> bool:
        return 0 < x and x <= self.height and 0 < y and y <= self.width

    def generate_river(self, length: int) -> None:
        start_found = False
        x, y = 0, 0
        while not start_found:
            x, y = utils.rand_point(self.height, self.width)
            if self.ground[x][y] == GROUND_ID:
                start_found = True

        cells = []
        cells.append((x, y))
        self.ground[x][y] = RIVER_ID
        cur_len = 1
        while cur_len < length:
            legal_moves = []
            for possible_move in possible_moves:
                xx = x + possible_move[0]
                yy = y + possible_move[1]
                if self.in_map(xx, yy) and self.ground[xx][yy] == GROUND_ID:
                    legal_moves.append(possible_move)
            if len(legal_moves) == 0:
                break
            move = utils.rand_move(legal_moves)
            x, y = x + move[0], y + move[1]
            self.ground[x][y] = RIVER_ID
            cells.append((x, y))
            cur_len += 1

        for cell in cells:
            for neighbour in neighbors:
                x, y = cell[0] + neighbour[0], cell[1] + neighbour[1]
                if self.in_map(x, y):
                    self.ground[x][y] = RIVER_ID

    def generate_river_old(self, length: int) -> None:
        start_found = False
        x, y = 0, 0
        cur_br = (0, 1)
        while not start_found:
            x, y = utils.rand_point(self.height, self.width)
            if (
                self.ground[x][y] == GROUND_ID
                and self.ground[x + cur_br[0]][y + cur_br[1]]
            ):
                start_found = True

        move = (0, 0)
        cur_len = 0
        while True:
            if move == cur_br:
                if self.ground[x - cur_br[1]][y - cur_br[0]] == GROUND_ID:
                    new_cur_br = (-cur_br[1], -cur_br[0])
                elif self.ground[x + cur_br[1]][y + cur_br[0]] == GROUND_ID:
                    new_cur_br = (cur_br[1], cur_br[0])
                else:
                    break
                xx = x + new_cur_br[0] - cur_br[0]
                yy = y + new_cur_br[1] - cur_br[1]
                if self.in_map(xx, yy):
                    self.ground[xx][yy] = RIVER_ID
                else:
                    break
                cur_br = new_cur_br
            elif move[0] == -cur_br[0] and move[1] == -cur_br[1]:
                if self.ground[x - cur_br[1]][y - cur_br[0]] == GROUND_ID:
                    new_cur_br = (-cur_br[1], -cur_br[0])
                elif self.ground[x + cur_br[1]][y + cur_br[0]] == GROUND_ID:
                    new_cur_br = (cur_br[1], cur_br[0])
                else:
                    break
                if new_cur_br[0] == 0 and cur_br[1] == 0:
                    xx = x + new_cur_br[1]
                    yy = y + cur_br[0]
                    if self.in_map(xx, yy):
                        self.ground[xx][yy] = RIVER_ID
                    else:
                        break
                else:
                    xx = x + new_cur_br[0]
                    yy = y + cur_br[1]
                    if self.in_map(xx, yy):
                        self.ground[xx][yy] = RIVER_ID
                    else:
                        break
            else:
                self.ground[x][y] = RIVER_ID
            self.ground[x + cur_br[0]][y + cur_br[1]] = RIVER_ID
            cur_len += 1
            if length == cur_len:
                break
            legal_moves = []
            for possible_move in possible_moves:
                xx = x + possible_move[0]
                yy = y + possible_move[1]
                if self.in_map(xx, yy) and (
                    self.ground[xx][yy] == GROUND_ID
                    or (self.ground[xx][yy] == RIVER_ID and cur_br == possible_move)
                ):
                    legal_moves.append(possible_move)
            if len(legal_moves) == 0:
                break
            move = utils.rand_move(legal_moves)
            x, y = x + move[0], y + move[1]

    def generate_trees(self, amount_of_trees: int, percent_of_trees: float = 0) -> None:
        possible_points = []
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                if self.ground[i][j] == GROUND_ID:
                    possible_points.append((i, j))
        amount_of_possible_points = len(possible_points)
        remainder_of_trees = min(amount_of_possible_points, amount_of_trees)
        while remainder_of_trees >= 0:
            amount_of_possible_points -= 1
            remainder_of_trees -= 1
            k = utils.rand_int(amount_of_possible_points - 1)
            point = possible_points.pop(k)
            self.ground[point[0]][point[1]] = TREE_ID

    def generate_buildings(self) -> None:
        point_found = False
        y, x = 0, 0
        while not point_found:
            y, x = utils.rand_point(self.height, self.width)
            if self.ground[y][x] == GROUND_ID:
                point_found = True
        self.ground[y][x] = STORE_ID

        point_found = False
        while not point_found:
            y, x = utils.rand_point(self.height, self.width)
            if self.ground[y][x] == GROUND_ID:
                point_found = True
        self.ground[y][x] = HOSPITAL_ID

    def processing_fire(self) -> None:
        cur_time = pygame.time.get_ticks()
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                if self.ground[i][j] == TREE_ID and utils.start_fire():
                    self.ground[i][j] = FIRE_ID
                    self.start_of_fire[(i, j)] = pygame.time.get_ticks()
                elif (
                    self.ground[i][j] == FIRE_ID
                    and cur_time - self.start_of_fire[(i, j)]
                    >= settings.MAX_DURATION_OF_FIRE
                ):
                    self.ground[i][j] = GROUND_ID
                    self.start_of_fire.pop((i, j))

    def update_tilemaps(self) -> None:
        cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                prev = self.ground_tilemap.map[i][j]
                if self.ground[i][j] == RIVER_ID:
                    cell_code = 0
                    for k in range(8):
                        cell_code += (
                            1
                            if self.ground[i + cells[k][0]][j + cells[k][1]] == RIVER_ID
                            else 0
                        ) << k
                    self.ground_tilemap.map[i][j] = settings.water_index[cell_code]

                elif self.ground[i][j] in {TREE_ID, FIRE_ID, STORE_ID, HOSPITAL_ID}:
                    self.ground_tilemap.map[i][j] = 0
                else:
                    self.ground_tilemap.map[i][j] = (
                        prev
                        if prev in {0, 1, 2}
                        else utils.rand_move([0, 0, 0, 0, 0, 1, 1, 1, 2])
                    )

        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                if self.ground[i][j] == TREE_ID:
                    self.onground_tilemap.map[i][j] = TILE_TREE_ID
                elif self.ground[i][j] == FIRE_ID:
                    self.onground_tilemap.map[i][j] = TILE_FIRE_ID
                elif self.ground[i][j] == STORE_ID:
                    self.onground_tilemap.map[i][j] = TILE_STORE_ID
                elif self.ground[i][j] == HOSPITAL_ID:
                    self.onground_tilemap.map[i][j] = TILE_HOSPITAL_ID
                else:
                    self.onground_tilemap.map[i][j] = -1

        self.helico_tilemap.set_zero()
        self.helico_tilemap.map[self.helico.position[0] - 1][
            self.helico.position[1]
        ] = TILE_HELICO_ID
        self.helico_tilemap.map[self.helico.position[0]][
            self.helico.position[1]
        ] = TILE_HELICO_SHADOW_ID

    def draw(self, window) -> None:
        self.ground_tilemap.render()
        window.blit(self.ground_tilemap.image, (0, settings.TEXT_HEIGHT))
        self.onground_tilemap.render()
        window.blit(self.onground_tilemap.image, (0, settings.TEXT_HEIGHT))
        self.helico_tilemap.render()
        window.blit(self.helico_tilemap.image, (0, settings.TEXT_HEIGHT))

    def processing_helico(self, points) -> int:
        y, x = self.helico.position[0], self.helico.position[1]
        if self.ground[y][x] == FIRE_ID and self.helico.water > 0:
            self.helico.water -= 1
            self.ground[y][x] = TREE_ID
            points += settings.POINTS_FOR_EXTINGUISHING_FIRE
        elif self.ground[y][x] == RIVER_ID:
            self.helico.water = self.helico.water_capacity
        elif self.ground[y][x] == STORE_ID and points >= settings.UPGRADE_TANK_COST:
            self.helico.water_capacity += 1
            points -= settings.UPGRADE_TANK_COST
        elif self.ground[y][x] == HOSPITAL_ID and points >= settings.ADD_LIVES_COST:
            self.helico.lives += settings.COUNT_ADDED_LIVES
            points -= settings.ADD_LIVES_COST
        return points
