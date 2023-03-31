import tkinter as tk
import turtle
import winsound
import random 

HEIGHT = 0
heightp = 0
WIDTH = 0
xcorp = 0
SPEED = 0
window_size = ()
score_a = 0
score_b = 0
window = tk.Tk()
SPEEDP = 0
title = ""

def difficultyScreen():
    global window
    window.title("Select Difficulty")
    window.geometry("800x400")
    
    # Define difficulty level options
    difficulty_options = ["Easy", "Medium", "Hard"]
    
    # Define tkinter widgets to display difficulty options and launch game
    tk.Label(window, text = "Select Difficulty:").pack(pady=10)
    for difficulty in difficulty_options:
        tk.Button(window, text=difficulty, command=lambda d=difficulty: launchGame(d)).pack()
    
    # Launch the tkinter window
    window.mainloop()

def launchGame(difficulty):
    global window_size, HEIGHT, WIDTH, SPEED, xcorp, window, SPEEDP, title
    if difficulty == "Easy":
        window_size = (600, 400)
        SPEED = 1/10
        SPEEDP = 20
        HEIGHT = 400
        WIDTH = 600
        xcorp = 280
        title = "Pong inspired by freeCodeCamp Easy Level"

    elif difficulty == "Medium":
        window_size = (800, 600)
        SPEED = 1/5
        HEIGHT = 600
        SPEEDP = 30
        xcorp = 350 #x coordinate of paddle
        WIDTH = 800
        title = "Pong inspired by freeCodeCamp Medium Level"

    else:
        window_size = (1000, 800)
        SPEED = 1
        HEIGHT = 800
        WIDTH = 1000
        xcorp = 430
        SPEEDP = 50
        title = "Pong inspired by freeCodeCamp Difficult Level"

    window.destroy()

difficultyScreen()
#Launc turtle screen with selected settings    
wn = turtle.Screen()
wn.title(title)
wn.bgcolor("black")
wn.setup(*window_size)
wn.tracer(0)#turn turtle animation on or off and set a delay for update drawings; tracer(n = None,delay = None)




#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("cyan")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1/2)
paddle_a.penup()
paddle_a.goto(-WIDTH/2 + 50, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("cyan")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1/2)
paddle_b.penup()
paddle_b.goto(WIDTH/2 - 50, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 0)
ball.dx = SPEED
ball.dy = -SPEED

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,HEIGHT/2 - 50)
pen.write(f"Player A: {score_a}\tPlayer B: {score_b}", align = "center", font = ('Courier', 20, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += SPEEDP
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= SPEEDP
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += SPEEDP
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= SPEEDP
    paddle_b.sety(y)
#Key
wn.listen()
wn.onkeypress(paddle_a_up, "w")#call method when the key pressed
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")#call methof when the key pressed
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    #the ball is moving
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > HEIGHT/2 - 10:
        ball.sety(HEIGHT/2 - 10)
        ball.dy *= -1

    if ball.ycor() < -HEIGHT/2 + 10:
        ball.sety(-HEIGHT/2 + 10)
        ball.dy *= -1

    if ball.xcor() < -WIDTH/2 + 20:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}\tPlayer B: {score_b}", align = "center", font = ('Courier', 20, "normal"))

    if ball.xcor() > WIDTH/2 - 20 :
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}\tPlayer B: {score_b}", align = "center", font = ('Courier', 20, "normal"))
        
    #Paddle with ball collide
    if (ball.xcor() > WIDTH/2 - 60 and ball.xcor() < WIDTH/2 - 50) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(WIDTH/2 - 60)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -WIDTH/2 + 60 and ball.xcor() > -WIDTH/2 + 50) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-WIDTH/2 + 60)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
