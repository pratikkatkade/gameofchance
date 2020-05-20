import random
money = 100

#Write your game of chance functions here
def coin_toss(bet, guess):
  #Need to ensure that the bet is higher than 0 first
  if bet <= 0:
    print("Your bet needs to exceed 0 to play.")
    return 0
  
  #Flip the coin
  print("Okay, let's flip! You guessed, " + guess)
  coin_result = random.randint(0,1)
  
  #Show the result to the user?
  if coin_result == 0:
    print("Heads!")
  elif coin_result == 1:
    print("Tails!")
    
    #Calculates the result
    if (coin_result == 0 and guess == "Heads") or (coin_result == 1 and guess == "Tails"):
      print("You win $" + str(bet) + ", well done!")
      return bet
    else:
      print("Better luck next time! You lost $" + str(bet) + ".")
      return -bet
	
  





#Call your game of chance functions here
coin_toss(500, guess = "Tails")