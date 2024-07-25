# 3.10. Every Function

# create a list of friends

## my_friends = ["Johana", "Alexandra(Nini)", "Miguel", "Steven"]
my_friends = []

# Append
my_friends.append("Johana")
my_friends.append("Alexandra(Nini)")
my_friends.append("Miguel")
my_friends.append("Steven")

print(my_friends)

# del - Steven left the list
del my_friends[3]

print(my_friends)

# Insert - Steven is back in first pos
my_friends.insert(0, "Steven")

# Pop - Miguel left the list and say goodbye
print(f"{my_friends.pop()}: Goodbye!")

# Sorted
print("The list is temporarily sorted")
print(sorted(my_friends))
print("The list is temporarily sorted in reverse")
print(sorted(my_friends, reverse=True))

# Sort
my_friends.sort()
print("The list is permanently sorted")
print(my_friends)

# Sort in reverse
my_friends.sort(reverse=True)
print("The list is permanently sorted in reverse")
print(my_friends)

# Reverse - The list is normally sorted
my_friends.reverse()
print("The list is normally sorted by the reverse method")
print(my_friends)

# Length - friend stays in the list
print(f"Total friends: {len(my_friends)}")
