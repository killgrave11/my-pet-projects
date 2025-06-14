number_of_sticks = 10
player_turn = 1


def can_take(sticks):
    return sticks >= 1 and sticks <= 3

def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2

def end_of_game(sticks):
    return number_of_sticks <= 0
    
while (not end_of_game(number_of_sticks)):
    print(f"Сколько палочек вы хотите взять? Палочек осталось {number_of_sticks}")
    taken = int(input())
    
    if not can_take(taken):
        print(f"Вы попробовали взять {taken}. Возможно взять 1, 2 или 3 палочки.")
        continue
    
    number_of_sticks -= taken
    print(f"Палочек взято: {taken}\n")
    
    if end_of_game(number_of_sticks):
        print(f"Палочек больше не осталось. \nИгрок {player_turn} проиграл!")
        break
    
    player_turn = switch_player_turn(player_turn)