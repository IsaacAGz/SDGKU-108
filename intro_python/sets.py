fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits = {"apple", "banana", "apple"}
print(fruits)

emails = ["a@.com", "b@.com", "a@.com", "a@.com", "c@.com", "a@.com"]
unique_emails = set(emails)
print(unique_emails)
print(list(unique_emails))
print(unique_emails)

fruits.add("orange")
print(fruits)

fruits.update(["kiwi", "mango"])
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("water")
print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

group_a = {"Leo", "Sam", "Alex", "Nina"}
group_b = {"Nina", "Jordan", "Sam", "Taylor"}

print(group_a.intersection(group_b))
print(group_a.difference(group_b))

signed_in = ["Leo", "Nina", "Leo", "Maya", "Sam"]

unique_students = set(signed_in)

not_signed_in = (group_a.difference(unique_students))
print("These students did not sign in: " + str(not_signed_in))

not_in_group = group_a.union(group_b)
not_in_group = unique_students.difference(not_in_group)

if len(not_in_group) == 0:
    print("Everyone velongs to a group!")
else: 
    print("Unregistered Students: " + str(not_in_group))



