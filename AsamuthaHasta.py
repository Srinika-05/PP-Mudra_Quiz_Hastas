import random

AsamyutaHasta = ["pathaka" , "tripataka" , "ardhapataka" , "kartharimukha" , "mayura" , 
                 "ardhachandra" , "arala" , "sukatunda" , "musthi" , "shikara" , 
                 "kapittha" , "katakamukha" , "soochi" , "chandrakala" , "padmakosha" , 
                 "sarpashirsa" , "mrgasirsa" , "simhamukha" , "kangula" , "alapadma" , 
                 "chatura" , "bharama" , "hamsasya" , "hamsapaksa" , "sandamsa" , "mukula" ,
                 "thamrachuda" , "trisula"]

AHmeaning = ["flag" , "flag with three corners" , "half flag" , "scissors" , "peacock" ,
             "half moon" , "bent" , "parrots head" , "fist" , "peak of a mountain" , 
             "woodapple" , "bracelet" , "needle" , "moon" , "lotus bud" , "snakes head" , 
             "deers head" , "lions head" , "bud" , "fully bloomed lotus" , "square" ,
             "bee" , "swan beak" , "swan wing" , "pincers" , "blossom" , "cock" , "trident"]


def nextWord():
    meaning = random.choice(AHmeaning)
    corespword = AHmeaning.index(meaning)
    word = AsamyutaHasta[corespword]

    print("What does the word\n" + word + "\nmean? ")
    AsamyutaHasta.pop(corespword)
    AHmeaning.pop(corespword)

    return meaning


def startAHgame():
    count = 0
    score = 0

    print("---------------------------------------------------------------------------")
    print("Hello! This is the Asamyutha Hasta Quiz. Please follow the directions!\n")


    wordMeans = nextWord()
    userGuess = input("Type your answer in lowercase: \n").lower()

    while count < 5:
        if userGuess == wordMeans:
            print("\nCorrect meaning!")
            
            score += 1
            print("\nNext Round: \n")
            wordMeans = nextWord()
            userGuess = input("Type your answer in lowercase: \n")
        else:
            print("\nIncorrect answer. The answer was: \n" + wordMeans + "\n")
            wordMeans = nextWord()
            userGuess = input("Type your answer in lowercase: \n")


        count += 1
        
            


    print("Points you got: " + str(score))

        

    print("\nYour final score: " + str(count) + "/6")


def startSHgame():
    print("Samyutha Hastas game now")


start = True

startGame = input("Are you ready to start the quiz? First, you will be assessed on Asamyutha Hastasn\n" \
"Type in yes or no to start (y/n)\n").lower()


if startGame == "y":
    startAHgame()
    start = True
else:
    start = False
    

while start == True:

    tryAgain = input("Would you like to try again? (y/n)").lower()

    if tryAgain == "y":
        startAHgame()
    elif tryAgain == "n":
        shgame = input("Would you like to start the Samyutha hastas quiz? (y/n)")
        if shgame == "y":
            startSHgame()
        elif shgame == "n":
            start = False
            quit
        



    
