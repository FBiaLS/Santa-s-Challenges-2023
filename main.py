import random

gifts = []
game = True
guesses = 0
points = 0

def pickTransport():
  print("I didn't quite catch that, which one?")
  print("Sleigh")
  print("Reindeer")
  print("Ice skates")
  transport = input()
  if transport == "ice skates":
    transport = "skates"
  elif transport != "sleigh" and transport != "reindeer":
    pickTransport()
  return transport

def challengeOne():
  global game
  global guesses
  print("We made it! The first challenge is to guess the average number of houses I can visit in one second")
  print("Do you want a clue?")
  clue = input()
  if clue == "yes":
    print("Ok ", name, " your clue is... it is between 1 and 100 houses")
  houses = random.randint(0,100)
  print("Take a guess!")
  guess = int(input())
  while game:
    guesses = guesses + 1
    if guess == houses:
      print("Yay you got it!")
      print("It only took ", guesses, " guesses! Thats amazing!")
      game = False
      if guesses == 0:
        points = 10
      elif guesses <= 5:
        points = 3
      elif guesses <= 7:
        points = 2
      elif guesses <= 10:
        points = 1
    else:
      if guess > houses:
         print("The number is less than ", guess)
      else:
        print("The number is greater than ", guess)
      print("Have another guess!")
      guess = int(input())

def challengeTwo():
  global game
  global points
  print("Time for the second challenge... hangman!")
  game = True
  start = "false"
  lives = 6 
  word = ["santa", "snowman", "present", "christmas", "tree", "elves", "reindeer", "sleigh", "wreath", "mistletoe", "holly", "krampus", "nicholas"] 
  dash = []
  letter = []
  num = random.randrange(0, len(word) - 1) 
  ans = word[num] 
  length = len(ans) 
  print("This is your word:")
  print()
  for x in range(length):
    dash.append("-")
  print("".join(dash))
  print()
  print("You have 6 lives")
  print("Guess a letter!")
  print()
  while game: 
    hangmanGuess = input()
    if hangmanGuess in ans:
      num = ans.count(hangmanGuess)
      for x in range(len(ans)):
        if hangmanGuess == ans[x]:
          dash.pop(x)
          dash.insert(x, hangmanGuess)
      print("".join(dash))
      print()
      print(hangmanGuess, " is in the word!")
    else:
      start = "true"
      letter.append(hangmanGuess)
      print("".join(dash))
      print()
      print(hangmanGuess, " is not in the word") 
      lives = lives - 1 
      if lives == 0:
        game = False 
        print("Unlcuky! Don't worry, there's still one challenge left") 
      else:
        print("Guess another letter!")
    print()
    if start == "true":
      print("Guessed letters:")
      print(sorted(letter))
      print()
    if lives == 5:
      print("-------     ")
    elif lives == 4:
      print("|")
      print("|")
      print("|")
      print("|")
      print("|")
      print("--------   ")
    elif lives == 3:
      print("|--------")
      print("|       |")
      print("|")
      print("|")
      print("|")
      print("---------      ")
    elif lives == 2:
      print("|---------")
      print("|        |")
      print("|        0")
      print("|")
      print("|")
      print("|")
      print("----------     ")
    elif lives == 1:
      print("|---------")
      print("|        |")
      print("|        0")
      print("|       /|\\")
      print("|")
      print("-----------       ")
    elif lives == 0:
      print("|---------")
      print("|        |")
      print("|        0")
      print("|       /|\\")
      print("|       / \\")
      print("|")
      print("-----------      ")
      print()
      print("The word was", ans)
    if "-" in dash:
      lives = lives
    else:
      print("You did it!")
      game = False
      if lives == 6:
        points += 5
      elif lives >= 4:
        points += 3
      elif lives >= 2:
        points += 2
      elif lives == 1:
        points += 1

print("Welcome to the christmas present hunt!")
print("What 3 things would you like for christmas? (in order of preference)")
for i in range(3):
  gifts.append(input())
print("Well I'm Santa Claus and my elves will start preparing!")
print("You will face 3 challenges... wait... I forgot to ask your name! What is it?")
name = input()
print("Well hello ", name, " lets begin... what mode of transport shall we use?")
print("Sleigh")
print("Reindeer")
print("Ice skates")
transport = input()
if transport.lower() == "ice skates":
  transport = "skates"
elif transport.lower() != "sleigh" and transport.lower() != "reindeer":
  transport = pickTransport()
print("Lets head to the", transport, "!")
challengeOne()
challengeTwo()
print("Now it's time for the final challenge... all you need to do is answer ONE question. Are you ready?")
clue = input()
while clue != "yes":
    print("How aout now?")
    clue = input()
print("Is santa real?")
clue = input()
print("Now you have completed all 3 challenges, the elves have now prepared you a present based on how good you've been this year (at the challenges)")
if points == 6:
  gift = gifts[1]
elif points > 6:
  gift = gifts[2]
else:
  gift = gifts[0]
print("You're present is a... ", gift)
