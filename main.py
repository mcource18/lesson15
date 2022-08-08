import  random
from class_loto import Card,Player

card1 = Card("Alex")
card2 = Card("Alex")
print(card1==card2)
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

if __name__ == '__main__':
    play()
