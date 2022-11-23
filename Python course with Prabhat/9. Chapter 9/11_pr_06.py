
found = False
with open("log.txt") as f:
    content = f.readlines()
    
for line in content:
    if 'python' in line.strip().split(' '):
        print("Python is present")
        found = True
        break

if(found == False):    
    print("Python is not present in this log file")