print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Ask for user's input
step_one = input('You\'re at a cross road. Where do you want? Type "Left" or "Right"\n').lower()
step_two = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
step_three = input('You arrive at the island unharmed. There is a house with 3 doors. Red, Yellow and Blue. Which colour do you choose?\n').lower()

#Nested if statements for possible outcome from user's input
if step_one == "left":
  if step_two == "wait":
    if step_three == "red":
      print("Burned by fire. Game Over")
    elif step_three == "blue":
      print("Eaten by beasts. Game Over")
    elif step_three == "yellow":
      print("You Win!")
    else:
      print("Game over.")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")
