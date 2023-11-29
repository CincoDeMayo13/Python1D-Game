def displaymenu():
        print("""
        SUTD simulator
        Main menu
        1. Start Game
        2. Leaderboard
        3. Exit Game
    """)
        
def exittext():
    print("""
        Thank you for playing the game, we hope you have a nice time and enjoyed yourself.
        Please drop by https://github.com/CincoDeMayo13/Python1D-Game if you have feedbacks or if you are curious about the codes.
    """)

def characterselection():
    print("""
        Please select:
        1: If you are a boy
        2: If you are a girl
    """)
    choice = int(input())
    return choice


def check_multiple_endings(*args):
    count = 0

    for var in args:
        if var == closefriendpoints and var >= 100:
            count += 1

        if var == knowledgepoints and var >= 100:
            count += 1

        if var == socialpoints and var >= 130:
            count += 1

        if var == lovelifepoints and var >= 110:
            count += 1

        if var == fifthrowpoints and var >= 100:
            count += 1

    return count >= 2


def check_extreme_endings(*args):
    count = 0
    printingstatement = ""
    for var in args:
        if count > 4:
          break
        if var == closefriendpoints and var >= 140:
            count += 1
            printingstatement += "Make sure you don’t become too clingy because your friend can move on anytime.\n"

        if var == knowledgepoints and var >= 160:
            count += 1
            printingstatement += "You ended up being the top of the cohort, but at what cost?\n"

        if var == socialpoints and var >= 200:
            count += 1
            printingstatement += "Uni to you is a place to have fun, know people and build connections. Screw the degree.\n"

        if var == lovelifepoints and var >= 150:
            count += 1
            printingstatement += "You are blinded by love. Everything you do is for your love.\n"

        if var == fifthrowpoints and var >= 140:
            count += 1
            printingstatement += "You are well-known only for being superb at your hobby.\n"

    if count > 0:
        print(printingstatement)
    else:
        print("You have no extreme endings.\n")

def check_good_endings(*args):
        count = 0
        printingstatement = ""
        for var in args:
            if var == closefriendpoints and var >= 100 and var < 140:
                count += 1
                printingstatement += ""

            if var == knowledgepoints and var >= 100 and var < 160:
                count += 1
                printingstatement += ""

            if var == socialpoints and var >= 100 and var < 200:
                count += 1
                printingstatement += ""

            if var == lovelifepoints and var >= 100 and var < 150:
                count += 1
                printingstatement += ""

            if var == fifthrowpoints and var >= 100 and var < 140:
                count += 1
                printingstatement += ""

        if count > 0:
            print(printingstatement)
        else:
            print("You have no good endings.\n")


def check_average_endings(*args):
        count = 0
        printingstatement = ""
        for var in args:
            if var == closefriendpoints and var >= 50 and var < 100:
                count += 1
                printingstatement += ""

            if var == knowledgepoints and var >= 50 and var < 100:
                count += 1
                printingstatement += ""

            if var == socialpoints and var >= 50 and var < 100:
                count += 1
                printingstatement += ""

            if var == lovelifepoints and var >= 50 and var < 100:
                count += 1
                printingstatement += ""

            if var == fifthrowpoints and var >= 50 and var < 100:
                count += 1
                printingstatement += ""

        if count > 0:
            print(printingstatement)
        else:
            print("You have no average endings.\n")

def check_below_average_endings(*args):
        count = 0
        printingstatement = ""
        for var in args:
            if var == closefriendpoints and var < 50:
                count += 1
                printingstatement += "You are a friend to some or many, but a confidant to none.\n"

            if var == knowledgepoints and var < 60:
                count += 1
                printingstatement += "Wake up your bloody idea! Your grades are like the titanic.\n"

            if var == socialpoints and var < 80:
                count += 1
                printingstatement += "You have no social life sadly.\n"

            if var == lovelifepoints and var < 60:
                count += 1
                printingstatement += "Beter love life next time!\n"

            if var == fifthrowpoints and var < 50:
                count += 1
                printingstatement += "You have no skills.\n"

        if count > 0:
            print(printingstatement)
        else:
            print("You have no below average endings.\n")

def which_multiple_endings(*args):
    count = 0

def ending_points_summary(*args):

    #check multiple above average endings
    if check_multiple_endings(*args):
        which_multiple_endings()
    
    #check extreme endings
    print("Extreme Endings:\n")
    check_extreme_endings()

    #check good endings
    print("Good Endings:\n")
    check_good_endings()

    #check average endings
    print("Average Endings:\n")
    check_average_endings()

    #check below average endings
    print("Below Average Endings:\n")
    check_below_average_endings()
