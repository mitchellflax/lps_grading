# It will call the object and have the classes below
class Players(object): 
  """ Encapsulates the name, age and goals. """

  # The function, __init__ will call and define the classes below to self
  def __init__(self, name, age, goals):
    self.name = name
    self.age = age
    self.goals = goals

  # This function will give us the summary back of the person name they entered, age and number of goals   
  def getStats(self):
    summary = 'Name: ' + self.name + '\n'
    summary = summary + 'Age: ' + str(self.age) + '\n'
    summary = summary + 'Goals: ' + str(self.goals) + '\n'
    return summary




# This is an empty list because the user needs to make their own list of their players and keep it stored when print    
myPlayers = []
    
# When the program is true, it will run and print out the options   
program = True
while program == True:
	print('What would you like to do? Enter your choice.')
	print('(1) Add players')
	print('(2) Print all players')
	print('(0) Exit and delete the info')
      	
        # This way you can input the choice you want
      	choice = raw_input()

        # If you input 0, the program will stop running,  exit you out & delete the info you entered. 
	if choice == '0':
		program = False 
        # If you input 1, the program will ask you input a name, age and goals
	if choice == '1':
		print('Enter their name: ')
       	 	playerName = raw_input()
       	 	print('Enter their age: ')
       	 	playerAge = raw_input()
       	 	print('Enter their number of goals: ')
       	 	playerGoals = raw_input()
        
		myPlayers.append(Players(playerName, playerAge, playerGoals))

        # If you input 2, the program will print the player(s) that you've entered with their name, age & goals
	if choice == '2':
        
		for p in myPlayers:
		 	print(p.getStats())
      


