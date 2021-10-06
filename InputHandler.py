from pathlib import Path


def receiveInput(lowerRange, upperRange):
    while True:
        userInput = input(">")
        try:
            userInput = int(userInput)
        except ValueError:
            print("Invalid input")
            continue
        if lowerRange <= userInput <= upperRange:
            break
        else:
            print("Number outside range.")
            continue
    return userInput


def createFolder(folderName):
    path = Path(folderName)
    try:
        path.mkdir()
    except FileExistsError:
        print(f"\n{folderName} folder already exist.")
        print("Existing folder will be used.")
