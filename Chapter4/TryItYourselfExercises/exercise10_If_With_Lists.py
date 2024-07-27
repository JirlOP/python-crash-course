# Exercise 5-10: Checking Usernames

current_users = ["jorge", "ARchi", "fer", "sergio", "faby"]
# two new users are currents users
new_users = ["Jorge", "Archi", "ale", "joha", "vale"]

for new_user in new_users:
    available = True
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(f"Sorry {new_user}, that name is already taken. \nPlease enter a new username.")
            available = False
            break

    # if not available not print this.
    if available:
        print(f"{new_user} is available.")

