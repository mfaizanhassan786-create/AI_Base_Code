
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


# - Example 4: AI Grade Checker 
# AI checks your marks and tells your grade.

print("--- Example 4: AI Grade Checker ---")

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


# ---------- Example 5: AI Even/Odd Checker ----------
# AI checks if a number is even or odd.

print("--- Example 5: AI Even/Odd Checker ---")

numbers = [3, 8, 15, 22, 7]

for num in numbers:
    if num % 2 == 0:
        print(f"AI says: {num} is Even ✅")
    else:
        print(f"AI says: {num} is Odd 🔵")

print()
print("--- All 5 Examples Done! ---")
