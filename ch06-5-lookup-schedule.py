# 6.5
def lookup(your_schedule):
    """This function returns a phone number when given a certain name."""
    name = input("Please type a name: ")
    surname = input("Please type a surname: ")
    key = (name, surname)
    if key in your_schedule:
        print(your_schedule[key])
    else:
        print("Name not found.")
        

schedule = {('Anna','Karenina'):'(123)456-78-90',
              ('Yu', 'Tsun'):'(901)234-56-78',
              ('Hans', 'Castorp'):'(321)908-76-54'}
lookup(schedule)
