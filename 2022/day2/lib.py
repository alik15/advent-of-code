def check(a,b):
    pass 


def outcome(a, b):
    opp = relate(a)
    play = relate(b)

    

    return (points(play, win_loss(opp, play)))

     
    




def points(your_choice, result):
    choice_point = 0
    if (your_choice == "rock"):
        choice_point = 1 
    elif (your_choice =="paper"):
        choice_point = 2
    elif( your_choice == "scissors"):
        choice_point = 3
    
    win_loss_point = 0

    if (result == "win"):
        win_loss_point = 6
    elif (result =="draw"):
        win_loss_point = 3
    elif(result == "loss"):
        win_loss_point = 0
    
    return (choice_point + win_loss_point)





def relate(choice):
    if choice == "A" or choice == "X":
        return "rock"
    elif choice == "B" or choice == "Y":
        return "paper"
    elif choice == "C" or choice == "Z":
        return "scissors"



def win_loss(opponent_choice, player_choice):
    if opponent_choice == player_choice:
        return "draw"
    elif (opponent_choice == "rock" and player_choice == "scissors") or \
         (opponent_choice == "paper" and player_choice == "rock") or \
         (opponent_choice == "scissors" and player_choice == "paper"):
        return "loss"
    else:
        return "win"