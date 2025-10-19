# tracker.py
# Name: Anvesha Saxena
# Date: 19 October 2025
# Project Title: Daily Calorie Tracker CLI

import datetime

print("\nWelcome to the Daily Calorie Tracker CLI!")
print("Track your meals, calories, and compare your daily intake with your set limit.\n")

# Task 2: Input & Data Collection
meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals would you like to enter? "))

for i in range(num_meals):
    name = input(f"Enter name of meal #{i+1}: ")
    calories = float(input(f"Enter calories consumed in {name}: "))
    meal_names.append(name)
    calorie_amounts.append(calories)

# Task 3: Calorie Calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts) if calorie_amounts else 0
daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
print()
if total_calories > daily_limit:
    print(f"Warning: You have exceeded your daily limit by {total_calories - daily_limit:.2f} calories!")
else:
    print(f"Good job! You are within your daily calorie limit with {daily_limit - total_calories:.2f} calories remaining.")

# Task 5: Neatly Formatted Output
print("\nMeal Name\tCalories")
print("-----------------------------")
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal:.0f}")
print("-----------------------------")
print(f"Total\t\t{total_calories:.0f}")
print(f"Average:\t{average_calories:.2f}")

# Task 6: Bonus - Save Session Log to File
save_option = input("\nWould you like to save this session to a file? (yes/no): ").strip().lower()
if save_option == "yes":
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename = f"calorie_session_{timestamp.replace(':','-').replace(' ','_')}.txt"
    with open(filename, "w") as file:
        file.write(f"Daily Calorie Tracker Session Log\n")
        file.write(f"Timestamp: {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("-----------------------------\n")
        for meal, cal in zip(meal_names, calorie_amounts):
            file.write(f"{meal}\t\t{cal:.0f}\n")
        file.write("-----------------------------\n")
        file.write(f"Total\t\t{total_calories:.0f}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        if total_calories > daily_limit:
            file.write(f"\nWarning: Exceeded limit by {total_calories - daily_limit:.2f} calories!\n")
        else:
            file.write(f"\nWithin daily limit. Remaining: {daily_limit - total_calories:.2f} calories\n")
    print(f"Session successfully saved to {filename}")

print("\nThank you for using the Daily Calorie Tracker CLI!")
