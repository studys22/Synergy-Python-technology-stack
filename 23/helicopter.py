import settings
import utils


class Helicopter:
    def __init__(self, size=(settings.WIDTH, settings.HEIGHT)):
        self.position = (size[1] // 2, size[0] // 2)
        self.size_of_map = size
        self.water = 0
        self.water_capacity = 1
        self.speed_x = 0
        self.speed_y = 0
        self.lives = settings.START_LIVES

    def in_map(self, pos: tuple) -> bool:
        return (
            0 < pos[1]
            and pos[1] <= self.size_of_map[0]
            and 0 < pos[0]
            and pos[0] <= self.size_of_map[1]
        )

    def go(self) -> None:
        new_position = (
            self.position[0] + self.speed_y,
            self.position[1] + self.speed_x,
        )
        if self.in_map(new_position):
            self.position = new_position

    def start_go(self, direction: str) -> None:
        if direction == "Left":
            self.speed_x = -1
        elif direction == "Right":
            self.speed_x = 1
        elif direction == "Up":
            self.speed_y = -1
        elif direction == "Down":
            self.speed_y = 1

    def stop_go(self, direction: str) -> None:
        if direction == "Left":
            self.speed_x = 0
        elif direction == "Right":
            self.speed_x = 0
        elif direction == "Up":
            self.speed_y = 0
        elif direction == "Down":
            self.speed_y = 0
