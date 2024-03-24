from turtle import *
if __name__=="__main__":
    shape("turtle")
    #title("gjddfghfhhdfgfyd")
    begin_fill()
    for i in range(3):
        for i in range(4):
            fd(100)
            rt(90)
        rt(15)
    end_fill()
    print(pos())
    exitonclick()