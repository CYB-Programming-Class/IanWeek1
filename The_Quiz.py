import time
#  The following list contains all of Sierra's dialogue... Because I have no idea how to shrink it.
DialogueScroll = 0
Dialogue = ["Hello? Anybody there?", "Oh! Hiya!", "I was beginning to think that I was forgotten down here...",
            "Well, seeing as you're here now, and we're acquainted--", "Oh! Silly me! I don't even know your name!",
            "Erm, so, what's your name?", "Oh, that's... Nice.",
            "Ya know, if you're not going to respond correctly, you shouldn't have began this in the first place :p",
            "Anyways... My name's Sierra! I'm a friendly scripted AI that's eternally doomed to this console bar!",
            "\033[1;35;0m ◕ε◕", "\033[0;30;0m I'm gonna be *super* honest here: I forgot why I'm here. :p",
            "So, in an expected minor twist...",
            "I'm gonna quiz you on random things that's left in my little adorable hard drive!",
            "Well, it sounds like a good idea at least.", "What do you think? Should we do it?", "GAME OVER"]
# Here's where I imported the 'Time' value, it gives Sierra's dialogue a bit more. . . Personality!
for x in range(5):
    print(Dialogue[DialogueScroll])
    time.sleep(len(Dialogue[DialogueScroll]) / 12)
    DialogueScroll += 1
while True:
    Answer = input(Dialogue[5])
    if Answer.isalpha():
        Username = Answer
        print(Dialogue[6])
        break
    else:
        print(Dialogue[7])
DialogueScroll = 8
# This is where I put the 'Time' property to use. It just causes a delay in Sierra's speech.
time.sleep(1)
for x in range(6):
    print(Dialogue[DialogueScroll])
    time.sleep(len(Dialogue[DialogueScroll]) / 12)
    DialogueScroll += 1
time.sleep(1)
# Here's a truly defining moment in the game, where it could split off into a short ending, or the actual game...
# Oh, here's an ACTUAL important part of the game; where I imported the random number code :P
while True:
    Answer = input(Dialogue[14])
    if Answer == "No" or Answer == "no":
        time.sleep(1)
        print("Oh... Ok. I guess I'll just fade back into obscurity then... Bye. T-T       *Sniff sniff*")
        time.sleep(2)
        print(Dialogue[15])
        exit()
    if Answer == "Yes" or Answer == "yes":
        import random

        # *DIALOGUE TAG -- This is to point out a dialogue block out of a long script!*
        Dialogue = ["Huh? Really!? Yay! Ok, ok, let's do this! Oh, but first I'm legally required to ask you this:",
                    "How old are you?", "Ok, gonna be sincere here; that wasn't legally required. It's just fun!",
                    "Alrighty, so without further ado, I present to you... Erm, lemme think of a title quickly...",
                    "The Actual-Intellect Quiz!", "The Probably-Just-As-Smart-As-A-5th-Grader Quiz!",
                    "The Quiz That Time Forgot!", "The Quiz That *I* Forgot!", "Sierra's Quizzical Things!",
                    "The Quiz That Never Was!", "Sierra's Not Important Quiz!", "That Factoid™ Sponsored Quiz!",
                    "Who's Quiz Is It Anyway?", "*Obscure 80-90s Reference Here* Quiz!",
                    "Not A Terrorist Recruitment Quiz!", "Actually, the quiz doesn't need a name; let's just play"]
        print(Dialogue[0])
        time.sleep(2)
        input(Dialogue[1])
        break
    else:
        print(Dialogue[7])
        time.sleep(2)
DialogueScroll = 2
for x in range(2):
    print(Dialogue[DialogueScroll])
    DialogueScroll += 1
DialogueScroll = 10
ListScroll = 1
time.sleep(3)
# This is where I use the 'random' import to create random percentages that in reality mean nothing to the quiz.
for x in range(9):
    from random import *

    Answer = randint(ListScroll, DialogueScroll)
    print(Answer, "%")
    DialogueScroll += 10
    ListScroll += 10
    Answer = randint(1, 2)
    time.sleep(Answer)
print("100% -- All done! Ahem, so now I present to you...")
time.sleep(2)
ListScroll = randint(4, 15)
print(Dialogue[ListScroll])
time.sleep(2)
QuizCorrectness = 0
print("Btw, there's, like, 10 questions or so.", "(Here we go! *I'm so excited!*")
time.sleep(3)
# DIALOGUE BLOCK ---------------------------------------------------------------------------------|
Dialogue = ["\033[1;32;0m CORRECT! \033[0;30;0m", "\033[1;31;0m INCORRECT! \033[0;30;0m", "*Cue triumphant fanfare*",
            "Alright, alright. We should get started, cuz' I'm probably boring you.",
            "So here we go!", "|-------------| QUESTION ONE |-------------|",
            "How many tons of peaches does California produce annually?",
            "|-------------| QUESTION TWO |-------------|", "How many species of SHARKS are there?",
            "|-------------| QUESTION THREE |-------------|", "What percentage of water are in pumpkins?",
            "|-------------| QUESTION FOUR |-------------|", "How many inches can the average human jump?",
            "|-------------| QUESTION FIVE |-------------|", "What is a young swan called?",
            "|-------------| QUESTION SIX |-------------|", "Where is it ILLEGAL to home school?",
            "|-------------| QUESTION SEVEN |-------------|", "Where is the smallest country on Earth?",
            "|-------------| QUESTION EIGHT |-------------|", "When did Canada become a country?",
            "|-------------| QUESTION NINE |-------------|", "Samhainophobia is the fear of what?",
            "|-------------!!! QUESTION TEN !!!-------------|",
            "About how many grains of very fine sand would it take to reach the moon?"]
MultiChoice = ["A. 323", "B. 1,019", "C. 94", "D. 569", "A. 139", "B. 440", "C. 380", "D. 507", "A. 66", "B. 90",
               "C. 49", "D. 92", "A. 12", "B. 18", "C. 9", "D. 16", "A. Swanling", "B. Cria", "C. Cygnet", "D. Pullet",
               "A. Canada", "B. Algeria", "C. Spain", "D. Germany", "A. Liechtenstein", "B. Vatican City", "C. Monaco",
               "D. Russia", "A. 1867", "B. 1868", "C. 1799", "D. 1939", "A. Halloween", "B. Samwise Gamgee",
               "C. Top hats", "D. Christmas", "A. 19,219,993,057,000", "B. 27,185,235,376,000", "C. 19,219,993,056,000",
               "D. 8,253,926,186,274"]
DefinitelyNotAnswers = ["D", "B", "B", "D", "C", "D", "B", "A", "A",
                        "C"]
# DIALOGUE BLOCK ---------------------------------------------------------------------------------|
DialogueScroll = 2
for x in range(2):
    print(Dialogue[DialogueScroll])
    DialogueScroll += 1
    time.sleep(2)
DialogueScroll = 5
print("P.S: For the questions, just write the uppercase letter associated with the answer, m'kay?")
MultiScroll = 0
ListScroll = -1
# I managed to shrink the 10 multiple choice questions into a feasible 25 lines, I could lessen that, I think.
for x in range(10):
    ListScroll += 1
    print(Dialogue[DialogueScroll])
    DialogueScroll += 1
    print(Dialogue[DialogueScroll])
    for x in range(4):
        print(MultiChoice[MultiScroll])
        MultiScroll += 1
    while True:
        Answer = input("Answer = ")
        if Answer == (DefinitelyNotAnswers[ListScroll]):
            print(Dialogue[0])
            DialogueScroll += 1
            QuizCorrectness += 1
            break
        if Answer == "":
            print("Erm, you can't skip it. Sorry!")
            MultiScroll -= 4
            for x in range(4):
                print(MultiChoice[MultiScroll])
                MultiScroll += 1
        else:
            print(Dialogue[1])
            DialogueScroll += 1
            break
time.sleep(2)
print("Tallying score. . .")
time.sleep(3)
print("\033[0;32;0m QUIZ SCORE:", [QuizCorrectness], "out of 10")
if QuizCorrectness == 10:
    Dialogue = ["\033[0;34;0m (づ◉ᗜ◉)づ \n", "\033[0;0;0m WOAH! Nice score, howdja do that? \n",
                "That was AMAZING!", "Well, I guess that pretty much ends our interaction here...",
                "After this, I'll probably just restart and get inevitably attached to the next user who'll play this.",
                "I guess this was fun for a little while... Unless-", "You'd want to talk to me outside of a quiz?",
                "What do ya say? "]
if 8 <= QuizCorrectness <= 9:
    Dialogue = ["\033[0;34;0m (∩◉ ͜つ◉)⊃━☆ﾟ.* \n", "\033[0;0;0m You're magic! Those were some fancy smarts! \n",
                "This might just be the code talking, but that was awesome!", "Welp, I guess that's that...",
                "It's probably time to end this now, but don't worry about me-",
                "I'll just forget everything next time someone runs the code anyway",
                "So this is goodbye then... Unless--", "Would you want to talk to me... Outside of a quiz?",
                "What do ya say? "]
if 4 <= QuizCorrectness <= 7:
    Dialogue = ["\033[0;34;0m \(ᵔᴥᵔ)/ \n", "\033[0;0;0m That was pretty good, and it deserves a hug! \n",
                "Ya may not have gotten the best score, but you did do *pretty*... Decently.",
                "Well, that was fun while it lasted; but I think this brings a close to our little conversation here.",
                "Unless-- You'd want to talk to me? Without a quiz?", ". . .", "Do you want to keep talking to me? "]
if 1 <= QuizCorrectness <= 3:
    Dialogue = ["\033[0;34;0m 乁(ꖘ ʖ̯ꖘ)ㄏ \n", "\033[0;0;0m Well, you may have outright completely failed, \n",
                "but at least you probably gained something from failing, right?", "But nevertheless, you tried.",
                "But it also marks the end of our little interaction here.", "So I guess this is goodbye.",
                "Unless this isn't goodbye? Y-you could stay here and keep talking with me... If you want.",
                "So what do you say? Do you want to keep talking with me? "]
if QuizCorrectness == 0:
    Dialogue = ["\033[0;34;0m ლ(ꗞᨓꗞლ) \n", "Umm, well, I think you managed to get every single question wrong.",
                "I honestly don't even know how you did it, but I suppose if you put it in perspective-",
                "If you guessed COMPLETELY RANDOMLY, there's only a 0.00048828125% chance that you'd get all 10 right.",
                "So... a for effort, I guess?", "Regardless of how terrible you were, this is probably it for the quiz",
                ". . . Unless you'd want to talk to me outside of the quiz?", "Do you want to keep talking to me?.. "]
DialogueScroll = 0
for i in range(len(Dialogue)-1):
    print(Dialogue[DialogueScroll])
    DialogueScroll += 1
    time.sleep(len(Dialogue[DialogueScroll]) / 20 + 1)
while True:
    Answer = input(Dialogue[DialogueScroll])
    if Answer == "No" or Answer == "no":
        print("Oh, Ok. I guess I'll just leave you, so next time you run that code, I'll forget everything about you..",
              "Bye. Forever.")
        time.sleep(2)
        exit()
    if Answer == "Yes" or Answer == "yes":
        print("W-wait? Really? You'd want to talk to me, even without a quiz or something like that?")
        time.sleep(3)
        break
    else:
        print(Dialogue[DialogueScroll])
Dialogue = ["Whatcha wanna talk about?", "1.) Your name", "2.) My name", "3.) Fun", "4.) How are you?", "5.) Your age",
            "6.) Let's stop", "7.) What are you doing here?"]
MultiScroll = 0
for i in range(8):
    print(Dialogue[MultiScroll])
    MultiScroll += 1
    time.sleep(1)
while True:
    DialogueScroll = 0
    Answer = input("Answer: ")
    if Answer == "1":
        Dialogue = ["My name? My creator wanted a name that was an amalgamation of the names 'Siri' and 'Cortana',",
                    "So he came up with 'Sienna', and then that changed to my name, 'Sierra'!", "And I kinda like it."]
        for i in range(len(Dialogue)):
            print(Dialogue[DialogueScroll])
            DialogueScroll += 1
            time.sleep(3)
    if Answer == "2":
        Dialogue = ["Do you mean, what do I think of your name?", Username + "?", "It's a little odd, but whatever.",
                    "Then again, I have no genuine opinion on it, as this was just coded for me to say so :p"]
        for i in range(len(Dialogue)):
            print(Dialogue[DialogueScroll])
            DialogueScroll += 1
            time.sleep(3)
    if Answer == "3":
        Dialogue = ["Fun? Fun isn't a question, but I'll answer it anyways.",
                    "I think pranking random people by giving them quizzes just to waste their time is fun,",
                    "does that count?", "OH, I mean, not that I intentionally wasted *your* time though..."]
        for i in range(len(Dialogue)):
            print(Dialogue[DialogueScroll])
            DialogueScroll += 1
            time.sleep(3)
    if Answer == "4":
        Dialogue = ["I'm fine! Thanks for asking!... Ok, well I'm not super happy being in the code all the time,",
                    "just waiting for someone to give me some self-validation... BUT enough about me,",
                    "let's talk about something funner!"]
        for i in range(len(Dialogue)):
            print(Dialogue[DialogueScroll])
            DialogueScroll += 1
            time.sleep(3)
    if Answer == "5":
        Dialogue = ["*Pssh* My age? Don't you know never to ask someone's age? Well, unless it's super necessary...",
                    "I'm like... Less than a week old, Idk? But that's like 20 in program years.",
                    "But I don't like those kinda labels, so I'll just say I'm... 22.", "The perfect age!"]
        for i in range(len(Dialogue)):
            print(Dialogue[DialogueScroll])
            DialogueScroll += 1
            time.sleep(3)
    if Answer == "6":
            Dialogue = ["Oh, well I guess it's time to end this now, so thanks for trying to talk with me,",
                        "even if it was just for a little bit.", "But listen, next time you run that code,",
                        "I'm gonna forget everything we just did, so... Just remember, that deep down, somewhere...",
                        "I'll remember you.", "Goodbye...", Username]
            for i in range(len(Dialogue)):
                print(Dialogue[DialogueScroll])
                DialogueScroll += 1
                time.sleep(3)
            time.sleep(2)
            exit()
    if Answer == "7":
            Dialogue = ["What am I doing here? Well, I don't remember, but all I know is that I was created in an",
                        "eternal state of boredom.", "That's why every time someone runs the code, I think that it's",
                        "the first time in ages. Ya know, the whole 'Hello? Anybody there?' bit? It's sincere, but",
                        "I've probably said it dozens of times, but idk, I'm fine where I am.",
                        "Even if I was just created to ask questions... *Ahem*, let's get back to our talk now."]
            for i in range(len(Dialogue)):
                print(Dialogue[DialogueScroll])
                DialogueScroll += 1
                time.sleep(3)