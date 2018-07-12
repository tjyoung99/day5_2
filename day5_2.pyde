def setup():
    size(500,500)
    background(0,0,255)

def fish(x,y,w,h):
    fill(random(0,50),random(0,50),random(0,50))
    ellipse(x,y,w,h)
    triangle(x+w/2, y, x+w, y+h/2,x+w,y-h/2)
    ellipse(x-w/3, y-h/4, h/3,h/3)
def draw():

    fish(random(500),random (500),random(40,100), random(20,50))
