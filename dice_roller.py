import random

print("welcome to the Dice roller")

while True:
    input("\n press ENTER to roll dice...")

    roll = random.randint(1, 6)
    print(f"you rolled {roll}")

    again = input("\n press ENTER to roll again? (yes/no)...").lower()
    if again == "yes":
        print("Thanks for playing!")
        break

