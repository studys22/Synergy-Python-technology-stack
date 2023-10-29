class Касса:
    money = 0

    def top_up(self, X):
        self.money += X

    def count_1000(self):
        print(f"В кассе осталось целых тысяч: {self.money // 1000}")

    def take_away(self, X):
        if X > self.money:
            print("Недостаточно денег!")
        else:
            self.money -= X


c = Касса()
c.top_up(4236)
c.count_1000()
c.take_away(4237)
c.count_1000()
c.take_away(2237)
c.count_1000()
