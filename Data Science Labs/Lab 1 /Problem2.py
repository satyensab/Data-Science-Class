# Question 2
# Name:Satyen Sabnis, satyen.sabnis@gmail.com, 1/12/2022, DSCI 1302
def string_to_list(user_string):
  user_string = list(map(int,user_string.split(",")))
  print(user_string)


user_string = input("Enter numbers seperated by a comma: ")
string_to_list(user_string)

