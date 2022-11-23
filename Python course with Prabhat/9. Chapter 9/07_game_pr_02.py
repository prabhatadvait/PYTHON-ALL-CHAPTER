def game():
    return 78

with open("hiscore.txt") as f:
    hiscorestr = (f.read())
score = game() 

if hiscorestr=='':
    with open("hiscore.txt","w") as f:
        f.write(str(score))
        
elif int(hiscorestr)<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))

