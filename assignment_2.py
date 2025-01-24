class Vehicle:
   def move(self):
       pass

class Car(Vehicle):
   def move(self):
       return "Driving on the road "

class Plane(Vehicle):
   def move(self):
       return "Flying through the sky "

class Boat(Vehicle):
   def move(self):
       return "Sailing across water "

# example
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
   print(vehicle.move())