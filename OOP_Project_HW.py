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
        print(self.name + " has gained +" + str(exp) + " exp!")
        self.curr_exp+=exp
        while (self.curr_exp >= self.lvl**2):
            global curve
            print(self.name + " has leveled up!")
            self.curr_exp-=self.lvl**2
            self.lvl+=1
            self.statChange()
            print("+50HP and +100MP!")
            curve+=1
    def statChange(self):
        self.hp+=50
        self.mp+=100
        
    def displayStats(self, x):
        print("Character " + str(x+1) + ": - Name: " + self.name + " | Level: " + str(self.lvl) + " | HP: " + str(self.hp) + " | MP: " + str(self.mp) + " | Current EXP: " + str(self.curr_exp) + " | EXP to lvl up: " + str(self.lvl**2-self.curr_exp))

def makeBanner(banner):
    print("")
    print("====================")
    print(banner)
    print("====================")

def getAnswer(randnum, randnum1, randsign):
    if randsign in "+":
        return float(randnum+randnum1), 1+curve
    elif randsign in "-":
        return float(randnum-randnum1), 2+curve
    elif randsign in "*":
        return float(randnum*randnum1), 3+curve
    else: # /
        return float(randnum/randnum1), 4+curve
characters = []
curve = 0
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
            makeBanner("TRAINING CHARACTER:")
            print("Training character...")
            time.sleep(1)
            randnum, randnum1 = random.randint(1,10), random.randint(1,10)
            signList = ("+","-","*","/")
            randsign = random.choice(signList)
            answer, ansExp = getAnswer(randnum, randnum1, randsign)
            x = input("What is " + str(randnum) + " " + randsign + " " + str(randnum1) + " = ?: ")
            print("Checking answer...")
            time.sleep(1)
            if float(x) == answer:
                print("Correct!")
                characters[selectedChar].levelup(ansExp)
            else:
                print("Incorrect. You do not gain exp!")
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
            print("[0] = switch characters")
            print("[1] = exit the game")
            y = input("Type a number: ")
            if y in "0":
                print("Exiting character...")
                time.sleep(2)
                break
            elif y in "1":
                print("Exiting game...")
                time.sleep(2)
                gameRun = False
                break
            else:
                print("Invalid input.")
        else:
            print("Invalid number")
print("Thank you for playing!")
print("Exited the game!")
time.sleep(5)
