def farh(cel):
    return (cel*(9/5)) + 32
# print(farh(37)) we can write like this
a = farh(int(input("Enter the temperature in celsius:- ")))
print("The farhenhit temperature is " + str(a))