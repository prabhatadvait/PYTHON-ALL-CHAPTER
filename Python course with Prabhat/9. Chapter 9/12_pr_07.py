content = True
i = 1 
with open ("log.txt") as f:
    while content:
        content = f.readline()
        if "python" in content:
            # print(content)
            print(f"Python is present in line log file {i}")
        i+=1
    