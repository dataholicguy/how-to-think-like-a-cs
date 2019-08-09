def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

if __name__ == '__main__':
    again = True
    my_score = 0
    your_score = 0
    games = 0
    human_plays_first = True
    while again:
        result = play_once(human_plays_first)
        games += 1
        if result == -1:
            print('I win!')
            my_score += 1
        elif result == 0:
            print('Game drawn!')
        elif result == 1:
            print('You win!')
            your_score += 1
        print('Human Score:', my_score, '\tComputer Score:', your_score)
        percentage = my_score / games * 100
        print('Percentage of wins for human:', percentage, '%')
        answer = input('Do you want to play again?')
        if answer != 'yes':
            print('Goodbye')
            break
