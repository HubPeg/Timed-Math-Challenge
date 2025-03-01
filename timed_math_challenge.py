import random
import time

# These are constant Variables. They are not going to change
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL_PROBLEMS = 6

# write a function


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    # This "random.choice" picks a random Operator from the OPERATORS Values.
    operator = random.choice(OPERATORS)

    # This generates the Equation. Left Random number (operator) Right Random number.
    expr = str(left) + " " + operator + " " + str(right)
    # Answer is equal to a function "eval" // This will return the Answer from the Expression.
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem " + str(i + 1) + ": " + expr + "= ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
# This rounds the number to 2 digits.
total_time = round(end_time - start_time, 2)

print("---------------------")
print("You are amazing! You finished in", total_time, "sendonds!")
