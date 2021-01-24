instructmenu = [
    "This is the Expenses Tracker.",
    "What would you like to do?\nEnter a purchase - 1\nRemove a purchase - 2\nCheck total expenses - 3\n",
    "Your total spent is $",
    "This is not a valid instruction. Try again!",
    "Yay, your purchase is added!",
    "Check purchase history - 4\nEnter: "
]

purchase_dict = {}


def expenseslogger():
    total = 0
    user_del_item = ""
    while True:
        try:
            print("")
            print(instructmenu[0])
            print("")
            user_instruct = int(input(instructmenu[1] + instructmenu[5]))
            if user_instruct == 1:
                print("")
                user_purchase = input("Enter purchase: ")
                user_price = float(input("Enter amount(in dollars): "))
                purchase_dict[user_purchase] = user_price
                total += int(user_price)
                if user_price >= 500:
                    print(instructmenu[4] + "(It's quite a hefty purchase)")
                else:
                    print(instructmenu[4] + "(It's quite a thrifty purchase)")
            elif user_instruct == 2:
                user_del_item = input("Enter the exact name of purchase: ")
                total -= int(purchase_dict[user_del_item])
                del purchase_dict[user_del_item]
                print("")
                print(user_del_item + " has been removed!")
            elif user_instruct == 3:
                print("")
                print(instructmenu[2] + str(total) + ".")
            elif user_instruct == 4:
                print("")
                print("Your purchase history:")
                for key, value in purchase_dict.items():
                    print(key + " - " + str(value))
            else:
                print(instructmenu[3])
        except KeyError:
            print("Purchase does not exist. Try again")
        except ValueError:
            print(instructmenu[3])


expenseslogger()

# Possible errors:
# user enters same user_purchase twice and it gets overridden (check if the key already exists, rename key by adding a
# number behind key, use variable to track the number of dups, inform user of renaming)
# user wants to cancel an ongoing action (enter another num)
#
# Possible ideas:
# purchase history can be sorted by price, time(with date of purchase) or alphabetical order
