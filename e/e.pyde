x=0
y=0
def setup():
    size(600,600)
    background(255,0,0)
def draw():
    global x, y
    point(100,100)
    point(500,100)
    
    translate(350,350)
    fill(15,x,x)
    rotate(y)
    x=x+1
    y=y+1
    ellipse(x,x,y,y)
    if y >= 700:
        text(u'салам малейкум', 0, 0)
        noLoop()
        
        
        

    
