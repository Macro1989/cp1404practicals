"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    score_descriptor(score)
    rand_score = random.randint(0, 100)
    print(rand_score)
    score_descriptor(rand_score)





def score_descriptor(score):

    if score < 0 or score > 100:
        outcome = "Invalid score"

    elif score > 90:
        outcome = "Excellent"

    elif score >= 50:
        outcome = "Passable"

    else:
        outcome = "Bad"
    print(outcome)


main()