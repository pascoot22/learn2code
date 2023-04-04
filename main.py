class Car:
  model = ""
  color = ""
  year = 0
  plate = ""

  def repaintBlue(self):
    self.color = "Blue"

  def printAttributes(self):
    print("Year: " + str(self.year) + ", Model: " + self.model)

def older(car1, car2):
  if car1.year > car2.year:
    return car2.year
  else:
    return car1.year

car1 = Car()
car2 = Car()

car1.model = "Tesla"
car1.color = "Red"
car1.year = 2018
car1.plate = "77WIN"

car2.model = "Mustang"
car2.color = "Black"
car2.year = 1980
car2.plate = "12YWO90"

car1.printAttributes()
car2.printAttributes()

def printAttributes2(car):
  print("Year: " + str(car.year) + ", Model: " + car.model)

printAttributes2(car1)
printAttributes2(car2)
  