import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    ___________
---'   ________)____
          __________)
          ___________)
         ___________)
---.______________)

'''
scissors = '''
    _______
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)

'''

#Write your code below this line 👇
again = "Y"
while again == "Y":
    choice = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "
        ))
    computerChoice = r.randint(0, 2)

    if choice == 0:
        print(rock)
        print("Computer chose:")
        if computerChoice == 0:
            print(rock)
            print("you both chose Rock, it's a tie!")
        elif computerChoice == 1:
            print(paper)
            print("Paper covers Rock, you lose!")
        elif computerChoice == 2:
            print(scissors)
            print("Rock breaks Scissors, you win!")

    elif choice == 1:
        print(paper)
        print("Computer chose:")
        if computerChoice == 0:
            print(rock)
            print("Paper covers Rock, you win!")
        elif computerChoice == 1:
            print(paper)
            print("You both chose paper, it's a tie!")
        elif computerChoice == 2:
            print(scissors)
            print("Scissors cut paper, you lose!")

    elif choice == 2:
        print(scissors)
        print("Computer chose:")
        if computerChoice == 0:
            print(rock)
            print("Rock breaks Scissors, you lose!")
        elif computerChoice == 1:
            print(paper)
            print("Scissors cut paper, you win!")
        elif computerChoice == 2:
            print(scissors)
            print("You both chose Scissors, it's a tie!")
    again = input("\nWould you like to play again? ( Y or N ) ").upper()
    print("")
