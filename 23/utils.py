import random
import settings

random.seed()


def rand_point(w, h) -> tuple:
    return (random.randint(1, w), random.randint(1, h))


def rand_direction() -> int:
    return random.randint(0, 3)


def rand_int(max: int) -> int:
    return random.randint(0, max)


def rand_move(points: list) -> tuple:
    length = len(points)
    if length == 0:
        return (0, 0)
    else:
        return points[random.randint(0, length - 1)]


def start_fire(p: float = settings.PROBABILITY_OF_STARTING_FIRE) -> bool:
    return random.random() < p


def start_cloud(p: float = settings.PROBABILITY_OF_CLOUD) -> bool:
    return random.random() < p


def start_lighting(p: float = settings.PROBABILITY_OF_LIGHTING) -> bool:
    return random.random() < p


def duration_of_cloud() -> int:
    return random.randint(
        settings.MIN_DURATION_OF_CLOUDS, settings.MAX_DURATION_OF_CLOUDS
    )
