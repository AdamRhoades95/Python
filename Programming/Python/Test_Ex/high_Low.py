import random

game = True
round = True
q = 0
g = 0
while(game == True):
	q = random.randint(1,1000)
	while (round == True):
		g = int(raw_input("enter a guess: "))
		if(g > q):
			print("To High")
		elif(g < q):
			print("To Low")
		else:
			round = False
			print(g)
	more = raw_input("do you want to play again (y|n)")
	if (more.lower() == "n"):
		game = False
	else:
		round = True
			
print("out loop")
