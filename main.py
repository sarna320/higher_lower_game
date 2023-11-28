import art
import game_data
import random
import os


score = 0
while True:
    os.system("cls")
    print(art.logo)
    if score > 0:
        print(f"You are right! Current score: {score}")
    compare_1 = random.choice(game_data.data)
    compare_2 = random.choice(game_data.data)
    print(
        f"Compare A: {compare_1['name']},a {compare_1['description']}, from {compare_1['country']}"
    )
    print(art.vs)
    print(
        f"Against B: {compare_2['name']},a {compare_2['description']}, from {compare_2['country']}"
    )

    correct_answer = "B"
    if compare_1["follower_count"] > compare_2["follower_count"]:
        correct_answer = "A"

    if correct_answer == input("Who has more followers? Type 'A' or 'B':"):
        score += 1
    else:
        print(f"Sorry, that is wrong. Final score: {score}")
        score = 0
        break
