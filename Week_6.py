# PRACTICAL TASK : 1

secret_number = 24

for attempt in range(3):
    guess = int(input("Guess the number: "))  
    if guess == secret_number:
        print("Congratulations! You guessed it!!!")  
        break 
    else:
        print("Wrong guess. Try again!")  

else:
    print(f"Attempts Over!!! The correct number was {secret_number}.")

# PRACTICAL TASK : 2

"""Two Most Interesting Things I Learned in Python:"""
# 1. Using if, elif, and else statements really helped me understand how computers make decisions. It felt like teaching the program how to think logically, which I found really fun and useful.

# 2. Writing my own functions was another exciting part. It made my code cleaner and easier to manage. I liked how I could reuse the same block of code without rewriting everything again and again.

