import turtle
tao = turtle.Pen()
tao.shape('turtle')
for i in range(10):
    tao.penup()
    tao.goto(i*5,i*13.656)
    tao.pendown()
    for j in range(8):
        tao.forward(100-(2*5*i))
        tao.left(45)
    

  

    

