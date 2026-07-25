# Pythin number guessing game
import random 

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0 
is_running = True

print("Python Number Guessing Game")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"Please enter a number between {lowest_num} and {highest_num}.")
            continue

        if guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {answer} in {guesses} attempts.")
            is_running = False
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
 










   
       
        
      
