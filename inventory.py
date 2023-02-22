# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    # This function will help my content to be readable
    def __str__(self):
        return f'{self.country}, {self.code}, {self.product}, £{self.cost}, {self.quantity}'


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    try:
        shoe_file = open("inventory.txt", "r", encoding="utf-8")
        line = shoe_file.readlines()
        for i, shoe in enumerate(line, start=0):
            # The line 37 will always skip the first line from the file, you will see this line several times
            # in the code
            if i != 0:
                split_line = shoe.strip().split(",")
                shoe_list.append(Shoe(split_line[0], split_line[1], split_line[2], split_line[3],
                                      int(split_line[4])))
        shoe_file.close()
    except FileNotFoundError:
        print("The file doesn't exist")


def capture_shoes():
    try:
        # This function will allow the user to enter information about shoes and then add them to the list and file
        country = input('Enter the country name: ')
        code = input('Enter the code number: ')
        product = input("Enter the shoe's/product's name: ")
        cost = int(input("Enter the cost of the shoe/product: "))
        quantity = int(input("Enter the total quantity of the product: "))
        shoe_list.append(Shoe(country, code, product, cost, quantity))

        file = open("inventory.txt", "a", encoding="utf-8")
        file.write(f'\n{country},{code},{product},{cost},{quantity}')
        file.close()
    except ValueError:
        print()
        print('Enter a number for the cost and quantity of the product')
        print()
        capture_shoes()


def view_all():
    # I have used the rad_shoes_data() because without I wouldn't be able to iterate through the shoe_list
    read_shoes_data()
    for i, shoe in enumerate(shoe_list):
        print(f'{i + 1}: {shoe}')
    # after the list is output I want the list to be deleted, otherwise when I called the view_all function
    # I will add the list to the previous list, which means the output will be repeated twice or the times
    # the function is called
    shoe_list.clear()


def re_stock():
    # I am using a list, because I will convert its content into an int, so that I could get the lowest number
    lowest = []
    try:
        shoe_file = open("inventory.txt", "r", encoding="utf-8")
        line = shoe_file.readlines()
        for i, shoe in enumerate(line, start=0):
            if i != 0:
                split_line = shoe.strip().split(",")
                # lowest list will store integers because I need to find the lowest value in terms of numbers
                # and not alphabetic order
                lowest.append(int(split_line[4]))
        smallest = min(lowest)
        # I have now converted the smallest variable into a string because I'll need to check
        # if it is exactly the same with data string I am comparing to. Which will happen in line 80
        smallest = str(smallest)
        for index, lowest_quantity_shoe in enumerate(line, start=0):
            if index != 0:
                split_line = lowest_quantity_shoe.strip().split(",")
                if smallest == split_line[4]:
                    print(line[index])
                    answer = input("The above product has the lowest quantity, would you like to updated? "
                                   "(Yes/No): ").lower()
                    if answer == "yes":
                        try:
                            new_digit = int(input("Enter the new quantity you'd like for this product: "))
                            line[index] = f"{split_line[0]},{split_line[1]},{split_line[2]}," \
                                          f"{split_line[3]},{new_digit}\n"
                            print("Quantity updated")
                            print(line[index])
                            upd_line = open("inventory.txt", "w", encoding="utf-8")
                            upd_line.writelines(line)
                            upd_line.close()
                        except ValueError:
                            print("Only numbers")
                            re_stock()
                    elif answer == "no":
                        print("Nothing has been updated")
                    else:
                        print("Wrong choice")
        shoe_file.close()
    except FileNotFoundError:
        print("The file doesn't exist")


def search_shoe():
    shoe_code = input("Enter the shoe code that you're looking for please: ")
    try:
        shoe_file = open("inventory.txt", "r", encoding="utf-8")
        lines = shoe_file.readlines()
        for line in lines:
            split = line.strip().split(",")
            if shoe_code == split[1]:
                print(line)
        else:
            print("shoe code not valid")
        shoe_file.close()

    except FileNotFoundError:
        print("The file doesn't exist")


def value_per_item():
    try:
        shoe_file = open("inventory.txt", "r", encoding="utf-8")
        lines = shoe_file.readlines()
        for index, line in enumerate(lines):
            if index != 0:
                split = line.strip().split(",")
                cst = int(split[3])
                qny = int(split[4])
                value = qny * cst
                print(f'The value of the {qny} {split[2]} is £{value}')
        shoe_file.close()
    except FileNotFoundError:
        print("The file doesn't exist")


def highest_qty():
    highest = []
    try:
        shoe_file = open("inventory.txt", "r", encoding="utf-8")
        line = shoe_file.readlines()
        for i, shoe in enumerate(line, start=0):
            if i != 0:
                split_line = shoe.strip().split(",")
                # highest list below will store integers because I need to find the lowest value in terms
                # of numbers and not alphabetic order
                highest.append(int(split_line[4]))
        high = max(highest)
        # This for loop below will allow me to check if the high variable is equal to any value in split[4]
        # check line 163
        for highest_qny in line:
            split = highest_qny.strip().split(",")
            if str(high) in split[4]:
                print(f'The {split[2]} is on sale')
        shoe_file.close()
    except FileNotFoundError:
        print("The file doesn't exist")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    print()
    menu = input('''Select one of the following Options below:
                 a - Adding new shoe
                 va - view all shoes
                 r - re-stock the lowest quantity of shoes
                 tv - view total value of each shoe
                 s- vew shoe on sale
                 e - Exit
                 : ''').lower()

    if menu == 'a':
        capture_shoes()
    elif menu == 'va':
        print(view_all())
    elif menu == 'r':
        re_stock()
    elif menu == 'tv':
        value_per_item()
    elif menu == 's':
        highest_qty()
    elif menu == 'e':
        exit()
    else:
        print('Wrong choice')
