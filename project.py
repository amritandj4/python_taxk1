#UNICOMPILER TASK 1
import random
min_value=int(input("enter lower bound"))
max_value=int(input("enter upper bound"))
n=random.randint(min_value,max_value)
guess=int(input("enter an integer which one you guess"))
while n!="guess":
    if guess<n:
        print("guessing number is low than n")
        guess=int(input("enter an integer from 1 to 100"))
    elif guess>n:
        print("guessing number is higher than n")
        guess=int(input("enter an integer from 1 to 100"))
    else:
        print("good work you guess no")
        break
    

