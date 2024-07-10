import random

z = True
while z == True:
    options = ["1-Snake", "2-Water", "3-Gun"]
    answers = ["Snake", "Water", "Gun"]
    print("-----WELLCOME TO SNAKE,WATER,GUN GAME-----\n")
    for i in range(len(options)):
        print(options[i])
    try:
        user_choice = int(input("Enter your choice:"))
    except:
        print("some error occured")

    comp_choice = random.randint(0, 2)

    if (options[user_choice - 1] == options[comp_choice]):
        print(
            f"You choose {answers[user_choice-1]} and computer also choose {answers[comp_choice]} so the match is draw"
        )

    elif (options[user_choice - 1] == options[0]
          and options[comp_choice] == options[1]):
        print(
            f"You choose {answers[user_choice-1]} and computer choose {answers[comp_choice]} you win"
        )

    elif (options[user_choice - 1] == options[0]
          and options[comp_choice] == options[2]):
        print(
            f"You choose {answers[user_choice-1]} and computer choose {answers[comp_choice]} you lose"
        )

    elif (options[user_choice - 1] == options[1]
          and options[comp_choice] == options[0]):
        print(
            f"You choose {answers[user_choice-1]} and computer choose {answers[comp_choice]} you lose"
        )

    elif (options[user_choice - 1] == options[1]
          and options[comp_choice] == options[2]):
        print(
            f"You choose {answers[user_choice-1]} and computer choose {answers[comp_choice]} you won"
        )

    elif (options[user_choice - 1] == options[2]
          and options[comp_choice] == options[0]):
        print(
            f"You choose {answers[user_choice-1]} and computer choose {answers[comp_choice]} you won"
        )

    elif (options[user_choice - 1] == options[2]
          and options[comp_choice] == options[1]):
        print(
            f"You choose {answers[user_choice-1]} and computer choose {answers[comp_choice]} you lose"
        )
