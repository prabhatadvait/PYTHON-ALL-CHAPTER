myDict = {
      "prabhat": "mr Perfect",
      "gudan": "monu lover",
    "marks": [1,2,3,4,5,6,7,8,9,0] ,
    "anotherDict" : {'Lovely':'Lohra lover' },
    1:2
}
# Method of dictionary
print(list(myDict.keys()))# printing the keys of dictionary
print(list(myDict.values())) # printing the values of dictionary
print(myDict.items()) # printing the (key,value) of all content of dictionary
gama = {
   "Prabhat": "Hero",
   "Sima": "prabhat's mother",
   "Chitranjan": "prabhat's father"
}
myDict.update(gama) # To add new key-value pairs use myDict.update()
print(myDict.get("gudan"))# print key value associated with key "gudan"
print(myDict["gudan2"])# print key value associated with key "gudan"
# The difference between .key and [] syntax 
print(myDict.get("gudan2"))# Returns None as gudan2 is not present in the dictionary
print(myDict["gudan2"])# Throws a error as gudan2 is not present in the dictionaryt