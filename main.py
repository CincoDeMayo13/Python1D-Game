# question_bank = {
#    "Time Management" :, 
#    "Academic Challenges" :,
#    "Scores" :,
#    "Social Connections" :,
#    "Internship Opportunity" :,
#    "Leadership Role" :,
#    "Financial Management" :,
#    "Time Management" :,
#    "Time Management" :,
#    "Time Management" :,
#    "Time Management" :,
#    "Time Management" :,
#    "Time Management" :,
#    "Time Management" :,
#    "Time Management" :,
# }



start =  True
while start:    
    #display menu
    print("""
        SUTD simulator
        Main menu
        1. Start Game
        2. Leaderboard
        3. Exit Game
    """)
    #prompt for what player wishes to do
    option = int(input("What would you like to do"))
    if option == 1:
        print(
        """
            _\|/^
            (_oo
            |     
            /|\c ---> Admission staff
            |
            LL
        """
        )

        name=""
        looping = True
        while looping:
            character = int(input("'Are you a boy(1) or a girl(2)?' "))
            if character == 1:
                name = "Jesca"
                looping = False
            elif character == 2:
                name = "Jovito"
                looping = False
            else:
                print("'There's only 2 genders!'")
        

        print("Dear {}".format(name))
        print(
        """"
        Heartiest congratulations from SUTD!1
        Thank you for applying to SUTD and participating in our interview process.
        The University Admission Selection Committee believes you will be an excellent fit for SUTD and will flourish due to the unique education experience we offer. 
        We are pleased to offer you admission to the undergraduate programme at SUTD commencing September 2023, as well as a Tuition Grant that allows you to pay subsidised tuition fees for the normal duration of the programme.
        As the top emerging engineering education institution in the world', SUTD's hallmark is our one-of-a-kind, design-centric, interdisciplinary curriculum blending liberal arts with science and technology - delivered through hands-on, cohort-based active learning.
        In SUTD, you will get to fully explore your interests in our stimulating Freshmore terms before selecting your major at the end of Term 3.
        The majors, along with the study of Humanities, Arts, and Social Sciences (HASS), offer an innovative engineering and architectural education that will prepare you for our fast-changing global environment.
        You will also have the option to take a minor to expand your knowledge beyond your major, thus enriching your learning experience.
        Our curriculum grooms you to be highly versatile, and prepares you for roles that involve design, technological expertise, leadership skills and creative thinking - competencies that are in high demand by today's employers.
        Your academic growth and personal development will be further enhanced by access to our team of dedicated and award-winning professors. cutting edge research and exceptional facilities. 
        Our students enjoy a rich selection of internship opportunities, overseas student exchanges, entrepreneurship activities, student organisations and a vibrant campus life. 
        Since the beginning, SUTD's boutique-style, academically rigorous programme has graduated cohorts of students who have attained employment at top corporations and organizations, consistently drawing the highest median starting salaries among all local university graduates.
        """
        )


    elif option == 2:
        #read from txt file for previous scores
        pass
    elif option == 3:
        start = False
    else:
        print("Invalid option")
    