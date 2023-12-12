import utils
import pygame
import settings


class Tilemap:
    def __init__(
        self,
        tileset,
        bounds: bool = True,
        size=(settings.WIDTH, settings.HEIGHT),
        rect=None,
    ):
        self.size = size
        self.tileset = tileset
        self.map = list(
            list(-1 for j in range(size[0] + 2)) for i in range(size[1] + 2)
        )
        if bounds:
            for i in [0, size[1] + 1]:
                for j in range(size[0] + 2):
                    self.map[i][j] = 0
            for i in range(size[1] + 2):
                for j in [0, size[0] + 1]:
                    self.map[i][j] = 0

        w, h = self.size
        self.image = pygame.Surface(
            (settings.TILE_SIZE * (w + 2), settings.TILE_SIZE * (h + 2)),
            pygame.SRCALPHA,
        )
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()

    def render(self):
        self.image = pygame.Surface(
            (
                settings.TILE_SIZE * (self.size[0] + 2),
                settings.TILE_SIZE * (self.size[1] + 2),
            ),
            pygame.SRCALPHA,
        )
        w, h = self.size
        for i in range(h + 2):
            for j in range(w + 2):
                if self.map[i][j] == -1:
                    continue
                tile = self.tileset.tiles[self.map[i][j]]
                self.image.blit(tile, (j * settings.TILE_SIZE, i * settings.TILE_SIZE))

    def set_zero(self):
        self.map = list(
            list(-1 for j in range(self.size[0] + 2)) for i in range(self.size[1] + 2)
        )
        # self.render()

    def set_random(self):
        n = len(self.tileset.tiles)
        self.map = list(
            list(utils.rand_int(n - 1) for j in range(self.size[0] + 2))
            for i in range(self.size[1] + 2)
        )
        self.render()

    def __str__(self):
        return f"{self.__class__.__name__} {self.size}"
