class soccerTeam(object):
  
  def __init__(self, name, age, goals): 
    self.name = name 
    self.age =age 
    self.goals = goals 
    
  def getStats(self):
    summary = "Name: " + self.name + "\n" 
    summary = summary + "Age: " + self.age + "\n"
    summary = summary + "Goals: " + self.goals + "\n" 
    return summary 
    
team = []

tom2 = True 

while tom2:
  print("What would you like to do? Enter your choice: ")
  print("(1) Add a player") 
  print("(2) Print all players") 
  print("(0) Leave the program and delete all players. ") 
  
  choice = input()
  
  if choice == "0":
    tom2 = False 
    
  elif choice == "1":
    print("Enter player name ")
    playerName = input()
    print("Enter age ")
    playerAge = input()
    print("Enter number of goals scored this season ")
    playerGoals = input()
    
    userPlayer = soccerTeam(playerName, playerAge, playerGoals)
    
    team.append(userPlayer) 
    print("Okay, player entered!")
     
  elif choice == "2":
    for m in team:
      print(m.getStats())

    
