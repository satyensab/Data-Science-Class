import numpy as np

class GradeStatistics:
  def __init__(self, user_numpy):
    self.user_numpy = user_numpy

  def __str__(self):
    return "\nStudent gradebook:\n " + str(self.user_numpy)

  def mean(self):
    print()
    n = 1
    for grade in self.user_numpy:
      print("Mean - Assignment " + str(n) + ": " + str(round((np.mean(grade)),2)))
      n+=1
    print("\nMean of all Assignments: " + str(round((np.mean(self.user_numpy)),2)))
  
  def median(self):
    print()
    n = 1
    for grade in self.user_numpy:
      print("Median - Assignment " + str(n) + ": " + str(round((np.median(grade)),2)))
      n+=1
    print("\nMedian of all Assignments: " + str(round((np.median(self.user_numpy)),2)))

  def mode(self):
    pass
  
  def standard_dev(self):
    print()
    n = 1
    for grade in self.user_numpy:
      print("Standard dev. - Assignment " + str(n) + ": " + str(round((np.std(grade)),2)))
      n+=1
    print("\nStandard dev. of all Assignments: " + str(round((np.std(self.user_numpy)),2)))
  
  def variance(self):
    print()
    n = 1
    for grade in self.user_numpy:
      print("Variance - Assignment " + str(n) + ": " + str(round((np.var(grade)),2)))
      n+=1
    print("\nVariance of all Assignments: " + str(round((np.var(self.user_numpy)),2)))



count_students = int(input("How many students are in your class: "))
count_assig = int(input("How many assignements did you have?: "))
input_array = np.random.uniform(1,100,(count_assig,count_students))
input_array = np.round(input_array,1)

student_class = GradeStatistics(input_array)
print(student_class)

student_class.mean()
student_class.median()
student_class.mode()
student_class.standard_dev()
student_class.variance()



