sub1= int(input("Enter the marks of sub1\n"))
sub2= int(input("Enter the marks of sub2\n"))
sub3= int(input("Enter the marks of sub3\n"))
if(sub1<33 or sub2<33 or sub3):
    print("sorry you are fail due to less marks in one subject")
elif(sub1+sub2+sub3)/3 < 40:
    print("sorry you are fail because overall percentage is less")
else:
    print("congratulations! you are passed in exam")