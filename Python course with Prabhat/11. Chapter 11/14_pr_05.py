class vector:
    def __init__(self,vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1  
        return str1[:-1]
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
v1 = vector([1,4,6])
v2 = vector([1,3,5])
print(v1 + v2)
print(v1*v2)

