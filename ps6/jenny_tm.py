#this creates a class named Player
class Player(object):
#this creates a function called __init__ and it has the parameters self, player, age, and goals and you set the 1,2,and 3rd parameters to self
	def __init__(self, player, age, goals):
		self.player = player
		self.age = age 
		self.goals = goals
#the getStats fucntion stores the information of the player like their name, age, and goals 
	def getStats(self):
		summary = "Player: " + self.player + "\n"
		summary = summary + "Age: " + self.age + "\n" 
		summary = summary + "Goals: " + self.goals + "\n"
		return summary
#the getGoals function returns the goals the player has score
	def getGoals(self):
		return self.goals

#myPlayers is an empty list that the user can add players later on
myPlayers = [] 
#used to create a while statement later on
sport = "soccer" 

#the while statement is used so that the user can see the options they can choose
while sport == "soccer":
 	print("What would you like to do? Enter the number of your choice and press enter.")
        print("(0) Leave the program and delete the players")
        print("(1) Add a player")
	print("(2) Print all players")
	print("(3) Print average number of goals for all payers")
  
#response is equal to raw_input to let the user decide what option they want to choose 
	response = int(raw_input())
#if the user chooses 1 it will ask the the player's info  
	if response == 0:
		sport == "sitting"
	if response == 1:
		print("Enter your player's name and press enter")
		playerName = raw_input()
		print("Enter age of the player")
		playerAge = raw_input()
		print("How many goals have they scored this season?")
		playerGoals = raw_input()
		my_Player = Player(playerName, playerAge, playerGoals)
		myPlayers.append(my_Player)
		print("Player now added to the team!")
#this will run if the user chooses choice 2 and it will display the players by using the getStats method
	elif response == 2:
		print("Here's a list of the players")
		for p in myPlayers:
			print(p.getStats())
#this will print if the user chooses choice 3 and it will print the average number of goals each player made 	
	elif response == 3:
		count = 1 
		number = 1
		for l in myPlayers:
			count = count + int(l.getGoals())
			number = number + 1
			print(count / number)
