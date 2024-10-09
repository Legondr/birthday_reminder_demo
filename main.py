name_birthday = {}
user_input = 0
while user_input != 3:
    print("1 - to display data")
    print("2 - to save data")
    print("3 - to exit")

    try:
        user_input = int(input("Your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match user_input:
        case 1:  # display data
            with open("name_birthday_database.txt", "r") as file:
                for line in file:
                    print(line)
        case 2:  # save data
            print("Type in format Name,day.month.year ex.(Medard,8.10.2024)")
            user_input = input("Your friend's name and birthday: ")
            #saving the user_input into name_birthday dictionary
            try:
                name, birthday = user_input.split(",")
                name = name.strip()  # Remove any extra spaces from name
                birthday = birthday.strip()  # Remove any extra spaces from birthday

                # Add to the dictionary
                name_birthday[name] = birthday
                print(f"{name} has been added with the birthday {birthday}.")
            except ValueError:
                print("Invalid format. Please use Name,day.month.year (e.g., Medard,8.10.2024)")

            #save data into a file
            with open("name_birthday_database.txt", "a") as file:
                    for name, birthday in name_birthday.items():
                        file.write(f"{name}, {birthday}")
        case 3:  # exit
            print("Exiting...")
            break
        case _:  # default case for invalid input
            print("Invalid choice. Please choose 1, 2, or 3.")
