import turtle
 
pencere=turtle.Screen()
pencere.bgcolor("gray")
 
turtle.color("blue","Magenta")
turtle.speed(10)
turtle.right(20)
turtle.left(34)
aci=0
for i in range(15):
    aci+=10
    turtle.circle(aci,180)