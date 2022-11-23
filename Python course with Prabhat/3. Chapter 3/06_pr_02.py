letter = '''Dear <|Name|>,
Greeting from Advait foundation,I am happy to tell you about your selection
your are selected!
Thanks and regards!
Prabhat
date: <|Date|>
Registration No:<Regn>
'''
name = input("Enter your name\n")
date = input("Enter Date\n")
Registration = input("Enter your Registration No\n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>", date)
letter = letter.replace("<Regn>", Registration)
print(letter)
