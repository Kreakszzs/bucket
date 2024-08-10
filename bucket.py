import turtle 
import pygame

li = turtle.Turtle()
li.screen.bgcolor("black")
li.pensize(2)
li.color("green")
li.left(90)
li.backward(60)
li.speed(50000)
li.shape("turtle")

#music
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

#gambar bunga
def love(i):
    if i<10:
        return
    else:
        li.forward(i)
        li.color("red")
        li.circle(2)
        li.color("green")
        li.left(30)

        love(3*i/4)

        li.right(60)

        love(3*i/4)

        li.left(30)
        li.backward(i)
        play_music("Do you think i have forgotten to you_.mp3")
love(60)
turtle.done()
pygame.mixer.music.stop()