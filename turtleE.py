

import turtle


screen = turtle.Screen()

screen.bgcolor("black")

screen.title("ColourINI Loopi ArtworkBANA")




artist = turtle.Turtle()

artist.speed("fastest")

artist.hideturtle()

artist.pensize(2)



def draw_petal(size, colour):

    artist.color(colour)

    artist.begin_fill()


    for _ in range(2):

        artist.circle(size, 60)

        artist.left(120)


    artist.end_fill()



colourss = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta"]

for i in range(72):

    draw_petal(90, colourss[i % len(colourss)])

    artist.right(5)




artist.penup()

artist.goto(0, -50)

artist.pendown()


artist.color("white")

artist.begin_fill()

artist.circle(25)

artist.end_fill()




turtle.done()