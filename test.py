
import itertools
#Ini points variables
closefriendpoints = 100
knowledgepoints = 100
socialpoints = 100
lovelifepoints = 100
fifthrowpoints = 100

def which_multiple_endings(*args):
    statement = ""
    for a, b in itertools.combinations(args, 2):
        if (a == lovelifepoints and a >= 110):
            if (b == closefriendpoints and a >= 100):
                statement = "You are quiet but empathetic and kind. You are an intimate person who may be less known by the masses, but are cherished by the closest ones around you"
            elif (b == fifthrowpoints and a >= 100):
                statement = "You are a homie. You are set for life knowing you have a loving partner and continue to focus on the things you like to do."
            elif (b == socialpoints and a >= 130):
                statement = "You are a person people love hanging out with. You are enthusiastic and spontaneous, and you certainly know how to make people around you feel good"
            elif (b == knowledgepoints and a >= 100):
                statement = "You have great management skills. You know how to achieve balance between love and studies. This highlights your maturity amidst your peers"
        elif (a == lovelifepoints and a >= 110):
            if (b == fifthrowpoints and a >= 100):
                statement = "You are pragmatic, you know that life is short and you prefer doing the things you love and you know that  your close friend is probably the only friend that will last till your funeral."
            elif (b == knowledgepoints and a >= 100):
                statement = "You may seem pretty shy, but you are actually very introspective, and spend a lot of time thinking about everything. Having a close friend gives you the space to share your insights and form extremely meaningful conversations."
            elif (b == socialpoints and a >= 130):
                statement = "You are a helpful and interactive person. You value friendship and can easily blend into any groups of people, making you somebody everyone can count on"

        elif (a == knowledgepoints and a >= 100):
            if (b == fifthrowpoints and a >= 100):
                statement = "An all rounder, doing well in more than just academics. You have extremely high employability because of your unique skills and knowledge"
            elif (b == socialpoints and a >= 130):
                statement = "You are witty and vocal. People know you for your ability to help others through your skills and knowledge"
    print(statement)



which_multiple_endings(lovelifepoints, closefriendpoints, knowledgepoints, socialpoints, fifthrowpoints)

