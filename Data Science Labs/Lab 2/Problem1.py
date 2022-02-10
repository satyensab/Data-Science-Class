# Question 1
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/3/2022, DSCI 1302
import numpy as np 

class Game:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.boardArray = np.random.randn(row,col)
    self.bomb_row = random.randint(0,row-1)
    self.bomb_col = random.randint(0,col-1)

  
  def __str__(self):
    return str(self.boardArray)

  def play(self):
    row = int(input("Which row?\n")) - 1
    col = int(input("Which column?\n")) - 1 
    if row > self.row-1 or user_col > self.col-1 or user_row <  0 or col <0:
      print("Dimensions out of bounds. Try again!")
      if self.boardArray[row][col] < 0:
        print("BOMB DETECTED!!!!")
        print(self)
      else:
        proceed = input("\nDo you want to continue? Y/N ")
        if proceed.lower() == 'y':
          self.play()
      else:
        print("hey goodbye, whatever")
        print(self)


rows = int(input("How many rows?\n"))
cols = int(input("How many columns?\n"))
x = Game(rows,cols)
x.play()