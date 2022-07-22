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




def play():
    print('1. играть с компьютером')
    print('2. играть с человеком')
    print('3. Настраиваемая игра')

    while True:
        try:
            choice = input('Выберите пункт меню ')
            if choice == '1':
                player_name=input('Выберите имя игрока ')
                players = [Player(player_name, is_computer=False), Player("Computer", is_computer=True)]
                break
            elif choice == '2':
                player_name_1 = input('Выберите имя игрока 1 ')
                player_name_2 = input('Выберите имя игрока 2 ')
                players = [Player(player_name_1, is_computer=False), Player(player_name_2, is_computer=False)]
                break
            elif choice=='3':
                count_player = int(input('Введите количество игроков '))
                players =[]
                for i in range(count_player):
                    players_name=input(f'Выберите имя игрока {i+1} ')
                    is_computer= input("Это компьютер? (y/n) ")=="y"
                    players.append(Player(players_name,is_computer))
                break
            else:
                print('Неверный пункт меню')
        except  Exception:
            print("Неверный ввод")


    list_value = [i for i in range(1, 91)]
    while True:
        for player in players:
            player.show_card()

        num = random.choice(list_value)
        list_value.remove(num)

        for player in players:
            sym = 'y'
            while True:
                if not player.is_computer:
                    sym = input(f'{player.name} зачеркнуть цифру {num}? (y/n)')
                if sym == 'y':
                    if not player.test(num):
                        print(f"{player.name} lose")
                        return
                    else:
                        break
                elif sym == 'n':
                    if player.test(num):
                        print(f"{player.name} lose")
                        return
                    else:
                        break
                else:
                    print("Неверный символ.")
            if (player.is_all_cross()):
                print(f"{player.name} win")
                return


play()
