#
# Project Rock Paper Scissors
#


# Import Random number module
import random

# Main function to run Janken

def main():
    gameBoolean = True
    gameScorePlayer = 0
    gameScoreCPU = 0

    while gameBoolean:
        gameUserInput = input("Choose one:\n1 - Rock\n2 - Paper\n3 - Scissors\n")
        # Generate a Random Number
        gameRandGen = random.randint(1,3)
        
        # Evaluate whether CPU or Player wins
        match int(gameUserInput):
            case 1:
                print("Player chooses Rock!\n")
                match int(gameRandGen):
                    case 1:
                        print("CPU chooses Rock!\nIt's a tie!\n")
                        #gameBoolean = False
                    case 2:
                        print("CPU chooses Paper!\nCPU Wins!\n")
                        gameScoreCPU = gameScoreCPU + 1
                        #gameBoolean = False
                    case 3:
                        print("CPU chooses Scissors!\nPlayer Wins!\n")
                        gameScorePlayer = gameScorePlayer + 1
                        #gameBoolean = False
            case 2:
                print("Player chooses Paper!\n")
                match int(gameRandGen):
                    case 1:
                        print("CPU chooses Rock!\nPlayer Wins!\n")
                        gameScorePlayer = gameScorePlayer + 1
                        #gameBoolean = False
                    case 2:
                        print("CPU chooses Paper!\nIt's a tie!\n")
                        #gameBoolean = False
                    case 3:
                        print("CPU chooses Scissors!\nCPU Wins!\n")
                        gameScoreCPU = gameScoreCPU + 1
                        #gameBoolean = False
            case 3:
                print("Player chooses Scissors!\n")
                match int(gameRandGen):
                    case 1:
                        print("CPU chooses Rock!\nCPU Wins!\n")
                        gameScoreCPU = gameScoreCPU + 1
                        #gameBoolean = False
                    case 2:
                        print("CPU chooses Paper!\nPlayer wins!\n")
                        gameScorePlayer = gameScorePlayer + 1
                        #gameBoolean = False
                    case 3:
                        print("CPU chooses Scissors!\nIt's a tie!\n")
                        #gameBoolean = False
            case _:        
                print("Please input a number 1, 2, or 3.\n")
        
        print("Player score:", str(gameScorePlayer), "\nCPU Score:", str(gameScoreCPU),"\n")

        if gameScorePlayer == 5:
            print("Player ultimately wins!!!\n")
            gameBoolean = False
        
        if gameScoreCPU == 5:
            print("CPU ultimately wins!!!\n")
            gameBoolean = False

if __name__ == "__main__":
    main()