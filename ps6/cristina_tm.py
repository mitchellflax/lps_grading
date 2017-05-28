class player(object):
  """ Encapsulates a player, age, and goals. """
  # this creates a function with the information i need
  def __init__(self, player, age, goals):
    self.player = player
    self.age = age
    self.goals = goals
    # this function returns all of the information together
  def GetplayerSummary(self):
    summary = "Player: " + self.player + "\n"
    summary = summary + "Age: " + self.age + "\n"
    summary = summary + "Goals: " + self.goals + "\n"
    return summary
   # this makes a variable that gives the goals of the players  
  def getGoals(self):
    return self.goals
    # this creates a list and a boolean
playerr = []
keepRunning = True
# This prints out and the person inputs what they want
while keepRunning:
  print("What players do you want? Enter the # of your choice and press Enter.")
  print("(1) Add a player")
  print("(2) Print all players")
  print("(3) Print average number of goals for all players")
  print("(0) Leave the program and delete all players")
  response = input()
  # if they enter 0 the function will not run
  if response == 0:
    keepRunning = False
  # if they enter 1 they can add in a player and their information
  elif response == 1:
    print("Enter your player and press enter")
    name = raw_input()
    print("Enter age of the player")
    age = raw_input()
    print("How many goals have they sccored this season")
    goals = raw_input()
    somebody = player(name, age, goals)
    somebody = playerr.append(somebody)
    # if they enter 2 then they will get the players information
  elif response == 2:
    for p in playerr:
      print(p.GetplayerSummary()) 
      # this will give the players average amount of goals they have scored
  elif response == 3:
    count = 0
    ct = 0
    for t in playerr:
      count = count + int(t.getGoals())
      ct = ct + 1 
    print(count / ct)
      
  
  
    