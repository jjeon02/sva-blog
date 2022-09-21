# Declaration
def openFridge():
    fridgeOpen = 1
    print("Now Open")
    return fridgeOpen

isTheFridgeOpen = openFridge()

def closeFridge():
    fridgeOpen = 0
    print("Now Closed")

# Definition
def say(what, whom):
    # print(what+ " " + whom)
    return what + " " + whom

# Callout the Function
openFridge()
# say("Hi","Bruno")
greeting = say("Hi", "Bruno")
print(greeting)

def isStudentPresent():
    # See if they are in the room
    return True

def checkAttendence():
    # loop through array of students
    # check is they are here
    # if they are return true
    isStudentPresent()
    
    if (22 == 22):
        return True
    else:
        return False

isEveryoneHere = checkAttendence() #True otherwise False
print(isEveryoneHere)