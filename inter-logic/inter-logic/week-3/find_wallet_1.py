import random
import time

# an object describing our player
# .lower() , while , if true, continue, break if() or ()
# while true: if / else, continue / break
player = { 
    "name": "p1", 
    "items" : ["no Food"],
    "friends" : [],
    "location" : "start"
}

def introStory():
    # let's introduce them to our world
    print ("Welcome to another normal day of your life. What's your name?")
    player["name"] = input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print ("You received a text msg from your friend")
    time.sleep(3)
    print (">> 'Hey, " +  player["name"] +" !"+" We're still having dinner at 6, right?\
        \n>> 'Sorry, I think I might be a bit late. I'm looking for my wallet.'")
    print (">> 'No worries, but make sure to come asap!'")
    print (" It's your friend's birthday today and you are going to her birthday party.")
    print (" But you can't find your wallet! You need to snoop around fast to not be late.")
    chooseParty()

def chooseParty():
    pcmd = input("please choose 'let's go' or 'go back to sleep' >")
    # the player can choose yes or no
    if (pcmd == "let's go"):
        print ("'Meow!' Your cat Oscar wants to play with you.")
        input("press enter")
        findWallet()
    elif (pcmd == "go back to sleep"):
        print ("You missed the party and your friend cancelled you.")
        print ("TAT TAT TAT TAT TAT TAT TAT")
        pcmd = input("press enter")
        introStory() # repeat over and over until the player chooses yes!
    else:
        print ("I don't understand that")
        chooseParty() 
        
# two ending results

def badEnding():
    # printGraphic("wallet")
    print("-------------------------------")
    print("You were not able to find your wallet and missed the party. Your friend is very sad.")
    input("press enter")
    print("Friend: I'm disappointed at you, " + player["name"] ) # customized with a name
    input("press enter")
    return

def goodEnding():
    printGraphic("wallet")
    print("-------------------------------")
    print("You were able to find your wallet and joined the party. Your friend is very happy!")
    return

#How much cat food do we need? WIP
def guessWeight(minNum, maxNum):
    result = random.randint(minNum,maxNum)
    print ("How much grams of food do we need?")
    # input ("How much grams of food do we need?")
    print ("You guess: " + str(result) + " gram out of " + str(maxNum))

    #minimum must be 25Gram
    if (result <= 25):
        print ("try again....")
        input("press enter")
        guessWeight(minNum, maxNum) 

    return result

# FINDING WALLET JOURNEY STARTS     
def findWallet():
    printGraphic("yourRoom")
    print("You can either check your drawer, interact with your cat or talk to mom.")
    print ("Your options: [ drawer, cat , mom ]")
    pcmd = input(">") 

    #drawer path
    if (pcmd == "drawer"):
        printGraphic("drawer")
        goToDrawer()

    #cat path
    elif(pcmd == "cat"):
        printGraphic("CAT")
        goToCat()

    #mom path
    elif(pcmd == "mom"):
        goToMom()

    else:
        print ("I don't understand that")
        input("press enter")
        findWallet()

##DRAWER PATH
def goToDrawer():
    print ("Your options: [ open the drawer, check on top ]")
    pcmd = input(">") 
    
    if (pcmd == "open the drawer"):
        print("You found the cat food")
        input("press enter")
        print("You now have food for your cat, Oscar")
        player["items"].append("cat food")
        findWallet()
    
    elif (pcmd == "check on top"):
        print("There's nothing")
        input("press enter")
        findWallet()
    
    else:
        print ("I don't understand that")
        goToDrawer()

##MOM PATH
def goToMom():
    print('You can ask mom for help, ignore your mom or help her with chores.')
    print ("Your options: [ ask, ignore, help ]")
    pcmd = input(">") 

    if (pcmd == 'ask'):
        print('"Mom, have you seen my wallet?"')
        print('Your mom is angry at you for being careless. She yelled at you.')
        input("press enter")
        printGraphic("angrymom")
        input("press enter")
        badEnding()

    elif (pcmd == 'ignore'):
        print('You walked away.')
        print('Your mom is angry at you for being careless. She yelled at you.')
        input("press enter")
        printGraphic("angrymom")
        input("press enter")
        badEnding()

    elif (pcmd == 'help'):
        print('Your mom is very happy.')
        input("press enter")
        printGraphic("happymom")
        print('"That\'s wonderful! Can you feed the cat? Here\'s some cat food. Take as many as you want."')
        player["items"].append("cat food")
        # roll = rollDice(0, 20, difficulty)

        input("press enter")
        print("You now have food for your cat, Oscar")
        goToCat()
    
    #If user types in other
    else:
        print ("I don't understand that")
        goToMom()

##CAT PATH
def goToCat():
    print ("You can either talk to Oscar or feed him")
    print ("Your options: [talk, feed]")
    pcmd = input(">") #user choose

    def userHasCatFood():
        print('You give Oscar his food.')
        input("press enter")
        print('Oscar: Nice food, human. Here\'s your wallet meow.')
        input("press enter")
    
    def userHasNoCatFood():
        print('You don\'t have any food.')
        input("press enter")
        print('Oscar: No food? You\'re useless, human!')
        input("press enter")

    if (pcmd == 'talk'):
        print('Do you have my wallet?')
        print('Oscar: Yes, I do. But I\'m hungry human, where\'s my food?')
        input("press enter")
        
        if ("cat food" in player["items"]):
            userHasCatFood()
            goodEnding()
        else:
            userHasNoCatFood()
            findWallet()
    
    elif (pcmd == 'feed'):
        if ("cat food" in player["items"]):
            userHasCatFood()
            input("press enter")
            goodEnding()
        else:
            userHasNoCatFood()
            findWallet()
    
    #If user types in other
    else:
        print ("I don't understand that")
        goToCat()

def printGraphic(name):
    if (name =="CAT"):
        print('                                   #%*..    %@    ')
        print('                                 . ,/&&$#/,,#*    ')
        print('                                  /%&@ /&&&  /(   ')
        print('                                 ,/#($$&%##//**,  ')
        print('                             .****.... .....,*,,  ')
        print('                        ,,,,,,,,..      . ,,**    ')
        print('                         ,,..... ..,,.... *...,*  ') 
        print('                     ,,........  ..,,,,,...,,*    ')
        print('                 .,............,,,**/,(,,*/       ')
        print('                 *,,.............,///(#////       ')
        print(' /%&        #&#/*,,,,.,...,....,/((##%#&%(        ')
        print('  %&       $&$$$%#/*,,,*,,,,.,,,*,,*/#%&&&&&&     ')
        print('  ,#&&$$&&#$$&&&%(/**/*#%&&@&&*(/(%@&&%*&@@@&&..  ')

    if (name == "yourRoom"):
        print('------------------------------')
        print('|                    ------  |')
        print('|                   |      | |')
        print('|   🐈‍         0     ------  |')
        print('|-------     / | \           |')
        print('|   0  |       |      ____   |')
        print('|-------      / \     |  |   |')
        print('|   0  |     /   \    |  |   |')
        print('------------------------------')
    
    if (name == "drawer"):
        print('|------- ')
        print('|   0  | ')
        print('|------- ')
        print('|   0  | ')
        print('---------')

    if (name == "wallet"):
        print(' ------- ')
        print('| \ o / |')
        print(' ------- ')
    
    if (name == "happymom"):
        print('             .#&&&&&&&%*                       ')                     
        print('            ,#&&&&%(//($$%/                    ') 
        print('           /%#(*,,.....,*/(/                   ')  
        print('           *#**,,...  ..,,(/                   ')     
        print('          **** (#/...//....(                   ') 
        print('          ,/,**,,,,,.,,,,,,*.                  ') 
        print('           */,,..,*..,.,.,,,.                  ') 
        print('             ,**,,,..,.,*,,                    ') 
        print('              *,,%@/*&(,,,                     ') 
        print('              *(/*,**,*.,***,.                 ') 
        print('         ,,,,,*////*,.,*,,,....,...,,.         ') 
        print('    .,.....,., *****/****,,..,..,,.....,,      ') 
        print('  *,.......*,. ,,,*/,**,,....,.,*,,,....,,     ') 
        print('  ,*,.....,,. ,,***,.*(,.*,*.,,, ,*,,,,..,,    ') 
        print(' **,,,,,,,,.*,,.,..*.,(#..,/,.,,,,**,,,.,,,    ') 
        print(' **,,,,,.,,/,,,.....*..*,,,....**(#/,,,,,,,    ') 
        print(' /*,,,,..*.,,.......*..,*,,,...,  ./,,,,,,,    ') 
        print(' /*,,,,,./,,. ..,..*.  .,*,,,...,.. *,,,,,,,   ') 
        print(' ./*,,,*/.**,,...*         ..,,*,,,,,,/*,,,,,  ') 
        print(' ,/*,,,//***,,*,.           ...****,,,,,**,,,. ')      
        print(' **,*/**,,***,...*            ...*****,,,,,*,. ')                                                                                           

    if (name == "angrymom"):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,,,......,,,...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.,*,... ..*,. .,  .@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..,,,,(%&&@@&&%*......@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. ..../&&@&@&&&&%/... .@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    ..%&&@@&&&&&&%.....@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@((@@@.    ../,,*###%,,/##*.,.*/@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@#((@@( .   ((%#&&&&&&& ###%*. .#@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@#(#%@@, ..*(&&&&&(#&###&&&##(,..#@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@ @@@@@@&# *(###&&&&#% & &&%##(*,,*@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@#&@@&&&@@@@&&##&&&&#@@@&(#&&##/.@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@#%&&&@@@@@/#@*##&&&&&&&&&&&&##&/@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@##%&&@@@&%@@@.@.(#&&(#&&&&%##(#.@@@&@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@#((//#*@&(@@&.,(((/#&&&%&&&#(/( &,@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@#&#(///,**,,,,/##((//*(###(*/(((##*...(@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@(#&&&&$#*,*,,,,,,&&##(((/////(((###&&$,.  ..,@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@(#$$&&&$*,*,,,,,,,*$$$##(#########$$&$&/,      .,&@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@##$$$&&&$#,,,,,,,,,,,&&$$$$$$$$$$$$$$&&&&&,,,...,.,,,,,(@@@@@@@@@@@@')
        print('@@@@@@@@@@@$$#$$$$$$#(,,,,,,,,,,,,&&&&$$&&&&&&&&&&&&&*,,,,,,.,,,,,,,,@@@@@@@@@@@')
        print('@@@@@@@@@@@##$$$$$$$#&&,,,,,,,,,,,,&&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,,,,,@@@@@@@@@@')
        print('@@@@@@@@@@##$$$$$$$#(&$$,,,,,,,,,,,,&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,,,,,*@@@@@@@@@')
        print('@@@@@@@@@###$$$$$$$##$$(.,,,,,,,,,,,,&&&&&&&&&&&&&&&,,,,,,,,,,,,,,.,,,,@@@@@@@@@')
        print('@@@@@@@@ /###$$$$$$##$#..,,,,,,,,,,,,,&&&$&&&&&&&&&,,,,,,,,,,,,,,,.,,.,(@@@@@@@@')
        print('@@@@@@@@ /###$$$$$##$#/..,,,,,,,,,,,,,,,$$&&&&&@&,,,,,,,,,,,,,....,.../@@@@@@@@@')
        print('@@@@@@@&(((########(#(...,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,, .,,(((//@@@@@@@@@')

# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens