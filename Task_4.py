import random
from scoreboard_task4 import Scoreboard

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
score=Scoreboard()
game_stop=False
while not game_stop:
    user_choice = int(input("enter your choice, 1 for rock, 2 for paper and 3 for scissors:"))
    if user_choice == 1:
        print(f"Your choice is {rock}")
    elif user_choice == 2:
        print(f"Your choice is {paper}")
    elif user_choice == 3:
        print(f"Your choice is {scissors}")
    else:
        print("invalid input")

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        print(f"Computer's choice is {rock}")
    elif computer_choice == 2:
        print(f"Computer's choice is {paper}")
    else:
        print(f"Computer's choice is {scissors}")

    if user_choice==computer_choice:
        print("draw")
        score.update_score()
    elif user_choice<computer_choice:
        print("ÿou loose :(")
        score.you_loose()
    elif user_choice>computer_choice:
        print("you win!!")
        score.you_win()
    elif user_choice == 1 and computer_choice == 3:
        print("you win!!")
        score.you_win()
    elif user_choice == 3 and computer_choice == 1:
        print("you loose :(")
        score.you_loose()

    # print(score.update_score())

    x=input("Do you want to continue? Type 'y' or 'n':").lower()
    if x=="n":
        game_stop=True


