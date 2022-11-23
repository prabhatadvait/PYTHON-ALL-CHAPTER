file1 = "copy.txt"
file2 = "this.txt"
with open("copy.txt") as f:
    f1 = f.read()
with open("this.txt") as f:
    f2 = f.read()
if f1==f2:
    print("files are identical")
else:
    print("files are not identical")