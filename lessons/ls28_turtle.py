from turtle import Turtle

em: Turtle = Turtle()
i: int = 0
while i < 100:
    em.forward(i * 2)
    em.left(90)
    i += 1

done()