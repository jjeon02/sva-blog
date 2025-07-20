import time

player = { 
    "name": "p1", 
    "items" : ["no Food"],
    "friends" : [],
    "location" : "start"
}

def introStory():
    print ("Welcome to another normal day of your life. What's your name?")
    player["name"] = input("Please enter your name >")

    print ("You received a text msg from your friend")
    time.sleep(1.5)
    print (">> 'Hey, " +  player["name"] +" !"+" We're still having dinner at 6, right?")
    time.sleep(2)
    print('>> Sorry, I think I might be a bit late. I\'m looking for my wallet.')
    time.sleep(2)       
    print('>> No worries, but make sure to come asap!')
    time.sleep(2)
    print (" It's your friend's birthday today and you are going to her birthday party.\
            \n But you can't find your wallet! You need to snoop around fast to not be late.")
    time.sleep(2)
    chooseParty()

def chooseParty():
    pcmd = input("please choose 'let's go' or 'go back to sleep' >")

    if (pcmd == "let's go"):
        print ("'Meow!' Your cat Oscar wants to play with you.")
        input("[press enter]")
        findWallet()
    elif (pcmd == "go back to sleep"):
        time.sleep(2)
        print ("You missed the party and your friend cancelled you.\
            \n TAT TAT TAT TAT TAT TAT TAT")
        pcmd = input("[press enter]")
        introStory() 
    else:
        print ("I don't understand that")
        chooseParty() 
        
# two ending results

def badEnding():
    # printGraphic("wallet")
    print("-------------------------------")
    print("You were not able to find your wallet and missed the party. Your friend is very sad.")
    time.sleep(2)
    print("Friend: I'm disappointed at you, " + player["name"] ) # customized with a name
    input("[Press enter to redo the game]")
    introStory()

def goodEnding():
    printGraphic("wallet")
    print("-------------------------------")
    print("You were able to find your wallet and joined the party. Your friend is very happy!")
    input("[Press enter to redo the game]")
    introStory()

# FINDING WALLET JOURNEY STARTS     
def findWallet():
    printGraphic("yourRoom")
    print("You can either check your drawer, interact with your cat or talk to mom.")
    print ("Your options: [ drawer, cat, mom ]")
    pcmd = input(">") 

    #drawer path
    if (pcmd.lower() == "drawer"):
        printGraphic("drawer")
        goToDrawer()

    #cat path
    elif(pcmd.lower() == "cat"):
        printGraphic("CAT")
        goToCat()

    #mom path
    elif(pcmd.lower() == "mom"):
        goToMom()

    else:
        print("I don't understand that")
        findWallet()

# GO TO DRAWER
def goToDrawer():                      
    print ("Your can either open the drawer or check on top") #Wife has mentioned apples in the list
    while True: #This is while loop defined to check if user gives a unwanted answer
        pcmd = input("Your options: [ top, open ]")
        print (pcmd)
        if pcmd.lower() == ("top"): 
            print("There's nothing")
            continue
        elif pcmd.lower() == ("open"): 
            print("You found the cat food")
            time.sleep(1)
            print("You now have food for your cat, Oscar")
            player["items"].append("cat food")
            goToCat()
            break
        else: #user chooses open
            print("I don't understand")
            continue
    input("(press enter to continue)")

##MOM PATH
def goToMom():
    print('You can ask mom for help, ignore your mom or help her with chores.')
    print ("Your options: [ ask, ignore, help ]")
    pcmd = input(">") 

    if (pcmd.lower() == 'ask'):
        print('"Mom, have you seen my wallet?"')
        print('Your mom is angry at you for being careless. She yelled at you.')
        time.sleep(2)
        printGraphic("angrymom")
        input("[press enter]")
        badEnding()

    elif (pcmd.lower() == 'ignore'):
        print('You walked away.\
              \n Your mom is angry at you for being careless. She yelled at you.')
        time.sleep(2)
        printGraphic("angrymom")
        input("[press enter]")
        badEnding()

    elif (pcmd.lower() == 'help'):
        print('Your mom is very happy.')
        time.sleep(1)
        printGraphic("happymom")
        print('"That\'s wonderful! Can you feed the cat? Here\'s some cat food. Take as many as you want."')
        player["items"].append("cat food")
        input("[press enter]")
        print("You now have food for your cat, Oscar")
        goToCat()
    
    #If user types in other
    else:
        print ("I don't understand that")
        goToMom()

##CAT PATH
def goToCat():
    time.sleep(1)
    print ("You can either talk to Oscar or feed him")
    print ("Your options: [talk, feed]")
    pcmd = input(">") #user choose

    def userHasCatFood():
        print('You give Oscar his food.')
        time.sleep(1)
        print('Oscar: Nice food, human. Here\'s your wallet meow.')
        input("[press enter]")
    
    def userHasNoCatFood():
        print('You don\'t have any food.')
        time.sleep(1)
        print('Oscar: No food? You\'re useless, human!')
        input("[press enter]")

    if (pcmd.lower() == 'talk'):
        print('Do you have my wallet?')
        time.sleep(1)
        print('Oscar: Yes, I do. But I\'m hungry human, where\'s my food?')
        input("[press enter]")
        
        if ("cat food" in player["items"]):
            userHasCatFood()
            goodEnding()
        else:
            userHasNoCatFood()
            findWallet()
    
    elif (pcmd.lower() == 'feed'):
        if ("cat food" in player["items"]):
            userHasCatFood()
            input("[press enter]")
            goodEnding()
        else:
            userHasNoCatFood()
            findWallet()
    
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
        print('@@@@@@@@@@@@@@@@@@@@@@@@((@@@.    ../,/*###%#&//#*.,.*/@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@#((@@( .   ((%# &&&&&& ,,#%*. .#@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@#(#%@@, ..*(&&&&&(#&###&&&##(,..#@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@ @@@@@@&# *(###&&&&#%/&/&&%##(*,,*@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@#&@@&&&@@@@&&##&&&&#@ ,&(#&&##/.@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@#%&&&@@@@@/#@*##&&&&&/&,&&&&##&/@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@##%&&@@@&%@@@.@.(#&&,#,./,%##(#.@@@&@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@#((//#*@&(@@&.,(((/#&&&,&,&#(/( &,@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
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

def main():
    printGraphic("title") 
    introStory() 

main()