# Игра "Пятнашки"
import random

# Заготовки для отображения поля

up = "_____________________"
mid = "---------------------"
bot = "---------------------"


def get_new_random():
    line = list(range(16))
    random.shuffle(line)
    return line


def print_board(new_game):
    print(up)
    for i in range(0, 16):
        if new_game[i] < 10:
            if new_game[i] == 0:
                print('|____', end='')
            else:
                print('| ' + str(new_game[i]) + '  ', end='')
        else:
            num = str(new_game[i])
            print('| ' + num + ' ', end='')
        if i == 3 or i == 7 or i == 11:
            print('|')
            print(mid)
    print('|')
    print(bot)


def ansver():
    while True:
        text = input('Введіть число від 1 до 15:')
        if text.isdigit() == False:
            print('Можна вводити тільки цілі числа! Спробуйте ще раз.')
        elif 15 < int(text) or int(text) < 0:
            print('Цього числа немає на ігровому полі, вибирайте число з заданого проміжку!')
        else:
            return int(text)


def possible_moves(new_game):
    moves = [0]
    ind = new_game.index(0)
    if ind == 0:
        moves.append(new_game[1])
        moves.append(new_game[4])
    elif ind == 1:
        moves.append(new_game[0])
        moves.append(new_game[2])
        moves.append(new_game[5])
    elif ind == 2:
        moves.append(new_game[1])
        moves.append(new_game[3])
        moves.append(new_game[6])
    elif ind == 3:
        moves.append(new_game[2])
        moves.append(new_game[7])
    elif ind == 4:
        moves.append(new_game[0])
        moves.append(new_game[5])
        moves.append(new_game[8])
    elif ind == 5:
        moves.append(new_game[1])
        moves.append(new_game[4])
        moves.append(new_game[6])
        moves.append(new_game[9])
    elif ind == 6:
        moves.append(new_game[2])
        moves.append(new_game[5])
        moves.append(new_game[7])
        moves.append(new_game[10])
    elif ind == 7:
        moves.append(new_game[3])
        moves.append(new_game[6])
        moves.append(new_game[11])
    elif ind == 8:
        moves.append(new_game[4])
        moves.append(new_game[9])
        moves.append(new_game[12])
    elif ind == 9:
        moves.append(new_game[5])
        moves.append(new_game[8])
        moves.append(new_game[10])
        moves.append(new_game[13])
    elif ind == 10:
        moves.append(new_game[6])
        moves.append(new_game[9])
        moves.append(new_game[11])
        moves.append(new_game[14])
    elif ind == 11:
        moves.append(new_game[7])
        moves.append(new_game[10])
        moves.append(new_game[15])
    elif ind == 12:
        moves.append(new_game[8])
        moves.append(new_game[13])

    elif ind == 13:
        moves.append(new_game[9])
        moves.append(new_game[12])
        moves.append(new_game[14])
    elif ind == 14:
        moves.append(new_game[10])
        moves.append(new_game[13])
        moves.append(new_game[15])
    else:
        moves.append(new_game[11])
        moves.append(new_game[14])

    return moves


# основной код игры
win = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
new_game = get_new_random()
print_board(new_game)
move_count = 0

while True:
    moves = possible_moves(new_game)
    move_num = ansver()
    if move_num in moves:
        ind_move = new_game.index(move_num)
        ind_0 = new_game.index(0)
        new_game[ind_0] = move_num
        new_game[ind_move] = 0
        print_board(new_game)

        move_count = move_count + 1
        if move_count % 10 == 1:
            print("Це ваш", move_count, "хід")
        if move_count % 10 == 2 or move_count % 10 == 3 or move_count % 10 == 4:
            print("Ви уже зробили", move_count, "ходи")
        if move_count % 10 == 5 or move_count % 10 == 6 or move_count % 10 == 7 or move_count % 10 == 8 or move_count % 10 == 9 or move_count % 10 == 0:
            print("Це ваш", move_count, "хід")


    else:
        print('Це число неможливо перемістити!')

    if new_game == win:
        print('Вітаю! Ви перемогли!')
        if move_count % 10 == 1:
            print("Для перемоги у цій грі вам знадобився", move_count, "хід")
        if move_count % 10 == 2 or move_count % 10 == 3 or move_count % 10 == 4:
            print("Для перемоги у цій грі вам знадобилося", move_count, "ходи")
        else:
            print("Для перемоги у цій грі вам знадобилося", move_count, "ходів")
        break
