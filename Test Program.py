from displayObject import displayObject
x = 0
y = 0
inputInt = 1
inputString = ""
f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]
pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

print("Hello! Welcome to the displayObject test program!")
while inputInt != 0:
	print("Please make a selection below!")
	print("0: Quit")
	print("1: Display fighter ship")
	print("2: Display Pac-man")
	inputString =input("Make a selection now! ")
	inputInt =int(inputString)
	if inputInt == 0:
		print("Thanks for testing!")
		break
	x =input("What would you like the x coordinate of the object to be? ")
	y =input("What would you like the y coordinate of the object to be? ")
	if inputInt == 1:
		displayObject(f1,x,y)
		print("Here's a fighter jet! \n")
	elif inputInt == 2:
		displayObject(pm,x,y)
		print("Here comes Pacman! \n")
	else:
		print("Invalid input! \n")
