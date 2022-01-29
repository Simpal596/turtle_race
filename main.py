from turtle import Turtle, Screen
from random import randint

my_screen = Screen()
my_screen.setup(width=500,height=400)

turtle_list = ["timmy", "tim", "tom", "tin", "jhonny", "jenny"]
color = ["red", "orange", "yellow", "green", "blue", "purple"]
i = 0
j= -150
for item in turtle_list :
    turtle_list[i] = Turtle(shape="turtle")
    turtle_list[i].penup()
    turtle_list[i].color(color[i])
    turtle_list[i].setpos(x=-230,y=j)
    i += 1
    j += 50

guess = (my_screen.textinput(title="BET TO WIN", prompt="guess the turtle color")).lower()
is_game_on = False

if guess :
    is_game_on = True

while is_game_on :
    for item in turtle_list :
        x_cor = item.xcor()
        if x_cor < 230 :
            random_number = randint(0, 10)
            item.setx(x_cor + random_number)
        elif x_cor >= 230 :
            color = item.pencolor()
            if color == guess :
                print(f"you win. {color} turtle win the race.")
                is_game_on = False
            else :
                print(f"you loose. {color} turtle win the race.")
                is_game_on = False


my_screen.exitonclick()
