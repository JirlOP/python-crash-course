# Exercise 5-11: Ordinal Numbers

# 1 to 9
ordinal_numbers = list(range(1, 10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    elif ordinal_number > 3:
        print(f"{ordinal_number}th")
