# This sets a class so that it can be used later in the code.
class Player(object):
  def __init__(self, name, age, goals):
    self.name = name
    self.age = age
    self.goals = goals
    # This makes it so that there can be a stats.
  def getPlayerSummary(self):
    Stats = "Player: " + self.name + "\n"
    Stats = Stats + "Age: " + self.age + "\n"
    Stats = Stats + "Goals: " + self.goals + "\n"
    return Stats

# Lets it so the program can add players.
players = []

run = True
# the user can use pick from any of the choices below.
while run:
  print("What would you like to do? Enter the number of your choice and press 'Enter'.")
  print('(1): Add players.')
  print('(2): View players information.')
  print('(0): Exit from teamManager.')
  
    # this is for the user to input their response.
  response = input()
  
  if response == "0":
    run = False
      #Due to their selection they will brought to a different option.
  elif response == "1":
    print('What is the name of the player?')
    playersName = input()
    print('What is the age of the player?')
    playersAge = input()
    print('How many goals have they made?')
    playersGoals = input()
    
    team = Player(playersName, playersAge, playersGoals)
    players.append(team)
    
    print('Okay! We go it, now it will appear in the list when you run it again.')
    
  elif response == "2":
    for p in players:
      print(p.getPlayerSummary())