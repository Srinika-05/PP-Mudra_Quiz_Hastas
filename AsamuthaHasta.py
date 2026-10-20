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


count = 0
score = 0

print("Hello! This is the Asamyutha Hasta Quiz. Please follow the directions!\n")

wordMeans = nextWord()
userGuess = input("Type your answer in lowercase: \n")

while count < 4:
    if userGuess == wordMeans:
        print("\nCorrect meaning!")
        count += 1
        #score += 1
        print("\nNext Round: \n")
        wordMeans = nextWord()
        userGuess = input("Type your answer in lowercase: \n")
    else:
        print("\nIncorrect answer. The answer was: \n" + wordMeans)
        wordMeans = nextWord()
        userGuess = input("Type your answer in lowercase: \n")
        


#print("Points you got: " + str(score))

    

# count += 1
# print("\nYour final score: " + str(count) + "/5")


# if userInput == word1: 
#     print("\nCorrect!")
# else:
#     print("\nOh wrong answer. Try again!")
#     userInput = input("Type your answer: \n")
#     if userInput == word1: 
#         print("\nCorrect!")

    
