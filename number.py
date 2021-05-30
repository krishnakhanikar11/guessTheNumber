# generate number between 1-100
# ask user for difficulty level and give them no of turns
# check user ans with the number generated and give them feedback
# reduce no. of turns if ans is wrong 
# repeat the code till answer is correct or number of turns is Zero

import random
easy_level = 10
hard_level = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 101)
level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

def difficulty(level):
  if level =="easy":
    return easy_level
  else:
    return hard_level


game_is_on = True

turns = difficulty(level)



while game_is_on:
  guess=int(input("Make a guess:"))
  
  if guess == answer:
    print("You won")
    game_is_on=False
  elif guess > answer:
    turns = turns - 1
    print(f"Too High{turns}")
  else:
    turns = turns - 1
    print(f"Too Low{turns}")

  if turns == 0:
    game_is_on = False
    print("You ran out of chances! GAME OVER")
