def food():                      #Made a function for the food shopping
    print ("---------------------------------------------------------------------\
        \n(:point_right:I remember wife has mentioned to get 2 dozen apples...)") #Wife has mentioned apples in the list
    while True:     #This is while loop defined to check if user gives a unwanted answer
        answer = input("Which section would have apples in it? - fruits:apple:/ meat:poultry_leg:/ veggies:green_salad:?  ")
        print (answer)
        if answer.lower() != ("fruits"):           #.lower() converts all the string letters into lower case
             print ("You did not find apples :apple: in this section,\nGo to other section >>")
             continue
        else:
             print ("\n______________________________________________________________\
                \nYayy!! Finally got something which makes my wife happy:tada:.\nI have bought 2 dozen apples:apple: for the apple pie.\
                \n______________________________________________________________\n")
             break
    input("(press enter to continue)")

food()