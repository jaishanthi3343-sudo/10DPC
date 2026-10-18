colors=["red","green","blue","yellow"]
print (colors[0])
print(colors[2])



colors=["red","green","blue","yellow"]
colors[2]= "white"
print(colors)


colors=["red","green","blue"]
colors.append("orange")

print(colors)


animals=["cat","lion"]
animals.insert(1,"dog")
print(animals)

animals=["cat","dog","lion","tiger"]
animals.remove("lion")
print(animals)






colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

animals = ["cat", "dog", "lion"]

if "tiger" in animals:
    print("found")
else:
    print("not found")

colors=["yelloe","blue","red","green"]
colors.sort()
print(colors)

animals=["tiger","lion","dog","cat"]
animals.reverse()
print(animals)

numbers=[10,20,30,40,50]
numbers.reverse()
print(numbers)
