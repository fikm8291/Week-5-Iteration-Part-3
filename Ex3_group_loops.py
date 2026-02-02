# -------------------------------------------
# Exercise 3: Group Loops
# -------------------------------------------
#
# GOAL:
# 1. Combine all skills: Variables, Input, Lists, Loops, and Logic.
# 2. Practise the "Relay Race" Git workflow in groups.
#
# CONCEPT:
# Real programs rarely use just one concept.
# - You might use a 'while' loop to validate input.
# - You might use a 'for' loop to iterate through a list of data.
# - You might use 'if/else' inside a loop to make decisions.
#
# GROUP RULES:
# - Work together on ONE computer at a time.
# - Switch computers/drivers after every task.
# -------------------------------------------


# -------------------------------------------
# Task 1: The Guest List (Lists & Loops)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: The Guest List\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for the names of three friends (one by one).
# 2. Store these names in three separate variables.
# 3. Create a list called 'friends' containing those variables.
#    Hint: my_list = [var1, var2, var3]
# 4. Use a 'for' loop to print a greeting for each friend in the list.
#
# Example Output:
# Hello, Sarah!
# Hello, Mike!
# ...

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Open the terminal.
# 3. Run:
#    git add Ex3_group_loops.py
#    git commit -m "Completed Task 1 - guest list"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 2: The Range Validator (While & Logic)
# -------------------------------------------
# INSTRUCTION: You are now at a new computer.
# 1. Open the terminal.
# 2. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 2: The Range Validator\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user to enter a number between 1 and 10.
# 2. Create a 'while' loop that keeps running if the number is valid.
#    WAIT! actually, we usually loop *while the number is INVALID*.
#    Logic: "While number is < 1 OR number > 10..."
# 3. Inside the loop:
#    - Print "Invalid number, try again."
#    - Ask for the input again.
# 4. Outside the loop (when it finishes), print "Number accepted!"

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex3_group_loops.py
#    git commit -m "Completed Task 2 - validation"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 3: The Quiz Master (Iterating Lists)
# -------------------------------------------
# INSTRUCTION: Get the code from the previous Driver.
# 1. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 3: The Quiz Master\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a list called 'questions' with 3 distinct questions.
#    e.g. questions = ["What is 2+2?", "Colour of the sky?", "Capital of UK?"]
# 2. Use a 'for' loop to ask every question in the list.
# 3. Inside the loop:
#    - Use input() to ask the specific question.
#    - Use if/else to check the answer (you can decide the correct answers).
#    - Print "Correct" or "Wrong".

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex3_group_loops.py
#    git commit -m "Completed Task 3 - quiz list"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Keep swapping computers after each extension task.

# Extension 1: The Strict Gatekeeper (Empty Strings)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: The Strict Gatekeeper\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a text input (e.g. "Enter your password").
# 2. Write a 'while' loop that checks if the input is empty ("").
# 3. Keep looping until they actually type something.
# 4. Print "Thank you" when done.

# Write your code below:


# Extension 2: Multiple Choice Logic
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Multiple Choice Logic\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user to choose "A", "B", or "C".
# 2. Use a loop to ensure they ONLY type A, B, or C.
# 3. Once valid, use if/elif/else to give a different response for each letter.
#
# Hint: while choice != "A" and choice != "B" and choice != "C":

# Write your code below:


# Extension 3: The Arcade Machine (Nested Loops)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: The Arcade Machine\n"
    + "-------------------------------------------")

# This is a "Loop inside a Loop".
#
# TODO:
# 1. Create an outer 'while' loop that asks for a "Player Name".
#    - If the name is empty (user just pressed Enter), BREAK the loop (stop game).
# 2. Inside this loop, run your Quiz code from Task 3 (the 'for' loop).
# 3. When the quiz finishes, the outer loop should run again for the next player.
#
# Structure:
# while True:
#     name = input("Player Name (or Enter to quit): ")
#     if name == "":
#         break
#     print(f"Welcome {name}!")
#     # ... Insert Quiz For-Loop here ...

# Write your code below:


# -------------------------------------------
# ADVANCED ACTIVITY: The Ultimate Combo
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Ultimate Combo\n"
    + "-------------------------------------------")

# TODO:
# Combine everything you have learned into one seamless program.
# 1. Ask the user for a number (validated with a while loop).
# 2. Generate that many "Friend" slots.
# 3. Use a loop to ask for the name of each friend.
# 4. For each friend, ask them a quiz question.
# 5. Keep score! (Create a 'score' variable and add +1 for correct answers).
# 6. Print the final results.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex3_group_loops.py
#    git commit -m "Completed extensions and advanced"
#    git push origin main
# 3. Check GitHub to confirm your group's final version appears.
# -------------------------------------------
