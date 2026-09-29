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


word = random.choice(AHmeaning)
index = AHmeaning.index(word)

word1 = AsamyutaHasta[index]

print("What Asamutha Hasta meaning is \n" , word1 , "\nreffering to?")
userInput = input("Type your answer in lowercase: \n")

if userInput == word1: 
    print("\nCorrect!")
else:
    print("\nOh wrong answer. Try again!")
    userInput = input("Type your answer: \n")
    if userInput == word1: 
        print("\nCorrect!")

    
