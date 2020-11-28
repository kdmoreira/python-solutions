# 6.2
def lookup(your_schedule):
    """This function finds the name of a person in a given schedule after a number is given."""
    while True:
        number = input("Please type the phone number in the format (xxx)xxx-xx-xx: ")
        if number in schedule:
            print(schedule[number])
        else:
            print("Number not found.")

schedule = {'(123)456-78-90':['Anna','Karenina'],
                '(901)234-56-78':['Yu', 'Tsun'],
                '(321)908-76-54':['Hans', 'Castorp']}

lookup(schedule)
