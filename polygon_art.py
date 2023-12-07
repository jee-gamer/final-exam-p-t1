import turtle
import random

class Polygon:
    def __init__(self, art):
        self.reduction_ratio = 0.618
        self.art = art

    def draw_polygon(self, num_sides, size, orientation, location, color,
                     border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def draw_inside(self, num_sides, size, orientation, border_size):
        color = self.get_new_color()  # get new color for another one
        size *= self.reduction_ratio
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        turtle.penup()
        turtle.forward(size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.draw_polygon(num_sides, size, orientation, location, color,
                          border_size)

    def draw_inside2(self, num_sides, size, orientation, location, color,
                     border_size):
        turtle.penup()
        turtle.forward(size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= self.reduction_ratio
        self.draw_polygon(num_sides, size, orientation, location, color,
                          border_size)

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_many(self, side, number):
        for i in range(number):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            self.draw_polygon(side, size, orientation, location,
                              color, border_size)
            self.draw_inside(side, size, orientation, border_size)

    def draw_many2(self, side, number):
        for i in range(number):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            self.draw_polygon(side, size, orientation, location,
                              color, border_size)
            self.draw_inside2(side, size, orientation, location,
                              color, border_size)
            size *= self.reduction_ratio  # reduce size to draw smaller
            self.draw_inside2(side, size, orientation, location,
                              color, border_size)

    def draw_many_choice(self):
        if self.art == 1:
            self.draw_many(3, 30)
        elif self.art == 2:
            self.draw_many(4, 30)
        elif self.art == 3:
            self.draw_many(5, 30)
        elif self.art == 4:
            self.draw_many(3, 10)
            self.draw_many(4, 10)
            self.draw_many(5, 10)
        elif self.art == 5:
            self.draw_many2(3, 30)
        elif self.art == 6:
            self.draw_many2(4, 30)
        elif self.art == 7:
            self.draw_many2(5, 30)
        elif self.art == 8:
            self.draw_many2(3, 10)
            self.draw_many2(4, 10)
            self.draw_many2(5, 10)


num_sides = input("Which art do you want to generate? "
                  "Enter a number between 1 to 8,inclusive: ")
while True:
    try:
        num_sides = int(num_sides)
    except TypeError:
        raise TypeError

    if num_sides > 8 or num_sides < 1:
        print("You can only enter a number between 1 to 8,inclusive")
        num_sides = input("Which art do you want to generate? "
                          "Enter a number between 1 to 8,inclusive: ")
        continue
    break

turtle.speed(0)
turtle.bgcolor('white')
turtle.tracer(0)
turtle.colormode(255)
Draw = Polygon(num_sides)
Draw.draw_many_choice()
# hold the window; close it by clicking the window close 'x' mark
turtle.done()