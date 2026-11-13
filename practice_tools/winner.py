def decide_winner(player_roll,computer_roll):
    if player_roll>computer_roll:
        return"you wins !"
    elif computer_roll>player_roll:
        return "computer wins!"
    else:
        return "its a tie !"
    

