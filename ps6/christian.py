class Player(object):
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	def getStats(self, name, age, goals):
		summary = "Name: " + self.name + "\n" + "Age: " + self.age + "\n" + "Goals: " + self.goals
		return summary



myPlayers = []

keepRunning = True
while keepRunning:
	print("What would you like to do?")
	print("(1)Add a Player")
	print("(2)Print Players")
	print("(0)End Code")
	answer = input()
	if answer == 1:
		print("What is their name?")
		name = raw_input()
		print("What is their age?")
		age = raw_input()
		print("How many goals do they have?")
		goals = raw_input()
		myPlayer = Player(name, age, goals)
		print("It has bee added")
		myPlayers.append(myPlayer)
	elif answer == 2:
		for p in myPlayers:
			print(p.getStats(name, age, goals))
	elif answer == 0:
		keepRunning = False
