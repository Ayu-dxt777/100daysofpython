

logo = '''   ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       '''
import random
MY_GUESS = random.randint(1,100)
# print(MY_GUESS) ----> Psst, you can use this to check for the number guessed by the computer
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

def count(counts, attempts):
  print(f"The correct answer is {MY_GUESS}")
  no_of_guesses = False
  count = 1 
  print("You have 10 attempts remaining to guess the number.\n")
  while no_of_guesses == False and count <= counts:
    guess = int(input("Make a guess: "))
    if guess == MY_GUESS:
      print(f"You got it! The answer was {MY_GUESS}")
      no_of_guesses = True
    elif guess < MY_GUESS:
      print(f"Too Low.\nGuess Again.\n")
      count += 1
      attempts -= 1
      print(f"You have {attempts} attempts remaining")
    elif guess > MY_GUESS:
      print(f"Too High.\nGuess Again.\n")
      count += 1
      attempts -= 1
      print(f"You have {attempts} attempts remaining")

if difficulty == 'easy':
  count(10, 10)
elif difficulty == 'hard':
  count(5, 5)
