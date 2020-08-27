import time
import random

class GameChar(object):
    
    def __init__(self, name, lvl, hp, mp, curr_exp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp
        self.curr_exp = curr_exp

    def levelup(self, exp):
        print(self.name + " has gained " + str(exp) + "+ exp!")
        if (curr_exp > self.lvl**2):
            print(self.name + "has leveled up!")
            self.curr_exp = curr_exp-self.lvl**2
            hp, mp = self.statChange()
            print("+50HP and +100MP!")

    def statChange():
        self.hp+=50
        self.mp+=100
        return hp, mp
    def displayStats(self, x):
        print("Character " + str(x+1) + ": - Name: " + self.name + " | Level: " + str(self.lvl) + " | HP: " + str(self.hp) + " | MP: " + str(self.mp))

def makeBanner(banner):
    print("")
    print("====================")
    print(banner)
    print("====================")

characters = []
charCreate, gameRun = True, True
count = 0
makeBanner("Character Creation")
while(gameRun):
    while(charCreate):
        if len(characters) > 0:
            ans = input("Do you want to create another character?: (yes/no): ")
            if ans.lower() in ["no"]:
                charCreate = False
                continue
        char = input("Type your name: ")
        if len(characters) < 1:
            print("Character was added!")
            characters.append(GameChar(char, 1, 100, 200, 0))
            continue
        else:
            while count < len(characters):
                if characters[count].name == char:
                    print("This name is unavaliable")
                    count = 0
                    break
                count+=1
            if count > 0:
                print("Character was added!")
                characters.append(GameChar(char, 1, 100, 200, 0))    
        count = 0
    makeBanner("Your Characters")
    for x in range (len(characters)):
        characters[x].displayStats(x)
        continue
    makeBanner("Selecting Characters")
    count = 0
    selectedChar = -1
    while(True):
        ans = input("Enter your character's name: ")
        while count < len(characters):
            if characters[count].name == ans:
                selectedChar = count
            count+=1
        if selectedChar != -1:
            break
        print("Invalid.")
        count = 0
    print("")
    print("Character, \"" + characters[selectedChar].name  + "\" was selected!")
    while(True):
        makeBanner("YOUR CHARACTER: " + characters[selectedChar].name.upper())
        print("[0] = train")
        print("[1] = stats")
        print("[2] = help")
        print("[3] = exit")
        ans = input("Type a number: ")
        if ans in "0":
            pass
        elif ans in "1":
            makeBanner("Your Characters")
            characters[selectedChar].displayStats(selectedChar)
        elif ans in "2":
            makeBanner("Help")
            print("[0] will train your character. You will gain a random amount of exp 0-50 after answering a math question. Once you have enough exp, you can level up and gain more stats.")
            print("[1] will show your stats and how close you are to leveling up.")
            print("[2] will print this text again.")
            print("[3] will exit this screen.")
        elif ans in "3":
            print("Exiting character...")
            time.sleep(2)
            break
        else:
            pass
