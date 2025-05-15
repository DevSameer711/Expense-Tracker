import random
import time

print("Welcome to the Multi-Level Number Guessing Game!")
name = input("Please enter your name: ")
print("Hello", name, "! Let's start the game.")

def game(level):
if level == 1:
n = random.randint(1, 10)
elif level == 2:
n = random.randint(1, 50)
else:
n = random.randint(1, 100)

attempts = 0
print("Level", level, "- Guess a number!")

while True:
g = input("Enter a number: ")
if g.isdigit():
g = int(g)
if g == n:
print("Correct!")
print("You took", attempts, "attempts.")
break
elif g &gt; n:
print("Lower")
attempts = attempts + 1
elif g &lt; n:
print("Higher")

attempts = attempts + 1
else:
print("Invalid input")

print("Level", level, "completed!")

def leaderboard(scores):
print("\n=== Leaderboard ===")
for i in range(len(scores)):
print(scores[i][0], "-", scores[i][1], "points")
print("===================\n")

def start():
scores = []
while True:
level = 1
totalScore = 0
time.sleep(1)
startTime = time.time()
game(level)
totalScore += 10
level = level + 1
game(level)
totalScore += 20
level = level + 1
game(level)
totalScore += 30
endTime = time.time()
duration = endTime - startTime
print("You finished all levels in", round(duration, 2), "seconds.")
scores.append((name, totalScore))
leaderboard(scores)
again = input("Play again? (y/n): ")
if again != "y":

print("Thanks for playing!")
break
else:
continue

start()