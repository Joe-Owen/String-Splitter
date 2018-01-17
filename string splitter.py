########################
#   Joe Owen           #
#   String Splitter    #
#   17/1/18            #
########################


def UserInputFunction():
    global UserInput
    UserInput = input(": ")
    Split()

def Split():
    global UserInput
    global InputArray
    InputArray = []
    TempInputStorage = "NULL"
    for i in UserInput:
        if i != " " and i != "." and i != "," and i != "?" and i != "!":
            if TempInputStorage == "NULL":
                TempInputStorage = i
            elif TempInputStorage != "NULL":
                TempInputStorage = TempInputStorage + i
        if (i == " " or i == "." or i =="," or i == "?" or i == "!") and TempInputStorage != "NULL":
            InputArray.append(TempInputStorage)
            TempInputStorage = "NULL"
    if TempInputStorage != "NULL":
        InputArray.append(TempInputStorage)
        TempInputStorage = "NULL"
    print(InputArray)
    print(TempInputStorage)

UserInputFunction()
