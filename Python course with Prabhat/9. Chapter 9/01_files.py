# Use open function to read the content of file
# f = open("sample.txt" ,'r')
f = open("sample.txt" ,)# by default mode is 'r'
# data = f.read()
data = f.read(10)# Read first ten character from the file
print(data)
f.close()