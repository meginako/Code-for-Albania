import turtle
import random
import time

turtle.bgcolor("white")




screen_width = 800
screen_height = 600
box_width = 800.0
box_height = 600.0
boundary_x = box_width / 2.0
boundary_y = box_height / 2.0
screen = turtle.Screen()
screen.title("Galaga")
screen.setup(width=1.0, height=1.0)
screen.bgpic("space2.gif")

screen.register_shape("playerdy.gif")
screen.register_shape("enemydy.gif")
screen.register_shape("hearts.gif")
screen.register_shape("bullet3.gif")
screen.register_shape("fireball.gif")




enemy_cooldown:float= 1.5
player = turtle.Turtle()
player.shape("playerdy.gif")
player.shapesize(55, 55)
player.color("white")
player.penup()
player.goto(-boundary_x / 2, -boundary_y)

player_last_shot: float = time.time()
player_cooldown:float = 3.0
player_height:float = 100.0
player_width:float =50.0

enemy_height:float =40.0
enemy_width:float =30

bullet_height:float = 50
bullet_width:float=30

def player_left_edge()->float:
	return player.xcor() - (player_width/2)
def player_right_edge()->float:
	return player.xcor() + (player_width/2)
def player_top_edge()->float:
	return player.ycor() + (player_height/2)
def player_bottom_edge()->float:
	return player.ycor() - (player_height/2)


def enemy_left_edge()->float:
	return enemy.xcor() - (enemy_width/2)
def enemy_right_edge()->float:
	return enemy.xcor() + (enemy_width/2)
def enemy_top_edge()->float:
	return enemy.ycor() + (enemy_height/2)
def enemy_bottom_edge()->float:
	return enemy.ycor() - (enemy_height/2)

def bullet_top_edge(bullet: turtle.Turtle)->float:
	return bullet.ycor() + (bullet_height/2)
def bullet_bottom_edge(bullet: turtle.Turtle)->float:
	return bullet.ycor() - (bullet_height/2)
def bullet_right_edge(bullet: turtle.Turtle)->float:
	return bullet.xcor() + (bullet_width/2)
def bullet_left_edge(bullet: turtle.Turtle)->float:
	return bullet.xcor() - (bullet_width/2)

box_drawer = turtle.Turtle()
box_drawer.penup()
box_drawer.speed(0)
box_drawer.goto(-boundary_x, -boundary_y)

for i in range(2):
    box_drawer.forward(box_width)
    box_drawer.left(90)
    box_drawer.forward(box_height)
    box_drawer.left(90)
box_drawer.hideturtle()

middle_drawer = turtle.Turtle()
middle_drawer.penup()
middle_drawer.speed(0)
middle_drawer.goto(-boundary_x, 0)
middle_drawer.setheading(0)
middle_drawer.forward(box_width)
middle_drawer.hideturtle()

player_left_bound = -boundary_x
player_right_bound = boundary_x

player_top_bound = 0
player_bottom_bound = -boundary_y
player_speed = 25


enemy_speed: float = 1
enemy_last_shot: float = time.time()
enemy_bullets: list[turtle.Turtle] = []
player_bullets: list[turtle.Turtle] = []

player_hearts: list[turtle.Turtle]=[]
enemy_hearts: list[turtle.Turtle]=[]
player_hearts_index:int = 2
enemy_hearts_index: int = 2

index = 10
for h in range(0, 3, 1):
    h=turtle.Turtle()
    h.shape("hearts.gif")
    screen.tracer(0)
    h.penup()
    h.goto(boundary_x-index,boundary_y-35)
    index=index+37
    enemy_hearts.append(h)
    screen.tracer(1)

index2 = 20
for h2 in range(3):
    h2=turtle.Turtle()
    screen.tracer(0)
    h2.penup()
    h2.goto(- boundary_x +index2,-boundary_y+35)
    h2.shape("hearts.gif")
    index2=index2+37
    player_hearts.append(h2)
    screen.tracer(1)


enemy = turtle.Turtle()
enemy.shape("enemydy.gif")
enemy.color("red")
enemy.penup()
enemy.goto(0, boundary_y - 40)


def move_left():
    x = player.xcor() - player_speed
    if x >= player_left_bound:
        player.goto(x, player.ycor())
def move_right():
    x = player.xcor() + player_speed
    if x <= player_right_bound:
        player.goto(x,player.ycor())
def move_up():
    y = player.ycor() + player_speed
    if y <= player_top_bound:
        player.goto(player.xcor(), y)
def move_down():
    y = player.ycor() - player_speed
    if y >= player_bottom_bound:
        player.goto(player.xcor(),y )

def move_enemy() -> None:
    if enemy.xcor() < player.xcor():
        enemy.goto(enemy.xcor() + enemy_speed, enemy.ycor())
    elif enemy.xcor() > player.xcor():
        enemy.goto(enemy.xcor() - enemy_speed, enemy.ycor())
    else:
        enemy.goto(enemy.xcor(), enemy.ycor())

def create_player_bullet() -> None:
        global player_last_shot
        if time.time() - player_last_shot > player_cooldown:

            screen.tracer(0)
            bullet2 = turtle.Turtle()
            bullet2.shape("bullet3.gif")
            bullet2.color("orange")
            bullet2.penup()
            bullet2.goto(player.xcor(), player.ycor())
            bullet2.setheading(90)
            player_bullets.append(bullet2)
            screen.tracer(1)
            player_last_shot = time.time()


def bullet_shooting_player() ->None:
    speed: float = 2.0

    for bullet2 in player_bullets:
        bullet2.forward(30)

def create_enemy_bullet() -> None:
    num = random.randint(0, 101)
    if num <= 40:
        screen.tracer(0)
        bullet = turtle.Turtle()
        bullet.shape("fireball.gif")
        bullet.color("orange")
        bullet.penup()
        bullet.goto(enemy.xcor(), enemy.ycor())
        bullet.setheading(-90)
        enemy_bullets.append(bullet)
        screen.tracer(1)

def collision_player():
    global player_hearts_index
    for bullet in enemy_bullets:
        if(
            player_left_edge()< bullet_right_edge(bullet) and
            player_right_edge() > bullet_left_edge(bullet) and
            player_bottom_edge()< bullet_top_edge(bullet) and
            player_top_edge()> bullet_bottom_edge(bullet) and
            bullet.isvisible()
        ):
            bullet.hideturtle()
            player_hearts[player_hearts_index].hideturtle()
            player_hearts_index=player_hearts_index - 1

def bullet_shooting() ->None:
    speed: float = 2.0
    i: int = 0
    while i < len(enemy_bullets):
        enemy_bullets[i].forward(30)
        if bullet_top_edge(enemy_bullets[i]) < -boundary_x:
            enemy_bullets[i].hideturtle()
            del enemy_bullets[i]
        else:
            i = i + 1

    i: int = 0
    while i < len(player_bullets):
        player_bullets[i].forward(30)
        if bullet_bottom_edge(player_bullets[i]) > boundary_x:
            player_bullets[i].hideturtle()
            del player_bullets[i]
        else:
            i = i + 1

screen.onkey(create_player_bullet, "space")

def collision_enemy():
    global enemy_hearts_index
    for bullet in player_bullets:
        if(
            enemy_left_edge()< bullet_right_edge(bullet) and
            enemy_right_edge() > bullet_left_edge(bullet) and
            enemy_bottom_edge()< bullet_top_edge(bullet) and
            enemy_top_edge()> bullet_bottom_edge(bullet) and
            bullet.isvisible()
        ):
            bullet.hideturtle()
            enemy_hearts[enemy_hearts_index].hideturtle()
            enemy_hearts_index=enemy_hearts_index - 1

def startGame() -> None:
    global enemy_last_shot

    lose: bool = False

    while True:
        move_enemy()
        if time.time() - enemy_last_shot > enemy_cooldown:
            create_enemy_bullet()
            enemy_last_shot = time.time()
        bullet_shooting()
        collision_player()
        collision_enemy()

        if player_hearts_index < 0:
            lose = True
            break
        elif enemy_hearts_index < 0:
            break

    writer: turtle.Turtle = turtle.Turtle()
    writer.hideturtle()
    writer.color("white")


    if lose == True:
        writer.write("You Lose!" , align="center" , font=("Arial", 50, "bold"))

    else:
        writer.write("You Win!", align="center" , font=("Arial", 50, "bold"))

screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

screen.onkey(startGame, "Return")



screen.listen()
screen.mainloop()