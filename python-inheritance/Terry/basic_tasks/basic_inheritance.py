class Vehicle:
  def __init__(self, drive_type):
    self.drive_type = drive_type

  def drive(self):
    print(self.drive_type)



class Car(Vehicle):
  def drive(self):
    print(self.drive_type)

class Motorcycle(Vehicle):
  def drive(self):
    print(self.drive_type)

class Truck(Vehicle):
  def drive(self):
    print(self.drive_type)



volvo = Car('four-wheel drive Car')
volvo.drive()

ducati = Motorcycle('rear-wheel drive Motorcycle')
ducati.drive()

mercedes = Truck('six-wheel drive Truck')
mercedes.drive()