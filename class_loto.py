import random

class Card:
    def __init__(self, name):
        rnd_list = random.sample(range(1, 90), 15)
        self.field = [rnd_list[x:x + 5] for x in range(0, len(rnd_list), 5)]
        self.space = [random.sample(range(0, 8), 4) for i in range(3)]
        self.cross_count = 0
        self.name = name

    def show(self):
        mult = int((20 - len(self.name)) / 2)
        print('-' * mult + self.name + '-' * mult + '-' * (0 if not len(self.name) % 2 else 1))
        for i in range(3):
            line = ''
            index = 0
            for j in range(9):
                if j in self.space[i]:
                    line += " "
                else:
                    line += str(self.field[i][index]) + " "
                    index += 1
            print(line)
        print('-' * 20)

    def cross(self, number):
        result = False
        for i in range(3):
            for j in range(5):
                if self.field[i][j] == number:
                    self.field[i][j] = '-'
                    self.cross_count += 1
                    result = True
        return result


class Player:

    @property
    def is_computer(self):
        return self.__is_computer

    def __init__(self, name, is_computer):
        self.__card = Card(name)
        self.__is_computer = is_computer
        self.name = name

    def test(self, num):
        return self.__card.cross(int(num)) or self.__is_computer

    def show_card(self):
        self.__card.show()

    def is_all_cross(self):
        return self.__card.cross_count == 15