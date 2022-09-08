import random

lucky_numbers = []
user_numbers = []
correct_numbers = 0

print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("                   Welcome to Xiao Lotto")
print("------------------------------------------------------------")
print("                   Enter 6 Lucky Numbers")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")


# For generating random lucky numbers
for num in range(0, 6):
    random_num = random.randint(1, 50)
    lucky_numbers.append(random_num)

# For getting user numbers
for num in range(0, 6):
    user_num = int(input("Enter a lucky number: "))
    user_numbers.append(user_num)

# For checking if got any lucky numbers
for lucky_num in lucky_numbers:
    for user_num in user_numbers:
        if user_num == lucky_num:
            correct_numbers += 1
            # correct_numbers = correct_numbers + 1


#output
print(f"You guessed {correct_numbers} correct numbers")

print(f"Final Result: {lucky_numbers}")



