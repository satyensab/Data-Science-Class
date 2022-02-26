# Classes - Employee Class
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/25/2022, DSCI 1302

class Employee:
  def __int__(self):
    pass

  def __str__(self):
    return "Name: " + self.name + ", Year of Joining: " + str(self.year) + ", Salary: " + str(self.salary) + ", Address: " + str(self.address)

  def getInfo(self,name,year,address,salary,hours,):
    self.salary = salary
    self.hours = hours
    self.name = name
    self.year = year
    self.address = address

  def AddSal(self):
    if self.salary < 500:
      self.salary+=10

  def AddWork(self):
    if self.hours > 6:
      self.salary+=5


employee1 = Employee()
employee1.getInfo("Bob","2011","Langdale Drive",100,8)
print(employee1)
employee1.AddSal()
employee1.AddWork()
print(employee1)

print()
employee2 = Employee()
employee2.getInfo("Mark","2015","Sparks Hall",500,6)
print(employee2)
employee2.AddSal()
employee2.AddWork()
print(employee2)

