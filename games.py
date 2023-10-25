import random
def play_game():
  target_number = random.randint(1, 100)
  attempts = 0

  print("Welcome to the Number Guessing Game!")
  print("I have a number, in mind between 1 and 100.")

  while True:
    guess = int(input("Take a guess: "))

    if guess < target_number:
      print("Too low! Give it another try.")
    elif guess > target_number:
       ! Give it another try.")
    else:
      print(f"Congratulations! You guessed the number, in {attempts} tries.")
      break

    if attempts >= 5:
      print(f"Game over! The number was {target_number}.")
      break

  play_again = input("Would you like to play ? (yes/no): ")

  if play_again.lower() == "yes":
    play_game()
  else:
    print("Thank you for playing!")
    
play_game()

