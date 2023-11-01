import random

# Инициализация игры
WIDTH, HEIGHT = 10, 10
helicopter_x, helicopter_y = WIDTH // 2, HEIGHT - 1
water_reserve = 100
trees = set()
tree_spawn_rate = 0.1
tree_fire_rate = 0.05
tree_fire = False
score = 0

# Основной игровой цикл
running = True

while running:
    # Генерация деревьев
    if random.random() < tree_spawn_rate:
        tree_x, tree_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
        trees.add((tree_x, tree_y))

    # Загорание деревьев
    if random.random() < tree_fire_rate and trees:
        tree_fire = True

    # Вывод игрового поля
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (helicopter_x, helicopter_y):
                print("H", end=" ")
            elif (x, y) in trees:
                print("T", end=" ")
            elif x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
        print()

    # Управление вертолетом
    move = input("Move left (L), right (R), or extinguish fire (E): ").upper()
    if move == "L" and helicopter_x > 1:
        helicopter_x -= 1
    elif move == "R" and helicopter_x < WIDTH - 2:
        helicopter_x += 1
    elif move == "E" and water_reserve > 0:
        water_reserve -= 1
        if tree_fire:
            score += 10
            tree_fire = False

    # Обработка деревьев и счет
    for tree in list(trees):
        if (tree[0], tree[1] + 1) == (helicopter_x, helicopter_y):
            water_reserve = 100
            trees.remove(tree)
        elif (tree[0], tree[1] + 1) in trees:
            tree_fire = True
            trees.remove((tree[0], tree[1] + 1))
            trees.remove(tree)
        elif tree_fire:
            score -= 10
            trees.remove(tree)
            
    print(f"Water reserve: {water_reserve}")
    print(f"Score: {score}")
    
    if score < 0:
        running = False

print("Game Over")
