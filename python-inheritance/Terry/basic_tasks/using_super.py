class Vehicle:
  def __init__(self, drive_type):
    self.drive_type = drive_type

  def drive(self):
    print(self.drive_type)



class Car(Vehicle):
  def drive(self):
    print(self.drive_type, self.__class__)

class Motorcycle(Vehicle):
  def drive(self):
    print(self.drive_type, self.__class__)

class Truck(Vehicle):
  def __init__(self, drive_type, year):
    super().__init__(drive_type)
    self.year = year

  def drive(self):
    print(self.drive_type, self.year)



volvo = Car('four-wheel drive Car')
volvo.drive()

ducati = Motorcycle('rear-wheel drive Motorcycle')
ducati.drive()

mercedes = Truck('six-wheel drive Truck', 2020)
mercedes.drive()