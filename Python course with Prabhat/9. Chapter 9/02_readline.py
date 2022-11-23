f = open("sample.txt" ,)
data = f.readline()# read first line 
print(data)
data = f.readline() # read second line
print(data)
data = f.readline() # read third line
print(data)
data = f.readline() # read fourth line and so.. on..
print(data)
f.close()