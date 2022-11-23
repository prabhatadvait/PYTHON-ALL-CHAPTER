myDict = {
    "pankha":"fan",
    "dabba":"box",
    "pani":"water",
    "adami":"Man"
}
print("Options are:",myDict.keys())
a = input("Enter Hindi word\n")
# print("The meaning of Hindi word:",myDict[a])
# Below line will not throw error if key is not present in the dictionary
print("The meaning of Hindi word:",myDict.get(a))

