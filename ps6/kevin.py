class Player(object):

  def __init__(self, name, age, goals):
    self.name = name
    self.age = int(age)
    self.goals = int(goals) 
    
    
  def getPlayerSummary(self):
    summary = "Player Name: " + self.name + "\n"
    summary = summary + "Player Age: " + str(self.age) + "\n"
    summary = summary + "Goals Scored: " + str(self.goals) 
    return summary
    

#Execution starts here 
myPlayers = []


keepRunning = True 

#While Loop Starts
while keepRunning: 

  print("(1) Add a player.")
  print("(2) Print all players.")
  print("(0) Leave the program and delete all players.")
  #variable for user input
  response = input()
  if response == 0:
    keepRunning = False
  #options for adding a player to the list
  elif response == 1:
    print("Enter name:")
    nombre = raw_input()
    print("Enter age:")
    edad = raw_input()
    print("Enter number of goals scored this season")
    goals = raw_input() 
    
    addedPlayer =  Player(nombre, edad, goals)
    myPlayers.append(addedPlayer)
    print("Ok, got it! Check again to see player added")
  #prints all the players summaries  
  elif response == 2:
    
    for jugadores in myPlayers:
      print(jugadores.getPlayerSummary())  