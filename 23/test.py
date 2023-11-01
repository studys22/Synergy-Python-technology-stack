import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Firefighting Helicopter Game")

# Инициализация вертолета
helicopter_x = WIDTH // 2
helicopter_y = HEIGHT - 50
helicopter_speed = 5
water_reserve = 100

# Инициализация деревьев
trees = []
tree_spawn_rate = 200
tree_fire_rate = 300
tree_size = 20
tree_fire = False

# Основной игровой цикл
running = True
score = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление вертолетом
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and helicopter_x > 0:
        helicopter_x -= helicopter_speed
    if keys[pygame.K_RIGHT] and helicopter_x < WIDTH - 20:
        helicopter_x += helicopter_speed
    if keys[pygame.K_SPACE] and water_reserve > 0:
        water_reserve -= 1
        if tree_fire:
            score += 10
            tree_fire = False

    # Генерация деревьев
    if random.randint(1, tree_spawn_rate) == 1:
        tree_x = random.randint(0, WIDTH - tree_size)
        tree_y = random.randint(0, HEIGHT - tree_size)
        trees.append((tree_x, tree_y))

    # Загорание деревьев
    if random.randint(1, tree_fire_rate) == 1:
        if trees:
            tree_fire = True

    # Отрисовка игровых объектов
    screen.fill(WHITE)
    for tree in trees:
        pygame.draw.rect(screen, GREEN if not tree_fire else RED, (*tree, tree_size, tree_size))

    pygame.draw.rect(screen, BLUE, (helicopter_x, helicopter_y, 20, 20))
    pygame.draw.rect(screen, BLUE, (0, HEIGHT - 50, WIDTH, 20))
    pygame.draw.rect(screen, BLUE, (0, 0, 20, HEIGHT))
    pygame.draw.rect(screen, BLUE, (WIDTH - 20, 0, 20, HEIGHT))

    # Отображение резервуара с водой
    font = pygame.font.Font(None, 36)
    text = font.render(f"Water: {water_reserve}", True, BLUE)
    screen.blit(text, (10, 10))

    # Отображение счета
    text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(text, (10, 50))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
