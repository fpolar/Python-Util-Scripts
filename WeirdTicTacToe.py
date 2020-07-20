import copy
from PIL import Image
import numpy as np

class Board:
	def __init__(self, size):
		self.spaces = []
		for i in range(0,size*size):
			self.spaces.append(" ")
		self.turnNum = 0
		self.size = size

	def turn(self, move, row, col):
		self.spaces[self.size*row+col] = move
		self.turnNum+=1

	def gameover(self):
		out = (self.turnNum>=self.size*2-1)
		for i in range(0, self.size):
			for j in range(0, self.size):
				if

	def print(self, pixel_size):
		print(self.spaces)
		colorArray = []#[(ord(char), 0, 0) for char in self.spaces]
		for i in range(0, self.size):
			col = []
			for j in range(0, self.size):
				col.append([ord(self.spaces[self.size*i+j]), 0, 0])
			colorArray.append(col*pixel_size)
		x = np.array(colorArray*pixel_size)
		img = Image.fromarray(x, 'RGB')
		img.show()

class Player:
	def __init__(self, char, toeUsed):
		self.char = char
		self.toeUsed = toeUsed
		#toesUsed could be int going to 0 if multiple players and toes

def playBoard(board, p1, p2):
	if board.gameover:

	for i in range(0, board.size):
		for j in range(0, board.size):
			currBoard = copy.deepcopy(board)
			if board.turnNum & 1:
				if currBoard.spaces[board.size*i+j] == ' ':
					currBoard.turn(p1.char, i, j)
					playBoard(currBoard, p1, p2)
				elif not p1.toeUsed:
					currBoard.turn(p1.char, i, j)
					p1C = copy.deepcopy(p1)
					playBoard(currBoard, p1C, p2)
			else:
				if currBoard.spaces[board.size*i+j] == ' ':
					currBoard.turn(p2.char, i, j)
					playBoard(currBoard, p1, p2)
				elif not p2.toeUsed:
					currBoard.turn(p2.char, i, j)
					p2C = copy.deepcopy(p2)
					p
					playBoard(currBoard, p1, p2C)




player1 = Player('X', False)
player2 = Player('O', False)

board = Board(3)
allBoards = [[board]]
playBoard(board, player1, player2)
board.print(300)
# pixel_size = 30
# for
# np_im = np.random.rand()*255
# new_im = Image.fromarray(np_im)
# new_im.show()
