from collections import deque
import copy


class Черепашка:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("S не может быть меньше 0")
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        q = deque()
        s = set()
        q.append({"turtle": self, "count_steps": 0, "prev_steps": [], "last_move": ""})
        while True:
            pos = q.popleft()
            turtle = pos["turtle"]
            if turtle in s:
                continue
            s.add(turtle)
            prev_steps = pos["prev_steps"].copy()
            count_steps = pos["count_steps"] + 1
            dx = x2 - turtle.x
            dy = y2 - turtle.y
            last_move = pos["last_move"]
            prev_steps.append({"turtle": turtle, "last_move": last_move})
            if turtle.x == x2 and turtle.y == y2:
                return pos["count_steps"], prev_steps
            if dx > 0:
                self.__move(q, turtle, prev_steps, count_steps, "go_right")
            elif dx < 0:
                self.__move(q, turtle, prev_steps, count_steps, "go_left")
            if dy > 0:
                self.__move(q, turtle, prev_steps, count_steps, "go_up")
            elif dy < 0:
                self.__move(q, turtle, prev_steps, count_steps, "go_down")
            self.__move(q, turtle, prev_steps, count_steps, "evolve")
            self.__move(q, turtle, prev_steps, count_steps, "degrade")

    def __move(self, q, turtle, prev_steps, count_steps, func):
        new_turtle = copy.copy(turtle)
        try:
            getattr(new_turtle, func)()
        except:
            pass
        else:
            q.append(
                {
                    "turtle": new_turtle,
                    "count_steps": count_steps,
                    "prev_steps": prev_steps,
                    "last_move": func,
                }
            )

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}] s={self.s}"
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y and self.s == __value.s
    
    def __hash__(self) -> int:
        return hash(2**self.x * 3**self.y * 5**self.s)


turtle = Черепашка(*tuple(map(int, input("X, Y, S: ").split())))
x2, y2 = map(int, input("X2, Y2: ").split())
count_steps, steps = turtle.count_moves(x2, y2)
print(f"Необходимо шагов: {count_steps}")
i = 0
for step in steps:
    print("{:3d}: {:8} {}".format(i, step["last_move"], step["turtle"]))
    i += 1
