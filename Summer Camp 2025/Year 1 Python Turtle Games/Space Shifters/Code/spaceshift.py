import turtle
import random
import time

screen: turtle.Screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("#964E4E")
screen.bgpic("background.gif")
#screen.register_shape("drone.gif")
#for big laser
screen.register_shape("drone.gif")
screen.register_shape("heart.gif")
screen.register_shape("meteorite.gif")
#for small laser
# screen.register_shape("")
# for meteorite
#screen.register_shape("")
# for background

hearts_row:list[turtle.Turtle]=[]
small_lasers: list[turtle.Turtle]= []
lasers: list[turtle.Turtle]=[]
small_laser_damage: float = 1
small_laser_width: float = 10
small_laser_length: float = 120


meteorites: list[turtle.Turtle]= []
def meteorite_spawn(y:float) -> list [turtle.Turtle]:
    x: float = 600
    screen.tracer(0)
    meteorite: turtle.Turtle = turtle.Turtle()
    meteorite.shape("meteorite.gif")    
    meteorite.shapesize(meteorite_length/20.0, meteorite_width/20.0)
    meteorite.penup()
    meteorite.goto(x, y)
    meteorites.append(meteorite)
    screen.tracer(1)
def make_small_laser_spawn(y:float) -> list [turtle.Turtle]:
    x: float = 600
    screen.tracer(0)
    small_laser: turtle.Turtle = turtle.Turtle()
    small_laser.shape("square")    
    small_laser.shapesize(small_laser_length/20.0, small_laser_width/20.0)
    small_laser.color("red")
    small_laser.penup()
    small_laser.goto(x, y)
    small_lasers.append(small_laser)
    screen.tracer(1)
    
def laser_spawn(y:float) -> list [turtle.Turtle]:
    x: float = 600
    screen.tracer(0)
    laser: turtle.Turtle = turtle.Turtle()
    laser.shape("square")    
    laser.shapesize(laser_length/20.0, laser_width/20.0)
    laser.color("orange")
    laser.penup()
    laser.goto(x, y)
    lasers.append(laser)
    screen.tracer(1)
    
#drone propertys
drone_width: float = 60.0
drone_length: float = 60.0
drone_speed: float = 8.0
drone_acceleration: float = -0.3
drone_velocity: float = 1



#box boundary
box_size: float = 650.0
boundary: float = box_size/2
screen.setup(box_size+50, box_size+50)



#drawing the box
box_drawer: turtle.Turtle = turtle.Turtle()
box_drawer.hideturtle()
box_drawer.penup()
box_drawer.speed(0)
box_drawer.goto(-boundary, -boundary)
box_drawer.pendown()
box_drawer.color("red")
box_drawer.width(10)
for i in range(4):
	box_drawer.forward(box_size)
	box_drawer.left(90)
box_drawer.hideturtle()

#drone movements
drone:turtle.Turtle = turtle.Turtle()
drone.shape("drone.gif")
drone.shapesize(5, 3)
drone.penup()
drone.goto(0,0)
def drone_top_edge() -> float:
    return drone.ycor() + (drone_width/2)
def drone_bottom_edge()-> float:
    return drone.ycor() - (drone_width/2)
def drone_left_edge() -> float:
    return drone.xcor() - (drone_length/2)
def drone_right_edge()-> float:
    return drone.xcor() + (drone_length/2)

def move_up()-> None:
    global drone_velocity
    drone_velocity = drone_speed

acceleration: float = -9.8
velocity: float = 100
y: float = 0

   
drone.penup()

#small laser properties
small_laser_damage: float = 1
small_laser_width: float = 120
small_laser_length: float = 15

# big laser properties
laser_damage: float = 3
laser_width: float = 240
laser_length: float = 20
#meteorite properties
meteorite_damage: float = 2
meteorite_width: float = 85
meteorite_length: float = 85
#heart
hearts_index: int = 2
gap_size: float = 10.0
heart_width: float = 30
heart_thickness: float = 30


def make_heart(x: float, y: float)-> turtle.Turtle:
    elisona: turtle.Turtle = turtle.Turtle()
    elisona.shape("heart.gif")
    elisona.speed(0)
    elisona.shapesize(heart_thickness/20, heart_width/20)
    elisona.penup()
    elisona.goto(x, y)
    elisona.color("red")
    
    return elisona
def make_heart_bar(color,y) -> None:
    x=-box_size/2.0 + gap_size + heart_width/2.0
    for i in range(0, 3, 1):
        hearts_row.append(make_heart(x ,y))
        x = x + heart_width + gap_size
        
y_heart: float = (box_size / 2.0) - gap_size - (heart_thickness / 2.0)
row1: list[turtle.Turtle] = make_heart_bar("red", y_heart)



# gun properties
gun_damage_: float = 1
# #bullet looks
# bullet: turtle.Turtle = turtle.Turtle()
# bullet.pencolor("yellow")
# bullet.fillcolor("yellow")
# bullet.begin_fill()
# bullet.forward(5)
# bullet.left(90)
# bullet.forward(5)
# bullet.left(90)
# bullet.forward(5)
# bullet.left(90)
# bullet.forward(5)
# bullet.left(90)
# bullet.forward(5)
# bullet.end_fill()
# bullet.hideturtle()
# bullet.left(90)

         
#Laser warnings

#Healthbar





#defining big laser edges wehre you can take damage as a player




#defining small laser edges wehre you can take damage as a player
def small_laser_top_edge(small_laser: turtle.Turtle) -> float:
    return small_laser.ycor() + (small_laser_length/2)
def small_laser_bottom_edge(small_laser: turtle.Turtle) -> float:
    return small_laser.ycor() - (small_laser_length/2)
def small_laser_left_edge(small_laser: turtle.Turtle) -> float:
    return small_laser.xcor() - (small_laser_width/2)
def small_laser_right_edge(small_laser: turtle.Turtle) -> float:
    return small_laser.xcor() + (small_laser_width/2)



def laser_top_edge(laser: turtle.Turtle) -> float:
    return laser.ycor() + (meteorite_width/2)
def laser_bottom_edge(laser: turtle.Turtle) -> float:
    return laser.ycor() - (meteorite_width/2)
def laser_left_edge(laser: turtle.Turtle) -> float:
    return  laser.xcor() - (meteorite_length/2)
def laser_right_edge(laser: turtle.Turtle) -> float:
    return laser.xcor() + (meteorite_length/2)

#defining meteor  edges wehre you can take damage as a player


def meteorite_top_edge(meteorite: turtle.Turtle) -> float:
    return meteorite.ycor() + (meteorite_width/2)
def meteorite_bottom_edge(meteorite: turtle.Turtle) -> float:
    return meteorite.ycor() - (meteorite_width/2)
def meteorite_left_edge(meteorite: turtle.Turtle) -> float:
    return  meteorite.xcor() - (meteorite_length/2)
def meteorite_right_edge(meteorite: turtle.Turtle) -> float:
    return meteorite.xcor() + (meteorite_length/2)
healthbar:float = 3
#how we define damage
#for big laser
def damage() -> None:
    global hearts_index
    for small_laser in small_lasers:
        if (
                drone_left_edge() < small_laser_right_edge(small_laser)
            and drone_right_edge() > small_laser_left_edge(small_laser)
            and drone_bottom_edge() < small_laser_top_edge(small_laser)
            and drone_top_edge() > small_laser_bottom_edge(small_laser)
            and small_laser.isvisible()
            # and brick.isvisible()
            ):
            hearts_row[hearts_index].hideturtle()
            hearts_index = hearts_index - 1
            small_laser.hideturtle()
    
    for meteorite in meteorites:
        if (
                drone_left_edge() < meteorite_right_edge(meteorite)
            and drone_right_edge() > meteorite_left_edge(meteorite)
            and drone_bottom_edge() < meteorite_top_edge(meteorite)
            and drone_top_edge() > meteorite_bottom_edge(meteorite)
            and meteorite.isvisible()
            # and brick.isvisible()
            ):
            hearts_row[hearts_index].hideturtle()
            hearts_index = hearts_index - 1
            meteorite.hideturtle()
            if hearts_index != -1:
                hearts_row[hearts_index].hideturtle()
                hearts_index = hearts_index - 1
                meteorite.hideturtle()
    
    for laser in lasers:
        if (
                drone_left_edge() < laser_right_edge(laser)
            and drone_right_edge() > laser_left_edge(laser)
            and drone_bottom_edge() < laser_top_edge(laser)
            and drone_top_edge() > laser_bottom_edge(laser)
            and laser.isvisible()):
            laser.hideturtle()
            hearts_row[hearts_index].hideturtle()
            hearts_row[0].hideturtle()
            hearts_row[1].hideturtle()
            hearts_row[2].hideturtle()
            hearts_index= hearts_index - 3
            laser.hideturtle()
x: float = -325   
#Health graphics
def gravity() -> None:
    global drone_velocity
    drone.goto(drone.xcor(), drone.ycor() + drone_velocity)
    drone_velocity += drone_acceleration

def spawn_enemy() -> None:
    random_number: int = random.randrange(0, 122)
    # There's a 20% chance we spawn a random enemy. If randnum <= 20, spawn an enemy
    # Inside that if statement, we can generate another random number: if 1, spawn a small laser
    # if 2, spawn a large laser, if 3, spawn a meteor, etc.
    if random_number <= 40:
        make_small_laser_spawn(random.randrange(-300, 300))
        random_number = random.randrange(0, 122)
        if random_number > 40 and random_number < 80 :
             meteorite_spawn(random.randrange(-300, 300))
        elif random_number > 80 and random_number <121:
            laser_spawn (random.randrange(0, 122))
            
            
        

def move_enemies() -> None:
    # for i in range(0, 10, 1):
        
    for small_laser in small_lasers:
        small_laser.goto(small_laser.xcor() - 8, small_laser.ycor())
    for meteorite in meteorites:
        meteorite.goto(meteorite.xcor() - 8, meteorite.ycor())
    for laser in lasers:
        laser.goto(laser.xcor() - 8, laser.ycor())
    i: int = 0
    while i < len(small_lasers):
        if small_laser_right_edge(small_lasers[i]) < -boundary:
            small_lasers[i].hideturtle()
            del small_lasers[i]
            # small_lasers.pop(i)
        else:
            i = i + 1
    
    while i < len(meteorites):
        if meteorite_right_edge(meteorites[i]) < -boundary:
            meteorites[i].hideturtle()
            del meteorites[i]
            # small_lasers.pop(i)
        else:
            i = i + 1
    while i < len(lasers):
        if laser_right_edge(lasers[i]) < -boundary:
            lasers[i].hideturtle()
            del lasers[i]
            # small_lasers.pop(i)
        else:
            i = i + 1

scoreboard: float = 0  
def startGame() -> None:
    screen.onkey(move_up, "space")
    
    lose: bool = False
    enemy_time: float = time.time()
    while True:
        gravity()
        damage()
        if time.time() - enemy_time > 2:
            spawn_enemy()
            enemy_time = time.time()

        move_enemies()
        
        if hearts_index < 0:
            lose = True
            break
        
        #if drone.xcor() == small_laser.xcor():
        
        if drone_bottom_edge() < -boundary:
            break
        if drone_top_edge() > boundary:
            break
        if healthbar == 0:
            break
        if hearts_index < 0:
            break
            
        if lose == True:
            break
    screen.tracer(0)
    writer: turtle.Turtle = turtle.Turtle()
    writer.color("white")
    writer.shapesize(30)
    writer.hideturtle()
    writer.penup()
    writer.goto(0, -50)
    writer.write("You lost!", align= "center", font=("Franklin Gothic Heavy", 18, "bold"))
    screen.tracer(1)
   
              

  
			



	# writer: turtle.Turtle = turtle.Turtle()
	# writer.hideturtle()
	# writer.color("white")
	# if lose == True:
	# 	writer.write("You lose")
	# else:
	# 	writer.write("You win!")
	


screen.tracer(1)
screen.onkey(startGame, "space")
screen.listen()
screen.mainloop()
      



