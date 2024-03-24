import turtle
class Figure:
    def __init__(self):
        self.__position=[0, 0]
        self._visible=False
        self.__color="forest green"
    def set_position(self, x, y):
        self.__position=[x, y]
    def get_position(self):
        return self.__position
    def is_visible(self):
        return self._visible

    def set_color(self, clr):
        self.__color = clr

    def draw(self):
        turtle.up()
        turtle.goto(*self.__position)
        turtle.down()
    def show(self):
        if not self.is_visible():
            turtle.pencolor(self.__color)
            self.draw()

    def hide(self):
        if self.is_visible():
            turtle.pencolor(turtle.bgcolor())
            self.draw()
class Triangle(Figure):
    def draw(self):
        side_len=50
        turtle.up()
        turtle.goto(*self.get_position())
        turtle.down()
        turtle.setheading(0)
        turtle.forward(side_len)
        turtle.setheading(120)
        turtle.forward(side_len)
        turtle.setheading(240)
        turtle.forward(side_len)
class Circle(Figure):
    def draw(self):
        super().draw()
        turtle.circle(50)

if __name__=="__main__":
    print("Hello, world!")
    obj=Figure()
    obj.draw()
    obj1=Triangle()
    obj1.draw()