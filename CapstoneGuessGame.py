import random
guess_number = int(input("Enter the Guess Number"))
true_number = random.randint(1,100)
while True:
  if guess_number == true_number:
    print("Correct")
    break
  elif guess_number < true_number:
    print ("Low Guess Try Again ")
    guess_number = int(input("Enter Again"))
  elif guess_number > true_number:
    print ("Higher Number Try Again")
    guess_number = int(input("Enter Again"))
