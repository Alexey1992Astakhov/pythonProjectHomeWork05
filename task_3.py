#3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

win_combination = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]

def maps_print():
    print("\n" * 100)
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

def win_maps(play1, play2):
    win = ""

    for i in win_combination:
        if maps[i[0]] == play1 and maps[i[1]] == play1 and maps[i[2]] == play1:
            win = f"Player 1{play1}"
        if maps[i[0]] == play2 and maps[i[1]] == play2 and maps[i[2]] == play2:
            win = f"Player 2{play2}"
    return win

game_over = False
player1 = True

while game_over == False:

    maps_print()

    if player1 == True:
        symbol = chr(10008)
        step = int(input("Ходит player 1: "))
    else:
        symbol = chr(11096)
        step = int(input("Ходит player 2: "))

    maps[maps.index(step)] = symbol

    win = win_maps(chr(10008), chr(11096))

    if win:
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

maps_print()
input(f"Выиграл {win}   ")