class Player(object):
  def __init__(self, name, age, goals):
	self.name = name
	self.age = age 
	self.goals = goals 
  def getStats(self):
	summary = "The players name is " + self.name + "." + "\n"
	summary = summary + "The players age is " + str(self.age) + "." + "\n"
	summary = summary + "The players final goals are " + str(self.goals) + "."
	return summary 

players = []
# x.getStats()
keepRunning = True 
while keepRunning:
	print("(0) To add a player:")
	print("(1) To see the players stats:")
	print("(2) To exit and delete information:")
	y = raw_input()
	if y == "0":
		print("What is the name of the player?") 
		playerName = raw_input()
		print("What is the age of the player?")
		playerAge = raw_input()
		print("How many goals did this player get?")
		playerGoals = raw_input()
		myPlayer = Player(playerName, playerAge, playerGoals)
		players.append(myPlayer)
	elif y == "1":	
		for p in players:
			print(p.getStats())
	elif y == "2":
		keepRunning = False		
