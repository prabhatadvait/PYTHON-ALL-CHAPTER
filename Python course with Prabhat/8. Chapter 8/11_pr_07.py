def remove_and_strip(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()
this = "  Prabhat is a good boy  "
f = remove_and_strip(this,"Prabhat")
print(f)

