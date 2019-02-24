import random

numbers = input("Enter the list of numbers separated by commas: ")
num_list = numbers.split(",")
secure_random = random.SystemRandom()
random_num = secure_random.choice(num_list)
print("Your random number is: ", random_num)

