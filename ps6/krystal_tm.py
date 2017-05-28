# teamManager.py

# this will call the objects within the player class
class Player(object):
        """ Encapsulates a player's name, age and number of goals. """

        def __init__(self, name, age, goals):
                self.name = name
                self.age = age
                self.goals = goals

# returns a string w player summary and stats
        def getStats(self):
                print("Player: " + self.name)
                print("Age: " + str(self.age))
                print("Goals: " + str(self.goals))


# empty list for users to fill up 
myPlayers = []

# defines variable choice and sets to one - will change in loop 
choice = 1

# creates a loop for the user to use
while choice != "0":
        # allows user to decide 
        print("Enter the number of your choice:")
        print("(1) Create new player")
        print("(2) List the player")
        print("(3) Leave and delete all players")
        choice = raw_input()

  # if user decides 1, able to input their own information for players
        if choice == "1":
                print("Player name?:")
                playerName = raw_input()
                print("Player age?:")
                playerAge = raw_input()
                print("Enter the amount of goals made:")
                playerGoals = raw_input()

                # allows data to be put into the empty list
                myPlayers.append(Player(playerName, playerAge, playerGoals))
                
                # if the user decides 2, all inputted information will show
        elif choice == "2":
                for k in myPlayers:
                        print(" ")
                        k.getStats()
                        print(" ")

        # if chosen 3, message will show
        if choice == "3":
                print("Thank you for the information!")

