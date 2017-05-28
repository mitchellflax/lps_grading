# This following class defines Team
class Team(object):
  """Encapulates a name, age, and goals."""
  def __init__(self,name,age,goals):
    self.name = name
    self.age = age
    self.goals = goals

#The next following lines define the printStats function
  def getStats(self):
    print("Name:" + self.name)
    print("Age:" + self.age)
    print("Goals:" + self.goals)


# In the following line I crated an empty list for the players called myPlayers
myPlayers = []
players = True

# In the next following lines I ask the user what they would like to view, and to enter in the number of what they choose to do
print("Welcome to TeamManager.py, if you would like to add a player, to the soccer team, enter 1. If you would like to view a player enter 2. If you would like to exit the program enter 0.")
answer = raw_input()

# The next line of code is for when the user wants to exit the program, because it won't print anything, it'll exit
while answer != "0":

# The next following lines of code are for when the user enters 1, and they have to enter the name, age, and the number of goals that the player has. After it will ask them what their next steps will be
  if answer == "1":
    print("We need the following information about your player:")
    print("Name:")
    name = raw_input()
    print("Age:")
    age = raw_input()
    print("Goals:")
    goals = raw_input()
    myPlayers.append(Team(name,age,goals))
    print("Okay, your new player has been added to the team. Do you want to add a player? If so enter 1. Or do you want view the players? If so enter 2. Or do you want to exit the program? If so enter 0")
    answer = raw_input()
    
    
# The next following lines of code are for when the  user chooses to enter 2 and it will allow them to see the stats and then ask them once again what they would like to do afterwards
  elif answer == "2":
    print("Current stats:")
    for info in myPlayers:
     info.getStats()
    print("Okay, you're done. Do you want to add another player? If so enter 1. Or do you want view all the players? If so enter 2. Or do you want to exit the program? If so enter 0")
    answer = raw_input()
