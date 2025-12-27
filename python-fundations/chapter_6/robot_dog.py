class Robot:

    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] += x
        print('New position:', self.position)

    def eat(self):
        print("I'm hungry!")

class Robot_Dog(Robot):
    # The parent class we're inherating from goes in parentheses
    # If we leave out the __init__() method it will call the parent's __init__() method by default

    def make_noise(self):
        print('Woof Woof!')

    # Method overriding
    def eat(self):
        # If use super().eat() it will get the method from the parent class
        print("I like bacon!")

# Main program
my_robot_dog = Robot_Dog('Toddy')
my_robot_dog.eat()
my_robot_dog.walk(10)
my_robot_dog.make_noise()