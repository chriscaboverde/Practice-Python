# From: https://www.youtube.com/watch?v=DLn3jOsNRVE

print("Welcome to my computer quiz!")
play = input("Do you want to play a game? ")
if play.lower() != "yes": #convert all yes answers to lower case
    quit()
print("OK! Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer != "central processing unit":
    print("Sorry. Try again.")
else:
    print("Correct!")
    score += 1

answer = input("What is the capital of Zimbabwe? ")
if answer != "Harare":
    print("Sorry. Try again.")
else:
    print("Correct!")
    score += 1

answer = input("Who is the author of Wealth of Nations? ")
if answer != "Adam Smith":
    print("Sorry. Try again.")
else:
    print("Correct!")
    score += 1

answer = input("What is Chandler Bing's job? ")
if answer == "statistical analysis and data reconfiguration":
    print("Correct!")
    score += 1
elif answer == "transponster":
    print("That's not even a word!")
else:
    print("Sorry. Try again.")

print("You got " + str(score) + " points!") # string because score is a number; convert number to string