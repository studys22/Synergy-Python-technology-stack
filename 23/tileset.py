import pygame
import settings


class Tileset:
    def __init__(
        self,
        file=settings.file_tileset,
        size=(settings.TILE_SIZE, settings.TILE_SIZE),
        margin=0,
        spacing=0,
    ):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        h, w = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for y in range(y0, w, dy):
            for x in range(x0, h, dx):
                tile = pygame.Surface(
                    self.size,
                    pygame.SRCALPHA,
                )
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f"{self.__class__.__name__} file:{self.file} tile:{self.size}"
