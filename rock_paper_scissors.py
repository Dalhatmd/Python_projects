import random

moves = ["rock", "paper", "scissors"]
on = True
while on:
  print("\t\tWelcome to My rock paper scissors game\n \t\tEnter \"Quit\" to quit")
  
  user = input("\t\tPlease enter a move: ")
  print("\t\tYou chose: ", user)
  if user.lower() == "quit":
    print("\t\tQuitting. Thank you for playing")
    on = False
  if user.lower() not in moves:
    print("\t\tPlease choose either Rock paper or scissors ")
    continue
    on = False
    
  computer = random.choice(moves)
  print("\t\t Computer chose: ",computer)
  if user == computer:
    print("\t\tYou both chose: ",user, " Please. try again")
  elif user == "rock" and computer == "paper":
    print("\t\tComputer Won!")
  elif user == "paper" and computer == "rock":
    print("\t\tYou won!!")
  elif user == "scissors" and computer == "rock":
    print("\t\tComputer Won!")
  elif user == "scissors" and computer == "paper":
    print("\t\t You won!!")
  elif user == "rock" and computer == "scissors ":
    print("\t\t You Won!!")
    
  
  