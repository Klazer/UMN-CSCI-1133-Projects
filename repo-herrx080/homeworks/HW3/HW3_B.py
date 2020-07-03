#CSCI 1133 Section 19 Lab 006, Homework Problem B, Isaiah Herr

R = 'Rock'
S = 'Scissors'
P = 'Paper'

def main():
    rounds=0
    Gamenumber = 1
        #It will represent the game number. It increases after every round.
    P1 = 0
    P2 = 0
    while (rounds<3):
        print('Game', Gamenumber, ':' )
        Player1 = input('Player 1: ')
        Player2 = input('Player 2: ')
        print(rock_paper_scissors(Player1, Player2))
        win = rock_paper_scissors(Player1, Player2)


        rounds = rounds+1
        Gamenumber = Gamenumber + 1

        if win == 'Player1 wins!':
            P1 = P1+1
        elif win == 'Player2 wins!':
            P2 = P2 +1

    if P1 > P2 :
        print('Player 1 Wins! Congratulations!')
    elif P1 < P2:
        print('Player 2 Wins! Congratulations!')
    elif P1 == P2:
        print('A tie, no one wins.')

def rock_paper_scissors(Player1, Player2):

    Rock = 'R'
    Scissors = 'S'
    Paper = 'P'

    if Player1 == Rock and Player2 == Scissors:
        return 'Player1 wins!'
    elif Player1 == Scissors and Player2 == Paper:
        return 'Player1 wins!'
    elif Player1 == Paper and Player2 == Rock:
        return 'Player1 wins!'
    elif Player2 == Rock and Player1 == Scissors:
        return 'Player2 wins!'
    elif Player2 == Scissors and Player1 == Paper:
        return 'Player2 wins!'
    elif Player2 == Paper and Player1 == Rock:
        return 'Player2 wins!'
    elif Player2 == Player1:
        return 'A tie!'
    else:
        return 'This is not valid'
        
        
    

main()
