import random
import sys


def main():
    answer = getRandomWord()
    chances = 0 
    guess = input("Enter a 5 letter guess?\n")
    while chances < 6 and guess != answer:
        if chances > 0:
            guess = input("Enter a 5 letter guess?\n")
        while len(guess) < 5 or len(guess) > 5:
            guess = input("Enter a random 5 letter guess: ")    
        printGuessColors(guess, answer)
        chances += 1
    if guess == answer:
        print(f"You Won! That took {chances} guess(es).")
    else:
        print(f"You lost. The answer was {answer}.")


def printGuessColors(guess, answer):
    for l in range(len(guess)):
        if guess[l] == answer[l]:
            print(f"{guess[l]} -", letterColor(l, guess, answer) )
        elif guess[l] != answer[l] and guess[l] not in answer:
            print(f"{guess[l]} -", letterColor(l, guess, answer) )
        else:
            print(f"{guess[l]} -", letterColor(l, guess, answer) )
    

def letterColor(index, guess, answer):
    if guess[index] == answer[index]:
        return "Green"
    elif guess[index] != answer[index] and guess[index] not in answer:
        return "Red"
    else:
        return "Yellow"



def getRandomWord():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()