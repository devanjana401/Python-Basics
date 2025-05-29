class Home:
    def __init__(self):
        pass
    def room1(self):
        width = 100
        breadth = 100
        print('Area of Room1:', width * breadth)
    def room2(self):
        width = 120
        breadth = 110
        print('Area of Room2:', width * breadth)
    def kitchen(self):
        width = 1222
        breadth = 4888
        print('Area of Kitchen:', width * breadth)
    def bathroom(self):
        width = 60
        breadth = 50
        print('Area of Bathroom:', width * breadth)
    def living_room(self):
        width = 200
        breadth = 150
        print('Area of Living Room:', width * breadth)
class FirstHome(Home):
    def study_room(self):
        width = 90
        breadth = 80
        print('Area of Study Room:', width * breadth)
class SecondHome(Home):
    def work_area(self):
        width = 100
        breadth = 70
        print('Area of Work Area:', width * breadth)
print("First Home Plan:")
first = FirstHome()
first.room1()
first.room2()
first.kitchen()
first.bathroom()
first.living_room()
first.study_room()
print("Second Home Plan:")
second = SecondHome()
second.room1()
second.room2()
second.kitchen()
second.bathroom()
second.living_room()
second.work_area()
