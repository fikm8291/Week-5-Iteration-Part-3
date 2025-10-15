# -------------------------------------------
# Exercise 3: Group Loops Exercise
# -------------------------------------------
# Work in groups of 2–3.
# You’ll combine everything learned so far:
# - Variables
# - Input and Output
# - Decision Making (if / elif / else)
# - Loops (while or for)
#
# Work together on ONE computer at a time:
# - Current learner completes the task.
# - Then git add, commit, and push changes.
# - Next learner moves to their computer, pulls the repository, and continues.
# - Repeat until everyone has contributed.

# -------------------------------------------
# Task 1: Collect Multiple Inputs
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Collect Multiple Inputs\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user for the names of three friends (or classmates).
# 2. Store them in separate variables.
# 3. Use a loop to print a greeting for each friend.
#
# Example idea:
# friend1 = Use input() to ask for the name
# friend2 = ...
# friend3 = ...
# friends = [friend1, friend2, friend3]  # put variables in a list
# for name in friends:
#     print("Hello " + name)  # loop through and greet

# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Hint: save your work and commit it to your repository.
# Next learner should pull the latest changes before continuing.
# -------------------------------------------


# Task 2: Number Input and Decisions
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Number Input and Decisions\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user to enter a number between 1 and 10.
# 2. Use if / elif / else to print:
#    - Message if the number is too low (<1)
#    - Message if the number is too high (>10)
#    - Message if the number is in the correct range
# 3. Use a loop so that if the number is invalid, the user is asked again.
#
# Example idea:
# number = Use input() to ask the user for a number # HINT: When using input(), the user response is always saved as a string
# while some_condition_is_not_met:
#     print("Invalid number, try again")
#     number = Use input() to ask the user for a number
# if some_condition1:
#     print("Message for first case")
# elif some_condition2:
#     print("Message for second case")
# else:
#     print("Message for other cases")

# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Hint: save, commit, and push your work before the next learner continues.
# Next learner should pull first to get your changes.
# -------------------------------------------


# Task 3: Mini Quiz Project Using a List
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Mini Quiz Project Using a List\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user multiple questions.
# 2. Use a list to store your questions. HINT: Look at Task 1 to see how this is done.
#    Example of a list:
#    questions = ["What is 2 + 2?", "Type the colour of the sky.", "First letter of the alphabet?"]
# 3. Use a loop to go through the list of questions and ask each one.
# 4. Use if / elif / else to give feedback for each answer.
#
# Example idea:
# for i in questions:
#     answer = input(i + " ")
#     # if answer == "something":
#     #     print("Good!")
#     # elif answer == "something else":
#     #     print("Try again")
#     # else:
#     #     print("Check your answer")

# Write your code below:


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Keep swapping computers after each extension task.

# Extension 1: Input Validation
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1: Input Validation\n"
    + "-------------------------------------------")
# TODO:
# 1. Make sure that text answers are not empty.
# 2. Make sure number answers are within a valid range.
# 3. Keep asking until valid input is given.
#
# Example idea (syntax only):
# answer = input("Enter something: ")
# while answer_is_empty:
#     print("You must type something")
#     answer = input("Try again: ")

# Write your code below:


# Extension 2: Multiple Feedback Options
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2: Multiple Feedback Options\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user to input 1 of at least 3 possible responses. E.g. "Type A, B, or C: "
# 2. Use if / elif / else to handle different answers.
# 3. Use the correct type of loop (for/while) to repeat question if input is not valid.
#
# Example idea (syntax only):
# answer = Use input() to ask for a response
# if answer == "A":
#     print something here
# elif answer == "B":
#     print something here
# else:
#     print something here

# Write your code below:


# Extension 3: Repeat Quiz for Another User
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 3: Repeat Quiz for Another User\n"
    + "-------------------------------------------")
# TODO:
# 1. Create a simple mini-quiz first. 
#    For example, create a list of 2–3 questions:
#    questions = ["What is 2 + 2?", "What colour is the sky?", "When were women first allowed to vote in the UK?"]
# 2. Ask the first user to enter their name.
# 3. Loop through the questions and ask each one.
#    Use if / elif / else to give feedback for each answer.
# 4. After the first user finishes, ask for a new user's name.
#    If they enter a name, repeat the same quiz for the new user.
#    If they press Enter without typing a name, stop the program.
# 5. Repeat this until no new name is entered.
#
# HINTS:
# - Use a while loop to keep asking for new users while the name is not empty.
# - Inside the while loop, use a for loop to ask each question.
# - Give feedback for each answer using if / elif / else.

# Example idea (not the answer):
# questions = ["2 + 2?", "Sky colour?"]
# user_name = input("Enter your name (or press Enter to stop): ")
# while user_name != "":
#     print("Welcome", user_name + "!")
#     for question in questions:
#         answer = input(question + " ")
#         # check answer and print feedback
#     user_name = input("Enter another user's name (or press Enter to stop): ")

# Write your code below:


# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the names of three friends and greet each using a loop.
# 2. Ask the user to enter a number between 1 and 10, with loop validation (keep asking the user for a number until they enter one that is valid).
# 3. Run a mini-quiz using a list of questions.
# 4. Use loops to repeat all tasks above and if / elif / else to give feedback.
# Hint: combine loops and decisions, and you can nest loops inside loops.

# Write your code below:


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once your group has completed the exercise and optional extensions:
# 1. Save your file.
# 2. Open the terminal and use Git commands to stage, commit, and push your changes.
#    (Hint: recall the commands for adding, committing, and pushing.)
# 3. Make sure each learner has pulled the latest changes so that the repository is up to date.
# 4. Check GitHub to confirm your group's final version appears.
# -------------------------------------------
