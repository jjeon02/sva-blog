# # Object 1 = Arrays
# myTools = ['Macbook', 'Ipad', 'Iphone']

# # Object 2 = Objects
# myMusic = {"App" : "Spotify Premium", "instrument" : "Bass Guitar"}

# # Object 3 = Numbers
# import datetime
# currentDateTime = datetime.datetime.now()
# date = currentDateTime.date()
# currentYear = date.strftime("%Y")
# myYearsLeftinSchool = float(2024 - int(currentYear))

# # Object 4 = Hours I sleep
# # let mySleep = 5;
# # let mySleepBoolean = Boolean(mySleep > 6)

# print('I am ' + str(myYearsLeftinSchool) + ' years away from graduating from Grad School.')

# Another Assignment 3 using python
print ("# Another Assignment 3 using python.")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
place = input("Enter a place you want to go: ")
color = input("Any color you find not impressing: ")
animal = input("Your favourite animal? ")
adjective = input("Enter an adjective: ")
number = input("Any number you have in mind ")
time = input("What time do you go to sleep? ")

story = "I went to " + place + "to do a little exercise. The " + color + "sky was " + adjective + " today. While running, the " + animal + " suddenly popped up and frightened me. What in the " + place + "? I thought to myself. The " + animal + " spoke: It's been " + number + " years since we last met, why haven't you called me since? Then I woke up at " + time
# finally we print the story
print(story)

