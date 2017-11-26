import random


print("Computer has taken O So you will go with X")

board=[0,1,2,3,4,5,6,7,8]

def show():
	print(" "+str(board[0])+ " | " +str(board[1]) + " | " +str(board[2]))
	print("-----------")
	print(" "+str(board[3])+ " | " +str(board[4]) + " | " +str(board[5]))
	print("-----------")
	print(" "+str(board[6])+ " | " +str(board[7]) + " | " +str(board[8]))

def checkline(char,spot1,spot2,spot3):
	if(board[spot1]==char and board[spot2]==char and board[spot3]==char):
		return True
def checkall(char):
	if (checkline(char,0,1,2)):
		return True
	if (checkline(char,3,4,5)):
		return True	
	if (checkline(char,6,7,8)):
		return True

	if (checkline(char,0,3,6)):
		return True
	if (checkline(char,1,4,7)):
		return True	
	if (checkline(char,2,5,8)):
		return True

	if (checkline(char,0,4,8)):
		return True
	if (checkline(char,2,4,6)):
		return True		



show()	
while True:
	indicator=False
	turn=raw_input("Wherew you want to put..??? (0 to 8) ")
	turn=int(turn)
	
	if(turn<=8 and turn >= 0):
		if(board[turn] != 'X' and board[turn] != 'O'):
			board[turn]='X'
			show()

			#Check for winner
			if(checkall('X')==True):
				print ("--X have won the match--")
				break;

			
			
			while True:
				count=0
				for i in range(0,9):
					if(board[i]=='X' or board[i]=='O'):
						count=count+1

				if (count<9):		
					#print(count)		
					random.seed()
					pc=random.randint(0,8)
					print("Now Copmuters Turn..!!")
					
					if(board[pc] != 'X' and board[pc] != 'O'):
						
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print(" ")
						print("######################################")
						print("Computer has placed at "+ str(pc))
						board[pc]='O'
						show()


						#Check for winner
						if(checkall('O')==True):
							indicator=True


						break;
				else:
					print("Board is FULL...!!!!")
					break;		



		else:
			print("This location is filled...!!!")
	else:
		print("Chose location properly....!!!")	

	
	if(indicator==True):
		print("--O have won the match--")
		break;

	if (count==9):
		break;


print("--Game completed--")