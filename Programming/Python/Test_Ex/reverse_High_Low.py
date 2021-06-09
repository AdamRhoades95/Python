import random

game = True
round = True
q = 0
g = 500
gn = 250
holder = 0
while(game == True):
	q = int(raw_input("enter the number: "))
	while (round == True):
		holder = g
		if(q == g):
                        print("Corect, You guessed "+ str(g))
			round = False
		elif(int(g) > q):
                        print(g, "To High", gn)
			g -= gn
			if (holder-g > gn):
                                gn = (g-holder)/2
		elif(g < q):
                        print(g, "To Low", gn)
			g += gn
			if (g-holder > 1):
                                gn = (g-holder)/2
	more = raw_input("do you want to play again (y|n)")
	if (more.lower() == "n"):
		game = False
	else:
		round = True
		g = 500
                gn = 250
                holder = 0
			
print("out loop")
