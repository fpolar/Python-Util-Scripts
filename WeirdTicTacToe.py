import copy
from PIL import Image
import numpy as np

class Board:
	def __init__(self):
		self.spaces = []
		for i in range(0,3*3):
			self.spaces.append(str(i))
		self.turnNum = 0

	def turn(self, move, row, col):
		self.spaces[3*row+col] = move
		self.turnNum+=1

	def gameover(self):
		out = (self.turnNum==9) and (self.turnNum>=5) 
		out = out and (self.spaces[0] == self.spaces[1] == self.spaces[2]) 
		out = out and (self.spaces[3] == self.spaces[4] == self.spaces[5]) 
		out = out and (self.spaces[6] == self.spaces[7] == self.spaces[8]) 
		out = out and (self.spaces[0] == self.spaces[3] == self.spaces[6]) 
		out = out and (self.spaces[1] == self.spaces[4] == self.spaces[7]) 
		out = out and (self.spaces[2] == self.spaces[6] == self.spaces[8]) 
		out = out and (self.spaces[6] == self.spaces[4] == self.spaces[2]) 
		out = out and (self.spaces[0] == self.spaces[4] == self.spaces[8])

	def print(self, pixel_size):
		# print(self.spaces*10)
		rgb = [[],[],[]]#[(ord(char), 0, 0) for char in self.spaces]
		for i in range(0, 3):
			for ps1 in range(0, pixel_size):
				for j in range(0, 3):
					color = []
					if self.spaces[3*i+j] == 'O':
						color = [0, 0, 255]
					elif self.spaces[3*i+j] == 'X':
						color = [255, 0, 0]
					else:
						color = [255, 255, 255]
					for a in range(0, 3):
						for ps2 in range(0, pixel_size):
							rgb[a].append(color[a])
		x = np.array(rgb)
		img = Image.fromarray(x, 'RGB')
		img.show()

class Player:
	def __init__(self, char, toeUsed):
		self.char = char
		self.toeUsed = toeUsed
		#toesUsed could be int going to 0 if multiple players and toes

def playBoard(board, p1, p2):
	if board.gameover:
		return
	for i in range(0, 3):
		for j in range(0, 3):
			currBoard = copy.deepcopy(board)
			if board.turnNum & 1:
				if currBoard.spaces[3*i+j] == ' ':
					currBoard.turn(p1.char, i, j)
					playBoard(currBoard, p1, p2)
				elif not p1.toeUsed:
					currBoard.turn(p1.char, i, j)
					p1C = copy.deepcopy(p1)
					playBoard(currBoard, p1C, p2)
			else:
				if currBoard.spaces[3*i+j] == ' ':
					currBoard.turn(p2.char, i, j)
					playBoard(currBoard, p1, p2)
				elif not p2.toeUsed:
					currBoard.turn(p2.char, i, j)
					p2C = copy.deepcopy(p2)
					p
					playBoard(currBoard, p1, p2C)




player1 = Player('X', False)
player2 = Player('O', False)

board = Board()
allBoards = [[board]]
playBoard(board, player1, player2)
board.print(10)
