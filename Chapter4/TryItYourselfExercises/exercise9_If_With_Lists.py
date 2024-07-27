# Exercise 5-9: NO Users

admins = ["admin", "joe", "jane", "john", "jim"]
admins.clear()

# greet each admin, admin user have a special greeting and make sure if
# the list is not empty
if admins:
    for admin in admins:
        if admin == "admin":
            print(f"Hello {admin}, would you like to see a status report?")
        else:
            print(f"Hello {admin}, thank you for logging in again.")
else:
    print("We need to find some users!")

