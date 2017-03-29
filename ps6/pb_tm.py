class Player(object):
# objects are created for this class
  def __init__(self, name, age, goals): 
    self.name = name 
    self.age = age 
    self.goals = goals 
    
  def getStats(self):
    summary = "Name: " + self.name + "\n"
    summary = summary + "Age: " + self.age + "\n"
    summary = summary + "Goals: " + self.goals + "\n" 
    return summary 

#an empty list for the team players is made here
myPlayers = [] 

#a boolean is made here for the choices of the suer to choose from
Tom3 = True 
#this while loop is true and prints the options for the user 
while Tom3: 
  print("What would you like to do? Enter your choice and press 'enter'.")
  print("(1) Add a player")
  print("(2) Print all players")
  print("(0) Leave the program and delete all players")
  
  response = input()
# the while loop doesn't run if the user inputs 0, making the boolean 'false'  
  if response == "0": 
    Tom3 = False 

#if the user chooses option 1 the loop is ran for the user put in a player of their own which then adds the player to the empty list from above
  elif response == "1": 
    print("Enter name: ") 
    userPlayer = input() 
    print("Enter Age: ") 
    userAge = input() 
    print("Enter number of goals scored this season: ") 
    userGoals = input() 
    
    userPlaya = Player(userPlayer, userAge, userGoals)
    
    myPlayers.append(userPlaya) 
    print("Okay, player entered!") 
# if the user chooses this optin, then whatever players are in the list then their stats will be printed to the user     
  elif response == "2": 
    for m in myPlayers:
      print(m.getStats()) 
      