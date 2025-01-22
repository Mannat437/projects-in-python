#defining a function to calculate sum of three variables
def calculate_sum(a,b,c):
    return a+b+c


#defining a function to print the board
def printboard(xstate,zstate):
    zero="X" if xstate[0] else ("O" if zstate[0] else 0)#if xstate[0] is true(1) than X will be displayeed else it will check the same condition for zstate and display O for true and place value for false
    one="X" if xstate[1] else ("O" if zstate[1] else 1) 
    two="X" if xstate[2] else ("O" if zstate[2] else 2) 
    three="X" if xstate[3] else ("O" if zstate[3] else 3) 
    four="X" if xstate[4] else ("O" if zstate[4] else 4) 
    five="X" if xstate[5] else ("O" if zstate[5] else 5) 
    six="X" if xstate[6] else ("O" if zstate[6] else 6) 
    seven="X" if xstate[7] else ("O" if zstate[7] else 7) 
    eight="X" if xstate[8] else ("O" if zstate[8] else 8) 
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


#here we are defining a function to check whether a person (X or O) has won
def checkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]#possible ways for winning
    for win in wins:
        if (calculate_sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("HURRAY!! X won the game ")
            return 1
        if (calculate_sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("HURRAY!! O won the game ")
            return 2
    return -1


#function for starting the game
def tic_tac_toe():
    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    turn=1 #1 for X and 0 for O
    chance=0#recording total chances in a game that is 9
    index=[]#list for storing the indexes where a person has already marked X or O
    while(True):
        printboard(xstate,zstate)
        if(turn == 1):
            print("X's chance")
            value=int(input("enter the place to set X: "))
            if value in index or value < 0 or value > 8:
                print("invalid move,try again")#raise error if the index is already marked or the index is out of range
            else:
                index.append(value)
                xstate[value]=1#set the value to true(1)
                turn=0 #giving next turn for O       
                chance+=1
        else:
            print("O's chance")
            value=int(input("enter the place to set O: "))
            if value in index or value < 0 or value > 8:
                print("invalid move,try again")
            else:
                index.append(value)
                zstate[value]=1
                turn=1        
                chance+=1
        cwin=checkwin(xstate,zstate)
        if cwin !=-1:#a person a won the game
            print("match over")
            break
        if chance == 9:#all the places in the board are filled whithout anyone winning
            print("It's a tie!")
            break
    
        
while(True):
    print("\nTIC TAC TOE\n")
    print("1. start a new game")
    print("2. quit")
    choice=input("enter your choice (1 or 2): ")
    if choice == '1':
        print("welcome to the game")
        tic_tac_toe()
    elif choice == '2':
        print("see you next time")
        break
    else:
        print("invalid choice")

        