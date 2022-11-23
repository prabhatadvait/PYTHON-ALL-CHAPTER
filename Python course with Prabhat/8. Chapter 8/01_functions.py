def percent(marks):
    p = (((marks[0] + marks[1] + marks[2] + marks[3])/400)*100)
    return p
marks1 = [67,76,78,96]
percentage1 = percent(marks1)
marks2 = [87,96,98,99]
percentage2 = percent(marks2)
print(percentage2,percentage1)