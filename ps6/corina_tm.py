class Player (object):
        def __init__(self, name, age, goals):
                self.name = name
                self.age = age
                self.goals = goals
        def getStats(self):
                summary = "Name: " + self.name + '\n'
                summary = summary + "Age: " + str(self.age) + '\n'
                summary = summary + "Goals: " + str(self.goals)
                return summary
myPlayers = []
x = True
while x == True:
        print("What do you want to do?")
        print('(1)Add Player')
        print('(2)Print Players')
        y = int(input())
        if y ==  1:
                print('Enter a Name')
                user_enteredname = input()
                print('Enter Age')
                user_enteredage = input()
                print('Enter number of goals')
                user_enteredgoals = input()
                myPlayer = Player(user_enteredname, user_enteredage, user_enteredgoals)
                myPlayers.append(myPlayer)
        elif y == 2:
                for l in myPlayers:
                        print(l.getStats())
