print('''-+-+-+-+-+ coded by -+-+-+-+-+-+-
	          _                               
 ___ _   _  __| | ___  ___ _   _ _ __ __ _ ____
/ __| | | |/ _` |/ _ \/ __| | | | '__/ _` |_  /
\__ | |_| | (_| | (_) \__ | |_| | | | (_| |/ / 
|___/\__,_|\__,_|\___/|___/\__,_|_|  \__,_/___|
 ''')

yes=input("Hey! do you wann paly with lists?\nJust hit Y for yes and N for no: ")
for i in yes :
	if i == "Y":
				b = []
				for x in range(5):
								b.append(input("enter something: "))	
								print("your latest list is :",b)
				y=input("do you wann remove any element from list? : ")				
				if y == "n":
							print("well done! Your list is ready.")
							print("your latest list is :",b)
							pass
				elif y=="y":
							r = int((input("how many elements you wann remove: ")))
							for x in range(r):
											b.remove(input("enter the word you want to remove: "))
											print("your latest list is :",b)
				else:
					print("wronge argument! please enter y or n!")
					y = input(" do you want to remove any element from list ,enter y/n: ")
					print("your latest list is :",b)

	elif i=="N":
				print("its okay dude! i know you're tired off, but hey did you follow @sudosuraz on instagram? \nIf didn't just visit https://instagram.com/sudosuraz to follow an amezing hacker!")
	
	elif i != "Y":
				yes=input("Y for yes and N for no: ")
	elif i != "N":
				yes=input(" hit Y for yes and N for no: ")






