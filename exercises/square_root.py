import math

def main():
    x = int(input("Please the number that is needed to be square rooted: "))
    guess = x / 2
    no_of_guesses = int(input("Enter number of trials to accuracy: "))
    y = 0
    while True:
        guess = (guess + x/guess)/2
        if guess - y == 0:
            break
        else:
            y = guess
    print(guess - math.sqrt(x), guess)

main()
