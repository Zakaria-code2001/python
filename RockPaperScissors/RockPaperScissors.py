rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#human part
game_images = [rock, paper, scissors]

human_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
print(game_images[human_choice])

#the computer part

import random

computer_choice = random.randint(0, 2)
print(f"Computer Choose : {computer_choice} ")
if computer_choice == 0:
  print(f"{rock}")
elif computer_choice == 1:
  print(f"{paper}")
elif computer_choice == 2:
  print(f"{scissors}")

if human_choice == 0 and computer_choice == 0 or human_choice == 1 and computer_choice == 1 or human_choice == 2 and computer_choice == 2:
  print("Nobody loses!")
if human_choice == 0 and computer_choice == 1:
  print("You lose try again!")
if human_choice == 1 and computer_choice == 0:
  print("You Win !")
if human_choice == 1 and computer_choice == 2:
  print("You lose try again!")
if human_choice == 2 and computer_choice == 1:
  print("You Win !")
