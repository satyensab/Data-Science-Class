
import random
import numpy

class Game:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.bomb_row = random.randint(0,row-1)
    self.bomb_col = random.randint(0,col-1)
    b = [['_'] * col for i in range(row)]
    self.board = numpy.array(b)

    print("Welcome to walmart minesweeper!")
 
    for i in range(row):
      for j in range(col):
        print(self.board[i][j], end = " ")
      print("\n")

    
  def print_board(self):
    for i in range(self.row):
      for j in range(self.col):
        print(self.board[i][j], end = " ")
      print("\n")

  def update_board(self,row,col,outcome):
    if outcome == "loss":
      self.board[row][col] = 'x'
    if outcome == "win":
      self.board[row][col] = '*'

  def play(self):
    number_of_tries = 0
    continue_game = True
    while(continue_game == True):
      user_row = int(input("Enter what row you think the bomb is located: "))
      user_col = int(input("Enter what column you think the bomb is located: "))
      user_row-=1
      user_col-=1
      if user_row > self.row-1 or user_col > self.col-1 or user_row <  0 or user_col <0:
        print("Dimensions out of bounds. Try again!")
        
      else:
        if (user_row == self.bomb_row and user_col == self.bomb_col):
          number_of_tries+=1
          Game.update_board(user_row,user_col,"win")
          Game.print_board()
          print("You found the bomb! You won!")
          continue_game = False
          print("It took you " + str(number_of_tries) + " number of tries" + " to finish the game!")
          if number_of_tries > (self.row * self.col)/2 :
            print("You should probably quit the game you suck!")
          else:
            print("your actually cracked at the game. you should go pro!")
        else:
          number_of_tries+=1
          print("You did not find the bomb. Try again!")
          Game.update_board(user_row,user_col,"loss")
          Game.print_board()
          print("Number of tries: " + str(number_of_tries))
          if (number_of_tries == (self.row * self.col) - 1):
            print("ya man you lost. you really just wasted your time")
            print("It really took you " + str(number_of_tries) + " to try to find the bomb and yet you still didnt find it. ")
            continue_game = False


Game = Game(random.randint(3,6),random.randint(3,5))
Game.play()
