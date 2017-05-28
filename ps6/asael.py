class player(object):
  """ Encapsulates a player, age, and goals. """
  # this creates a function 
  def __init__(self, player, age, goals):
    self.player = player
    self.age = age
    self.goals = goals
    # this returns the summary 
  def GetplayerSummary(self):
    summary = "Player: " + self.player + "\n"
    summary = summary + "Age: " + self.age + "\n"
    summary = summary + "Goals: " + self.goals + "\n"
    return summary
   # this makes a variable that gives the goals of the players  
  def getGoals(self):
    return self.goals
   
playerr = []
keepRunning = True
# This prints on the screen to give the person a choice of what to do 
while keepRunning:
  print("What do you want to do? Enter the # of your choice and press Enter.")
  print("(1) Add a player")
  print("(2) Print all players")
  print("(3) Print average number of goals for all players")
  print("(0) Leave the program and delete all players")
  response = input()
  # if they enter 0 then they will exit the program 
  if response == 0:
    keepRunning = False
  # if they enter 1 they can add in a player
  elif response == 1:
    print("Enter your player and press enter")
    name = raw_input()
    print("Enter age of the player")
    age = raw_input()
    print("How many goals have they sccored this season")
    goals = raw_input()
    somebody = player(name, age, goals)
    somebody = playerr.append(somebody)
    # if they enter 2 then they can access the player information 
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