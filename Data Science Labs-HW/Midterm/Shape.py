# Classes - Shape Class
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/25/2022, DSCI 1302
import math

class Shape:
  def __init__(self):
    pass
    
  def Area(self):
    pass

class Triangle(Shape):
  def __init__(self,a,b,angle_c):
    self.a = a
    self.b = b
    self.angle_c = angle_c

  def Area(self):
    self.angle_c = math.radians(self.angle_c)
    area = (self.a*self.b* math.sin(self.angle_c))/2
    print("Area of Triangle: " +str(round(area,2)))

  def Perimeter(self):
    c = math.sqrt(self.a**2+self.b**2 - (2*self.a*self.b*math.cos(self.angle_c)))
    perimeter = self.a + self.b + c
    print("Perimeter of Triangle: " + str(round(perimeter,2)))
    
class Rectangle(Shape):
  def __init__(self,height,width):
    self.width = height
    self.height = width

  def Area(self):
    area = self.height * self.width
    print("Area of rectangle: " + str(area))

  def Perimeter(self):
    perimeter = 2*(self.height + self.width)
    print("Perimeter of Rectangle: " + str(perimeter))
  

obj1 = Triangle(3,4,60)
obj1.Area()
obj1.Perimeter()

print()
obj2 = Rectangle(5,10)
obj2.Area()
obj2.Perimeter()

