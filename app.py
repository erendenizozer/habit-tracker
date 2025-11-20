habits = []

def add_habit(name):
    habits.append({"name": name, "days": 0})

def complete_habit(name):
    for habit in habits:
        if habit["name"].lower() == name.lower():
            habit["days"] += 1

def show_habits():
    for habit in habits:
        print(f"{habit['name']} — {habit['days']} days")

def find_habit():
   if habit not in habits:
      print("That habit does not exist.")
      

def menu():
    while True:
        print("\n1. Add Habit\n2. Complete Habit\n3. Delete Habit\n4. Show Progress\n5. Quit")
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
             for habit in habits:
                if completed_habit.lower() == habit["name"].lower():
                    complete_habit(completed_habit)
                    print(f"Completed the habit {completed_habit}!")
                    break
             else:
                print(f"Couldn't find a habit named {completed_habit}")
            elif input_num == 3:
               unwanted_habit = input("Enter the habit you want to delete: ")
               for habit in habits:
                  if unwanted_habit.lower() == habit["name"].lower():
                     habits.remove(habit)
                     print(f"Deleted the habit {unwanted_habit}")
                     break
               else:
                print(f"Couldn't find a habit named {unwanted_habit}")
            elif input_num == 4:
             show_habits()
            elif input_num == 5:
             print("Bye")
             break
            else:
             print("Choose a number 1-4")
        except ValueError:
            print("Please enter a valid number.")

             
menu()

