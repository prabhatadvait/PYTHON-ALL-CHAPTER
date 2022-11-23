import random

# STONE , PAPER AND KAICHI
def gamewin(computer,you):
    if you == computer: #IF COMPUTER AND YOU BOTH CHOOSES YOU 
        return None
# CHECK ALL POSSIBLE VALUE WHEN COMPUTER CHOSE 'S'
    elif computer=='s':
        if you=='p':
            return True
        elif you=='k':
            return False
# CHECK ALL POSSIBLE VALUE WHEN COMPUTER CHOSE 'P'
    elif computer=='p':
        if you=='k':
            return True
        elif you=='s':
            return False
# CHECK ALL POSSIBLE VALUE WHEN COMPUTER CHOSE 'K'
    elif computer=='k':
        if you=='s':
            return True
        elif you=='p':
            return False
print("computer turn: stone(s) or paper(p) or kaichi(k)?")
randNo = random.randint(1,3)
if randNo==1:
    computer='s'
elif randNo==2:
    computer='p'
elif randNo==3:
    computer='k'
you = input("Your Turn: Stone(s) or paper(p) or kaichi(k)?")
a = gamewin(computer,you)
print(f"Computer chose {computer}")
print(f"YOU chose {you}")
if a == None:
    print("game is a tie")
elif a:
    print("You win the match")
else:
    print("Yor lose the match")
