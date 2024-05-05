x=200
def setup():
    size(600,600)
def draw():
    global x
    push()
    fill(245,0,0)
    rect(0,0,600,200)
    rect(0,400,600,200)
    pop()
    
    
    fill(182,255,57)
    rect(300,450,200,100)
    rect(50,450,200,100)
    
    
    push()
    fill(0)
    rect(550,0,40,900)
    textSize(20)
    text(u'вперёд', 400, 500)
    text(u'назад',100 , 500)
    pop()
    if mouseX>300 and mouseX<500 and mouseY> 450 and mouseY<550:
        x=x+2
    if mouseX>50 and mouseX<250 and mouseY>450 and  mouseY<550:
        x=x-2 
        
    
    
    push()
    fill(0,232,255)
    ellipse(x,300,200,200)
    pop()
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     

 
