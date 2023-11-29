from gamefunctions import *

start =  True
while start:    
    #display menu
    display_menu()
    #prompt for what player wishes to do
    option = int(input("What would you like to do "))
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
            character = char_selection()
            if character == 1:
                name = "Jesca"
                looping = False
            elif character == 2:
                name = "Jovito"
                looping = False
            else:
                print("'There's only 2 genders!'")
        
        post_char_selection(name)

        #book in arc
        book_in_arc()
        
        #orientaion arc
        orientation_arc()

        #school life arc
        school_life_arc()

        #hall life arc
        hall_life_arc()

        #summary
        ending_points_summary()

    elif option == 2:
        start = False
        exit_text()
    else:
        print("Invalid option")
