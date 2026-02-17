
#       5 Simple AI-Based Python Examples


# Example 1: Simple Chatbot 
# A basic chatbot that replies based on what you type.

print(" Example 1: Simple Chatbot ")

user_message = "hello"

if user_message == "hello":
    print("Bot: Hi there! 😊")
elif user_message == "how are you":
    print("Bot: I am fine, thank you!")
elif user_message == "bye":
    print("Bot: Goodbye! 👋")
else:
    print("Bot: Sorry, I don't understand.")

print()


# Example 2: Guess the Number 
# AI picks a random number and you try to guess it.

print(" Example 2: AI Random Number ")

import random

ai_number = random.randint(1, 10)  # AI picks a number between 1 and 10
my_guess = 5

print(f"AI picked: {ai_number}")
print(f"Your guess: {my_guess}")

if my_guess == ai_number:
    print("You guessed it! ✅")
elif my_guess > ai_number:
    print("Too high! ⬇️")
else:
    print("Too low! ⬆️")

print()


#  Example 3: AI Calculator
# AI checks what operation you want and gives the answer.

print(" Example 3: AI Calculator ")

num1 = 10
num2 = 5
operation = "add"

if operation == "add":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
elif operation == "divide":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Unknown operation")

print()


# Example 4: AI Grade Checker 
# AI checks your marks and tells your grade.

print(" Example 4: AI Grade Checker ")

marks = 75

print(f"Your marks: {marks}")

if marks >= 90:
    print("AI says: Grade A ⭐")
elif marks >= 70:
    print("AI says: Grade B 👍")
elif marks >= 50:
    print("AI says: Grade C 🙂")
else:
    print("AI says: Fail ❌")

print()


# Example 5: AI Even/Odd Checker 
# AI checks if a number is even or odd.

print(" Example 5: AI Even/Odd Checker ")

numbers = [3, 8, 15, 22, 7]

for num in numbers:
    if num % 2 == 0:
        print(f"AI says: {num} is Even ")
    else:
        print(f"AI says: {num} is Odd ")

print()
print(" All 5 Examples Done! ")

print("All Done!")



#       5 Simple Examples of Loops

# A loop means doing something again and again.
# Just like in real life — you brush your teeth
# EVERY day, you eat breakfast EVERY morning.
# That's a loop! Let's see some examples. 👇



# Example 1: Morning Routine ☀️
# Every morning you do the same tasks — wake up,
# brush teeth, take a shower, eat breakfast, go
# to school/work. A for loop does them one by one.


print("☀️ Example 1: My Morning Routine")
print()

morning_tasks = [
    "Wake up from bed 🛏️",
    "Brush my teeth 🪥",
    "Take a shower 🚿",
    "Eat breakfast 🍳",
    "Go to school/work 🎒"
]

step = 1
for task in morning_tasks:
    print(f"  Step {step}: {task}")
    step = step + 1

print("  ✅ Morning routine done! Ready for the day!")
print()


# Example 2: Counting My Shopping Bill 🛒
# You bought some items from a shop. Now you want
# to add up the prices one by one — just like a
# cashier does at the counter.

print("🛒 Example 2: Counting My Shopping Bill")
print()

items = {
    "Milk": 120,
    "Bread": 80,
    "Eggs": 200,
    "Juice": 150,
    "Biscuits": 50
}

total_bill = 0

for item_name, price in items.items():
    total_bill = total_bill + price
    print(f"  🔹 {item_name} = Rs.{price}  (Running total: Rs.{total_bill})")

print(f"  💰 Total Bill: Rs.{total_bill}")
print()


# Example 3: Studying for Exams 📚
# You have 5 chapters to study. You study one
# chapter at a time. After each chapter, you
# check how many are left. When all are done,
# you say "I'm ready for the exam!"

print("📚 Example 3: Studying for Exams")
print()

chapters_left = 5

while chapters_left > 0:
    print(f"  📖 Studying chapter {6 - chapters_left}... ({chapters_left} left to go)")
    chapters_left = chapters_left - 1

print("  🎉 All chapters done! I'm ready for the exam!")
print()


# Example 4: Teacher Calling Names in Class 
#
# Imagine a teacher has 3 classes.
# In EACH class, the teacher calls the name of
# EVERY student to check attendance.
#
# So the teacher first goes to Class 1,
#   calls Student 1, Student 2...
# Then goes to Class 2,
#   calls Student 1, Student 2...
# And so on.
#
# This is a NESTED LOOP:
#   Outer loop = goes class by class
#   Inner loop = calls each student in that class


print(" Example 4: Teacher Calling Names")
print()

# These are the classes
classes = ["Class A", "Class B", "Class C"]

# These are the students in each class
students = ["Ali", "Sara", "Ahmed"]

# Outer loop — teacher goes to each class
for my_class in classes:
    print(f"   Teacher enters {my_class}:")

    # Inner loop — teacher calls each student
    for student in students:
        print(f"      '{student}! Are you here?'")

    print(f"   {my_class} attendance done!")
    print()

print("  All classes checked! Attendance complete!")
print()



# Example 5: Looking for Lost Keys 🔑
# You lost your keys! You check your pockets,
# bag, table, sofa... one by one. The moment
# you find them, you STOP looking (break).

print("🔑 Example 5: Looking for My Lost Keys")
print()

places = [
    "Pocket",
    "Bag",
    "Table",
    "Sofa",        # <-- Keys are here!
    "Bedroom",
    "Kitchen"
]

keys_found = False

for place in places:
    print(f"   Checking {place}...")
    if place == "Sofa":
        print(f"  Found my keys on the {place}! No need to look further!")
        keys_found = True
        break  # stop looking, we found them!

if not keys_found:
    print("   Couldn't find the keys anywhere...")

print()
print("=" * 45)
print("   All 5 Loop Examples Done!")
print("=" * 45)
print("All Done!")