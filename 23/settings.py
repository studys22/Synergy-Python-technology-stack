

CAPTION = "Helicopter battle"
HEIGHT = 10
WIDTH  = 20
SIZE = (WIDTH, HEIGHT)
FPS = 10
TEXT_HEIGHT = 50 * 0

PROBABILITY_OF_STARTING_FIRE = 0.05 / FPS
MAX_DURATION_OF_FIRE = 5 * 1000 # seconds

UPGRADE_TANK_COST = 500
POINTS_FOR_EXTINGUISHING_FIRE = 100

START_LIVES = 5
ADD_LIVES_COST = 1000
COUNT_ADDED_LIVES = 5

file_tileset = 'images/tilemap_packed_32.png'
#file_tileset = 'images/tilemap_32.png'
TILE_SIZE = 32

water_index_file = open('water_index.txt','r')
water_index = list(map(int, water_index_file.readline().split()))

