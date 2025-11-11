habits = []

def add_habit(name):
    habits.append({"name": name, "days": 0})

def complete_habit(name):
    for habit in habits:
        if habit["name"] == name:
            habit["days"] += 1

def show_habits():
    for habit in habits:
        print(f"{habit['name']} — {habit['days']} days")

def menu():
    while True:
        print("\n1. Add Habit\n2. Complete Habit\n3. Show Progress\n4. Quit")
        try:
            input_num = int(input("Enter a number: "))
            if input_num == 1:
                new_habit = input("Enter your new habit: ").capitalize()
                for habit in habits:
                    if habit["name"].lower() == new_habit.lower():
                        print("This habit already exists")
                        break
                else:
                    add_habit(new_habit)
                    print(f"Added new habit: {new_habit}")
            elif input_num == 2:
             completed_habit = input("Enter the complated habits name:")
             complete_habit(completed_habit)
            elif input_num == 3:
             show_habits()
            elif input_num == 4:
             print("Bye")
             break
            else:
             print("Choose a number 1-4")
        except ValueError:
            print("Please enter a valid number.")

             
menu()

