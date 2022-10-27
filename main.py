# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

weapon = False

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def introScene():
    directions = ["left","right","forward"]
    print("You are at crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "forward":
            hauntedRoom()
        elif userInput == "backward":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")

def showShadowFigure():
    directions = ["left","right"]
    print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            cameraScene()
        elif userInput == "left":
            print("You find that this door opens into a wall.")
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")

def cameraScene():
    directions = ["forward","backward"]
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            print("You Made it! you've found an exit.")
            # quit()
        elif userInput == 'backward':
            showShadowFigure()
        else:
            print("Please enter a valid option.")

def hauntedRoom():
    directions = ["left","right","backward"]
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("Multiple goul-like creatures start emerging as you enter the room. You are killed. please retry again.")
            # quit()
        elif userInput == "left":
            print("You made it! You've found an exit.")
            # quit()
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")

def showSkeletons():
    directions = ["backward","forward"]
    global weapon
    print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You find that this door opens into a wall. you open some of the drywall to discover knife")
            weapon = True
        elif userInput == "backward":
            introScene()
        elif userInput == 'forward':
            strangeCreature()
        else:
            print("Please enter a valid option.")

def strangeCreature():
    actions = ["fight","flee"]
    global weapon
    print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print(
                    "You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
            else:
                print("The goul-like creature has killed you. please retry again.")
                # quit()
        elif userInput == "flee":
            showSkeletons()
        else:
            print("Please enter a valid option.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("Welcome to the Adventure Game!")
        print("As an adventure traveler, you have decided to visit the Catacombs of India.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " + name + ".")
        introScene()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
