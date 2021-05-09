import random

def playboard(slot):
    print('\n'*50)

    print(slot[7]+'|'+slot[8]+'|'+slot[9])
    print('-|-|-')
    print(slot[4]+'|'+slot[5]+'|'+slot[6])
    print('-|-|-')
    print(slot[1]+'|'+slot[2]+'|'+slot[3])

def player_type():
    answer = input('Enter A for a two-person game or enter B for computer player: ').upper()

    if answer == 'A':
        game_type = '2person'
    else:
        game_type = 'computer'
    return game_type

def player_move(slot):
    move = 0

    while move not in [1,2,3,4,5,6,7,8,9]:
        move = int(input('Make a move (position 1-9 on numpad): '))

    return move

def computer_move(slot):
    list = []

    for i in range(1,10):
        if slot[i] == ' ':
            list.append(i)
    move = random.choice(list)

    return move

def mark_choice(slot, letter, choice):
    slot[choice] = letter

def check_for_win(slot,letter):
    return ((slot[1] == slot[2] == slot[3] == letter) or
            (slot[4] == slot[5] == slot[6] == letter) or
            (slot[7] == slot[8] == slot[9] == letter) or
            (slot[1] == slot[4] == slot[7] == letter) or
            (slot[2] == slot[5] == slot[8] == letter) or
            (slot[3] == slot[6] == slot[9] == letter) or
            (slot[1] == slot[5] == slot[9] == letter) or
            (slot[3] == slot[5] == slot[7] == letter))

def check_for_tie(slot):
    for i in range(1, 10):
        if slot[i] == ' ':
            return False
    return True

while True:
    slots = [' '] * 10
    player1 = 'O'
    player2 = 'X'
    turn = "Player1"

    game_type = player_type()

    print("Player 1 is O and Player 2 is X")
    print("Player 1 goes first")

    play_game = input('Enter Y to start: ').upper()

    if play_game == 'Y':
        start_game = True
    else:
        break

    while start_game:
        if turn == "Player1":
            playboard(slots)

            choice = player_move(slots)
            mark_choice(slots, player1, choice)

            if check_for_win(slots, player1):
                playboard(slots)
                print("Player 1 wins")

                break

            else:
                if check_for_tie(slots):
                    playboard(slots)
                    print("It's a tie")

                    break

                else:
                    turn = "Player2"

        else:
            playboard(slots)

            if game_type == '2person':
                choice = player_move(slots)
            else:
                choice = computer_move(slots)
            mark_choice(slots, player2, choice)

            if check_for_win(slots, player2):
                playboard(slots)
                print("Player 2 wins")

                break

            else:
                if check_for_tie(slots):
                    playboard(slots)
                    print("It's a tie")

                    break

                else:
                    turn = "Player1"

    break
