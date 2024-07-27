# Exercise 5-8: Hello Admin

admins = ["admin", "joe", "jane", "john", "jim"]

# greet each admin, admin user have a special greeting
for admin in admins:
    if admin == "admin":
        print(f"Hello {admin}, would you like to see a status report?")
    else:
        print(f"Hello {admin}, thank you for logging in again.")

