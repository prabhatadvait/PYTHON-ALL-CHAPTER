with open('another.txt','r') as f:
    a = f.read()
with open('another.txt','w') as f:
    a = f.write("Advaita,he is not so good")
print(a)
