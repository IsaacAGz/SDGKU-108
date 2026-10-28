my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

temp_tuple = ("apple", "banana", "cherry")
temp_list = list(temp_tuple)
temp_list[0] = "kiwi"

print(temp_list)


single = ("water",)
print(type(single))
not_tuple = ("apple")
print(type(not_tuple))

more = ("date", "elderberry")
print(my_tuple + more)
print(more * 2)
print(my_tuple[1:])
for item in my_tuple:
    print(item)

letters = ("a", "b", "c", "a")
print(letters.count("a"))
print(letters.count("c"))

coordinates = (10,20)
x, y = coordinates
print(x)
print(y)


# Mini Challenge
travel_bag = ("first aid", "food", "water", "fire starter", "camping gear")

print(travel_bag[2])
print(travel_bag[3])

if "boots" in travel_bag:
    print("you are ready to walk")
else: 
    print("You forgot your boots!")

essentials = ("hyegen kit", "extra clothes", "canmera")

final_bag = travel_bag + essentials 

print(len(final_bag))
print(final_bag[-1])


