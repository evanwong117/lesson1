class BMW():
    def country(self):
        print("BMW is a car manufacturer from Munich, Germany.")
    def establishment(self):
            print("BMW was founded in 1916. ")
class Ferrari():
    def country(self):
        print("Ferrari is a car manufacturer from Maranello, Italy.")
    def establishment(self):
            print("Ferrari was founded in 1939. ")
obj_bmw = BMW()
obj_ferrari = Ferrari()
for car in (obj_bmw, obj_ferrari):
      car.country()
      car.establishment()
