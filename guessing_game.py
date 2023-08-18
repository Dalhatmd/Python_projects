import random

number = random.randint(1, 11)
while True:
  guess = int(input("Guess a number between 1 - 10: "))
  if guess not in range(1, 11):
    print("I said between 1 - 10!")
  if guess == number:
    print("You got it!")
    break
  else:
    print("Try Again")
 