X=0
P=0
x=200
s=100
def setup():
    global P,X
    size(600,600)
    X=loadImage("T.jpeg")
    P=loadImage("golova-ryby.jpeg") 
def draw():
    global x,P,X
    background(255)
    push()
    fill(0,232,255)
    ellipse(x,300,200,200)
    pop() 
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
    textAlign(CENTER, CENTER)
    text(u'вперёд', 400, 500)
    text(u'назад',150 , 500)
    pop()



    if x>= 600:
        image( P, 0, 0)
        fill(255)
        textSize(50)
        text(u'вы прошли игру ',200,300)
        noLoop() 
    if x<= 0:
        image( X, 0, 0)
        fill(255)
        textSize(50)
        text(u'ТЫ ПРОИГРАЛ ',200,300)
        noLoop()
         
    
def mouseClicked():
    global x 
    if mouseX>300 and mouseX<500 and mouseY> 450 and mouseY<550:
        x=x+20
    if mouseX>50 and mouseX<250 and mouseY>450 and  mouseY<550:
        x=x-20
        
    
        
        

    
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     

 
