import random

wins = 0
losses = 0

def rps():
  my_choice = raw_input("Rock, paper or scissors?")
  choices = ["rock", "paper", "scissors"]
  result = ""
  global wins
  global losses
  comp_choice = random.choice(choices)
  if my_choice == "rock":
    if comp_choice == "rock":
    	print "Computer chose: rock. It's a Tie!"
    elif comp_choice == "paper":
      print "Computer chose: paper. You Lose!"
      losses = losses + 1
    else:
      print "Computer chose: scissors. You Win!!"
      wins = wins + 1
  elif my_choice == "paper":
    if comp_choice == "rock":
      wins = wins + 1
      print "Computer chose: rock. You Win!!"
    elif comp_choice == "paper":
      print "Computer chose: paper. It's a Tie!"
    else:
      print "Computer chose: scissors. You Lose!"
      losses = losses + 1
  else:
    if comp_choice == "rock":
      losses = losses + 1
      print "Computer chose: rock. You Lose!"
    elif comp_choice == "paper":
      print "Computer chose: paper. You Win!!"
      wins = wins + 1
    else:
      print "Computer chose: scissors. It's a Tie!"

def play_again():
  play_input = raw_input("Would you like to play again?")
  if play_input == "yes":
    rps()
    score(wins,losses)
    play_again()
  else:
    print "Goodbye!"


def score(w,l):
  if w < l:
    print ("You: %d, Computer: %d. Better step up your game!" % (w, l))
  elif w == l:
    print ("You: %d, Computer: %d. Hmm who is better?" % (w, l))
  else:
    print ("You: %d, Computer: %d. Wow you're good at this game!" % (w, l))


rps()
score(wins,losses)
play_again()
