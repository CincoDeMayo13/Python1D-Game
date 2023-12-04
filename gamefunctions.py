from shared_variables import closefriendpoints, knowledgepoints, socialpoints, lovelifepoints, fifthrowpoints,extremeending, belowaverageending, multipleending
import itertools

def display_menu():
        print("""
        SUTD simulator
        Main menu
        1. Start Game
        2. Exit Game
    """)
        
def exit_text():
    print("""
        Thank you for playing the game, we hope you have a nice time and enjoyed yourself.
        Please drop by https://github.com/CincoDeMayo13/Python1D-Game if you have feedbacks or if you are curious about the codes.
    """)

def char_selection():
    print("""
        Please select:
        1: If you are a boy
        2: If you are a girl
    """)
    choice = int(input())
    return choice

def post_char_selection(name):
        print("\nDear {}".format(name))
        print(
        """
        Heartiest congratulations from SUTD!
        Thank you for applying to SUTD and participating in our interview process.
        The University Admission Selection Committee believes you will be an excellent fit for SUTD and will flourish due to the unique education experience we offer. 
        We are pleased to offer you admission to the undergraduate programme at SUTD commencing September 2023, as well as a Tuition Grant that allows you to pay subsidised tuition fees for the normal duration of the programme.
        As the top emerging engineering education institution in the world', SUTD's hallmark is our one-of-a-kind, design-centric,\n        interdisciplinary curriculum blending liberal arts with science and technology - delivered through hands-on, cohort-based active learning.
        In SUTD, you will get to fully explore your interests in our stimulating Freshmore terms before selecting your major at the end of Term 3.
        The majors, along with the study of Humanities, Arts, and Social Sciences (HASS), offer an innovative engineering and architectural education that will prepare you for our fast-changing global environment.
        You will also have the option to take a minor to expand your knowledge beyond your major, thus enriching your learning experience.
        Our curriculum grooms you to be highly versatile, and prepares you for roles that involve design, technological expertise, leadership skills and creative thinking - competencies that are in high demand by today's employers.
        Your academic growth and personal development will be further enhanced by access to our team of dedicated and award-winning professors. cutting edge research and exceptional facilities. 
        Our students enjoy a rich selection of internship opportunities, overseas student exchanges, entrepreneurship activities, student organisations and a vibrant campus life. 
        Since the beginning, SUTD's boutique-style, academically rigorous programme has graduated cohorts of students who have attained employment at top corporations and organizations,\n        consistently drawing the highest median starting salaries among all local university graduates.
        """
        )

def test():
    global closefriendpoints
    global knowledgepoints
    global socialpoints
    global lovelifepoints
    global fifthrowpoints

    if closefriendpoints != 0: print("Success")

def book_in_arc():

    global closefriendpoints
    global knowledgepoints
    global socialpoints
    global lovelifepoints
    global fifthrowpoints

    choice = 0
    secondchoice = 0

    print("You are now starting the 'Book In Arc'\n")    

    print("""
    While shifting into dorm, after introducing yourself to your roommate, you:
    1. Continue having a wholesome conversation with your roommate
    2. Go out to say hi to your level mates
    3. Find out all the administrative matters to prepare for school
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())

    if choice == 1:
        closefriendpoints += 10

        print("""
    It is approaching lunchtime! You:
    1. Ask your roommate out for lunch at CCP
    2. Go around your level and casually slot yourself into a group going for lunch
    3. Cook maggie and start finding out administrative matters to prepare for school
    """)
        while secondchoice != 1 and secondchoice != 2 and secondchoice != 3:
            secondchoice = int(input())

        if secondchoice == 1:
            closefriendpoints += 10
        elif secondchoice == 2:
            socialpoints += 10
        elif secondchoice == 3:
            knowledgepoints += 10
    
    elif choice == 2:
        socialpoints += 10

        print("""
    Good job! You have made yourself known to your new cooler level mates and they ask you out for lunch, you:
    1. Accept with enthusiasm (+20 social life)
    2. Remembered that you love your roommate so you ask that your roommate joins
    3. Kindly reject, saying that you have a cooler roommate to eat with
    4. Cook maggie and start finding out administrative matters to prepare for school
    """)
        while secondchoice != 1 and secondchoice != 2 and secondchoice != 3 and secondchoice != 4:
            secondchoice = int(input())

        if secondchoice == 1:
            socialpoints += 20
        elif secondchoice == 2:
            socialpoints += 10
            closefriendpoints += 10
        elif secondchoice == 3:
            closefriendpoints += 20
        elif secondchoice == 4:
            knowledgepoints += 10

    elif choice == 3:
        knowledgepoints += 20

        print("""
    While you are being antisocial, your roommate asks if you want to have lunch! You:
    1. Say ‘Yes! About time you asked’
    2. Ask if your roommate wants to go with any other level mates
    3. Say your parents cook for you already and its time to go home 
    """)
        
        while secondchoice != 1 and secondchoice != 2 and secondchoice != 3:
            secondchoice = int(input())

        if secondchoice == 1:
            closefriendpoints += 10
        elif secondchoice == 2:
            socialpoints += 10
            closefriendpoints += 10

    #reset
    choice = 0
    secondchoice = 0

    print("""
    After unpacking you looked through your email and notice that there is a fifth row fair that afternoon. Knowing that you have orientation the next day, you:
    1. Ask your roommate if he/she would like to go with you to the fifth row fair
    2. Spend the afternoon going to the fifth row fair to explore your interest
    3. Go to library to study
    4. Sleep because you are tired from unpacking 
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())
    
    if choice == 1:
        fifthrowpoints += 10
        closefriendpoints += 10
    elif choice == 2:
        fifthrowpoints += 10
    elif choice == 3:
        knowledgepoints += 10

    #reset
    choice = 0 
    secondchoice = 0

    print("""
    Today, SUTD is holding fifth row fair, you
    1. Ask your roommate if he/she would like to go with you to the fifth row fair
    2. Go with your level mates
    3. Go to the fair by yourself and fast game find out so you can meet your other friends at NUS Utown for dinner!
    4. Start looking at lecture notes because fifth rows don’t add to GPA
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())

    if choice == 1:
        fifthrowpoints += 10
        closefriendpoints += 10

        print("""
    You found out that your roommate likes the otaku club! You:
    1. Agree to attend with him/her for fun
    2. You tell him/her that he/she is a weirdo and proceed to join what you want
    3. Convince him/her to join your favourite fifth row
    4. Go join the fifth rows with the pretty girls/ handsome boys that you are infatuated with
    """)
        
        while secondchoice != 1 and secondchoice != 2 and secondchoice != 3:
            secondchoice = int(input())

        if secondchoice == 1:
            closefriendpoints += 10
        elif secondchoice == 2:
            closefriendpoints += -10
            fifthrowpoints += 10
        elif secondchoice == 3:
            closefriendpoints += 10
            fifthrowpoints += 10
        elif secondchoice == 4:
            lovelifepoints += 10
            fifthrowpoints += 10

    elif choice == 2:
        fifthrowpoints += 10
        socialpoints += 10

        print("""
    You were surprised that in your friend group, a pretty girl/ handsome boy has tagged along! You:
    1. Hit on him/her
    2. Find out what she/he is joining and pretend you also like it so you can meet him/her more
    3. Stay focused and join what you really are interested in
    4. Join what your other friends want to
    """)
        
        while secondchoice != 1 and secondchoice != 2 and secondchoice != 3:
            secondchoice = int(input())

        if secondchoice == 1:
            lovelifepoints += 10
            socialpoints += -10
        elif secondchoice == 2:
            fifthrowpoints += 10
            lovelifepoints += 10
        elif secondchoice == 3:
            fifthrowpoints += 20
        elif secondchoice == 4:
            socialpoints += 10
            fifthrowpoints += 10
    
    elif choice == 3:
        fifthrowpoints += 10
        socialpoints += 10
    elif choice == 4:
        knowledgepoints += 10

    print("You have come to the end of the 'Book In Arc'\n")

def orientation_arc():
    global closefriendpoints
    global knowledgepoints
    global socialpoints
    global lovelifepoints
    global fifthrowpoints

    choice = 0

    print("You are now starting the 'Orientation Arc'\n")

    print("""
    You are placed in the group Lazarus. You walk into the sports hall and spotted your allocated group, you choose to sit:
    1. Where there is most space
    2. Beside The girl/guy you think is cute (uhoh you now have a crush)
    3. Beside your roommate
    4. Anyone because you want to know more people
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())

    if choice == 2:
        lovelifepoints += 10
    elif choice == 3:
        closefriendpoints += 10
    elif choice == 4:
        socialpoints += 10
    
    #reset
    choice = 0

    print("""
    First day was fun, you made some new friends its time to sleep for day 2 at Sentosa beach. The next day you woke up feeling tired, you:
    1. Skip to sleep in
    2. Wake up anyways to get ready for the beach
    3. Ask if your roommate wants to skip with you
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())

    if choice == 1:
        socialpoints += -10
    elif choice == 2:
        socialpoints += 20
    elif choice == 3:
        closefriendpoints += 10
        socialpoints += 10
    
    #reset
    choice = 0

    print("""
    It’s a sunny day at the beach, you:
    1. Hide in the shade alone because you can’t stand Singapore’s weather
    2. Take part in the activities because they seem fun
    3. Secretly leave to go back hall to rest
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())
    
    if choice == 1:
        socialpoints += -10
    elif choice == 2:
        socialpoints += 10
    elif choice == 3:
        socialpoints += -10

    #reset
    choice = 0

    print("""
    It’s the last day of orientation, there is a social night filled with music and dancing, you:
    1. Skip because you really tired cannot take it anymore
    2. Attend to see what’s up
    3. Ask your crush if he/she wants to have dinner with you first before going together
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())
    
    if choice == 1:
        socialpoints += -10
    elif choice == 2:
        socialpoints += 10
    elif choice == 3:
        lovelifepoints += 10

    print("You have come to the end of the 'Orientation Arc'\n")

def school_life_arc():
    global closefriendpoints
    global knowledgepoints
    global socialpoints
    global lovelifepoints
    global fifthrowpoints
    
    choice = 0

    print("You are now starting the 'School Life Arc'\n")

    print("""
    Its the first day of school and youre choosing what to wear for your first class, you:
    1. Dress to impress
    2. Old class tshirt, shorts and slippers
    3. Dress like a hippie to stand out
    4. Let your roommate pick your outfit
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())

    if choice == 4:
        closefriendpoints += 10

    #reset
    choice = 0 

    print("""
    In the blink of an eye, mid-terms are nearing yet you have lessons in the afternoon, you:
    1. Skip class to take an afternoon nap
    2. Skip class to go for fifth row
    3. Study with your roommate in hall
    4. Ask if anyone is willing to skip with you to have lunch
    5. Study with the love of your life after lesson
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        choice = int(input())

    if choice == 2:
        fifthrowpoints += 20
    elif choice == 3:
        closefriendpoints += 10
    elif choice == 4:
        socialpoints += 10
        knowledgepoints += -10
    elif choice == 5:
        lovelifepoints += 10
        knowledgepoints += 10
    
    #reset
    choice = 0

    print("""
    It’s week 9 and it’s just another normal day of school. After school, you:
    1. Ask your crush out for dinner
    2. Revise cause passing is not good enough for a pass/fail mod
    3. Attend fifthrow
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())

    if choice == 1:
        lovelifepoints += 10
    elif choice == 2:
        knowledgepoints += 10
    elif choice == 3:
        fifthrowpoints += 10

    #reset
    choice = 0

    print("""
    Congratulations! You won a pair of coldplay tickets from the parachute competition, you:
    1. Invite your crush
    2. Invite your roommate
    3. Sell the tickets on carousell 
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())

    if choice == 1:
        lovelifepoints += 10
    elif choice == 2:
        closefriendpoints += 10

    #reset
    choice = 0

    print("""
    Uhoh! A wild 2d project appeared! you:
    1. Do the bare minimum so you can attend fifth row
    2. Ditch your own project to help your crush do his/her portion of work
    3. Who cares about projects? Self study more important
    """)

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input())
    
    if choice == 1:
        fifthrowpoints += 20
        knowledgepoints += -10
    elif choice == 2:
        lovelifepoints += 20
        socialpoints += -10
    elif choice == 3:
        knowledgepoints += 10
    
    print("You have come to the end of the 'School Life Arc'\n")

def hall_life_arc():    
    global closefriendpoints
    global knowledgepoints
    global socialpoints
    global lovelifepoints
    global fifthrowpoints

    choice = 0

    print("You are now starting the 'Hall Life Arc'\n")

    print("""
    It’s week 10 and there is a hall event going on, you:
    1. Go for it to let loose and support your friend who is hosting
    2. Skip to study
    3. Ask your crush to go with you
    4. Attend to take the free food for you and your roommate
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())

    if choice == 1:
        socialpoints += 10
    elif choice == 2:
        knowledgepoints += 10
        socialpoints += -10
    elif choice == 3:
        lovelifepoints += 10
    elif choice == 4:
        closefriendpoints += 10

    #reset
    choice = 0

    print("""
    Every wednesday night, you decide to:
    1. Cook dinner with your friends
    2. Play board games with your friends 
    3. Attend fifth row 
    4. Study date with your crush
    5. Study alone in hall
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        choice = int(input())

    if choice == 1:
        socialpoints += 10
    elif choice == 2:
        socialpoints += 10
    elif choice == 3:
        fifthrowpoints += 10
    elif choice == 4:
        lovelifepoints += 10
    elif choice == 5:
        knowledgepoints += 10
        socialpoints += -10

    #reset
    choice = 0

    print("""
    It’s nearing the end of the month and you’re running low on cash, you:
    1. Meal prep with your friends
    2. Cook maggie in hall and study
    3. Stop going changi city point to have dinner and go canteen dabao caifan instead
    4. Sleep the hunger away
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())
    
    if choice == 1:
        socialpoints += 10
    elif choice == 2:
        knowledgepoints += 10

    #reset
    choice = 0

    print("""
    It’s the end of the term! To celebrate, you:
    1. Bring your crush to an exquisite restaurant - bistro in SUTD
    2. Go for fifth row because training/practice is the most important
    3. Mug hard for term 2 because term 1 was too easy
    4. Ask your roommate if he/she wants to throw a hall party in your dorm
    """)

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        choice = int(input())

    if choice == 1:
        lovelifepoints += 10
    elif choice == 2:
        fifthrowpoints += 10
    elif choice == 3: 
        knowledgepoints += 10
    elif choice == 4:
        socialpoints += 10
        closefriendpoints += 10

    print("You have come to the end of the 'Hall Life Arc'\n")

def check_multiple_endings(*args):
    global multipleending
    count = 0

    for var in args:
        if var == lovelifepoints and var >= 100 and var :
            count += 1

        if var == knowledgepoints and var >= 100:
            count += 1

        if var == socialpoints and var >= 130:
            count += 1

        if var == lovelifepoints and var >= 110:
            count += 1

        if var == fifthrowpoints and var >= 100:
            count += 1

    if count >= 2:
        multipleending = True

    return count >= 2

def check_extreme_endings(*args):
    global extremeending

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
        print("You have the following extreme endings:")
        print(printingstatement)
        extremeending = True
    else:
        print("You have no extreme endings.\n")

def check_below_average_endings(*args):
        global belowaverageending

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
            print("You have the following below average endings:")
            print(printingstatement)
            belowaverageending = True
        else:
            print("You have no below average endings.\n")

def which_multiple_endings(*args):
    count = 0
    statement = ""
    for a, b in itertools.combinations(args, 2):
        if (a == lovelifepoints and a >= 110):
            if (b == closefriendpoints and a >= 100):
                count += 1
                statement = "You are quiet but empathetic and kind. You are an intimate person who may be less known by the masses, but are cherished by the closest ones around you"
            elif (b == fifthrowpoints and a >= 100):
                count += 1
                statement = "You are a homie. You are set for life knowing you have a loving partner and continue to focus on the things you like to do."
            elif (b == socialpoints and a >= 130):
                count += 1
                statement = "You are a person people love hanging out with. You are enthusiastic and spontaneous, and you certainly know how to make people around you feel good"
            elif (b == knowledgepoints and a >= 100):
                count += 1
                statement = "You have great management skills. You know how to achieve balance between love and studies. This highlights your maturity amidst your peers"
        elif (a == lovelifepoints and a >= 110):
            if (b == fifthrowpoints and a >= 100):
                count += 1
                statement = "You are pragmatic, you know that life is short and you prefer doing the things you love and you know that  your close friend is probably the only friend that will last till your funeral."
            elif (b == knowledgepoints and a >= 100):
                count += 1
                statement = "You may seem pretty shy, but you are actually very introspective, and spend a lot of time thinking about everything. Having a close friend gives you the space to share your insights and form extremely meaningful conversations."
            elif (b == socialpoints and a >= 130):
                count += 1
                statement = "You are a helpful and interactive person. You value friendship and can easily blend into any groups of people, making you somebody everyone can count on"

        elif (a == knowledgepoints and a >= 100):
            if (b == fifthrowpoints and a >= 100):
                count += 1
                statement = "An all rounder, doing well in more than just academics. You have extremely high employability because of your unique skills and knowledge"
            elif (b == socialpoints and a >= 130):
                count += 1
                statement = "You are witty and vocal. People know you for your ability to help others through your skills and knowledge"

        if count > 0:
            print("You have the following special endings:")
            print(statement)
        else:
            print("You have no special endings.\n")

def ending_points_summary():
    global closefriendpoints
    global knowledgepoints
    global socialpoints
    global lovelifepoints
    global fifthrowpoints
    global multipleending
    global extremeending
    global belowaverageending

    #summary of points
    print("You've earned the following:")
    print("Close Friends Points:", closefriendpoints)
    print("Knowledge Points:", knowledgepoints)
    print("Social Points:", socialpoints)
    print("Love Life Points:", lovelifepoints)
    print("Fifth Row Points:", fifthrowpoints)
    print("\n")

    #check multiple above average endings
    if check_multiple_endings(closefriendpoints, knowledgepoints, socialpoints, lovelifepoints, fifthrowpoints):  
        which_multiple_endings(lovelifepoints, closefriendpoints, knowledgepoints, socialpoints, fifthrowpoints)

    #check extreme endings
    check_extreme_endings(closefriendpoints, knowledgepoints, socialpoints, lovelifepoints, fifthrowpoints)

    #check below average endings
    check_below_average_endings(closefriendpoints, knowledgepoints, socialpoints, lovelifepoints, fifthrowpoints)

    if (multipleending != True and extremeending != True and belowaverageending != True):
        print("You're just another average joe. Nothing wrong with that as long as you had fun lol.")
