# Question 1
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 1/12/2022, DSCI 1302

def divisor_user(user_number):
  divisor_list = []
  for i in range(1, user_number):
    if user_number%i == 0:
      divisor_list.append(i)
  print(*divisor_list,sep = ",")

user_number = int(input("Enter a number: "))
divisor_user(user_number)




