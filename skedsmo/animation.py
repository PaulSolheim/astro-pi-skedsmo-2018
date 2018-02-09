from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.set_rotation(270)

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
black = (0,0,0)
magenta = (74,35,90)
lila=(255,0,0)
lilla=(187,143,206)
Black= (23, 32, 42)
oransj = (255,140,0)
grey =(10,10,10)
gray = (55,55,55)
brown = (182, 82, 10)
orange = (234,122,11)
BRUN = (110, 44, 0 )


def aina():
    G = green
    Y = yellow
    B = blue
    O = nothing
    W = white
    R = red

    image1 = [
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R,
      W,W,W,B,W,W,W,W,
      B,B,B,B,B,B,B,B,
      W,W,W,B,W,W,W,W,
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R
    ]

    G = green
    R = red
    O = nothing
    W = yellow
    B = green
    
    image2 = [
        R,R,W,B,W,R,R,R,
        R,R,W,B,W,R,R,R,
        W,W,W,B,W,W,W,W,
        B,B,B,B,B,B,B,B,
        W,W,W,B,W,W,W,W,
        R,R,W,B,W,R,R,R,
        R,R,W,B,W,R,R,R,
        R,R,W,B,W,R,R,R
    ]

    P = pink
    O = nothing
    S = black
    W = white
    
    image3 = [
    S,W,W,W,W,W,W,S,
    S,S,W,W,W,W,S,S,
    S,W,S,S,S,S,W,S,
    S,W,S,W,W,S,W,S,
    S,W,S,S,W,S,S,S,
    S,P,W,S,W,S,P,S,
    W,S,W,W,S,W,W,S,
    W,W,S,S,S,S,S,W
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)
    sense.set_pixels(image3)
    sleep(1)


def amalie():
    y = yellow
    r = red
    n = nothing
    w = white
    
    image1 = [
      
    n,n,n,n,n,n,n,n,
    n,n,n,y,y,y,n,n,
    n,n,y,y,y,y,y,n,
    n,y,y,w,y,y,w,y,
    n,y,y,y,y,y,y,y,
    n,y,y,r,y,y,r,y,
    n,n,y,y,r,r,y,n,
    n,n,n,y,y,y,n,n
    ]

    P = pink
    O = blue
    
    image2 = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)


def arvan():
    W = white
    o = nothing
    p = pink
    
    image1 = [
    p,o,p,o,p,o,p,o,
    p,p,p,o,o,o,o,p,
    p,o,o,o,p,p,p,p,
    p,p,p,o,o,o,o,p,
    p,p,p,p,p,p,p,p,
    p,p,p,p,p,p,p,p,
    p,o,o,o,o,p,o,o,
    p,p,p,o,o,p,p,p
    ]
    
    sense.set_pixels(image1)
    sleep(1)    


def evelin():
    G = green
    Y = yellow
    B = blue
    o = nothing
    W = white
    R = red
    image1 = [
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R,
      W,W,W,B,W,W,W,W,
      B,B,B,B,B,B,B,B,
      W,W,W,B,W,W,W,W,
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R
    ]
    
    W = yellow
    B = red
    R = green
    
    image2 = [
    R,R,W,B,W,R,R,R,
    R,R,W,B,W,R,R,R,
    W,W,W,B,W,W,W,W,
    B,B,B,B,B,B,B,B,
    W,W,W,B,W,W,W,W,
    R,R,W,B,W,R,R,R,
    R,R,W,B,W,R,R,R,
    R,R,W,B,W,R,R,R
    ]
    
    P = pink
    O = nothing
    b = blue
    W = white
    
    image3 = [
    b,W,W,W,W,W,W,b,
    b,b,W,W,W,W,b,b,
    b,W,b,b,b,b,W,b,
    b,W,b,W,W,b,W,b,
    b,W,b,b,W,b,b,b,
    b,P,W,b,W,b,P,b,
    W,b,W,W,b,W,b,W,
    W,W,b,b,b,b,W,W
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)
    sense.set_pixels(image3)
    sleep(1)


def fabian():
    w = white
    p = pink
    o = nothing
    
    image1 = [
    p,p,p,p,o,o,p,w,
    p,p,p,o,o,o,w,o,
    p,p,p,o,o,o,o,w,
    p,p,o,o,o,w,o,o,
    p,p,p,p,o,o,p,w,
    p,p,p,o,o,o,w,o,
    p,p,p,o,o,o,o,w,
    p,p,o,o,o,w,o,o
    ]    

    P = pink
    O = lila
    
    image2 = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)    


def haakon():
    G = green
    Y = yellow
    B = pink
    N=yellow
    T=green
    R = green
    H=yellow
    
    image1 = [
      R,R,H,B,H,R,R,R,
      R,R,H,B,H,R,R,R,
      H,H,H,B,H,H,H,H,
      B,B,B,B,B,B,B,B,
      H,H,H,B,H,H,H,H,
      R,R,H,B,H,R,R,R,
      R,R,H,B,H,R,R,R,
      R,R,H,B,H,R,R,R
    ]
    
    R= green
    H= red
    B = blue
    
    image2 = [
      R,R,H,B,H,R,R,R,
      R,R,H,B,H,R,R,R,
      H,H,H,B,H,H,H,H,
      B,B,B,B,B,B,B,B,
      H,H,H,B,H,H,H,H,
      R,R,H,B,H,R,R,R,
      R,R,H,B,H,R,R,R,
      R,R,H,B,H,R,R,R
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)


def henrik():
    G = green
    R = blue
    O = nothing
    W = blue
    B = yellow
    
    image1 = [
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R,
      W,W,W,B,W,W,W,W,
      B,B,B,B,B,B,B,B,
      W,W,W,B,W,W,W,W,
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R,
      R,R,W,B,W,R,R,R
    ]
    
    W = white
    O = red
    
    image2 = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O
    ]

    P = pink
    O = nothing
    B = blue
    R = red
    W = white
    
    image3 = [
      B,B,B,B,B,R,R,R,
      B,B,B,B,B,W,W,W,
      B,B,B,B,B,R,R,R,
      W,W,W,W,W,W,W,W,
      R,R,R,R,R,R,R,R,
      W,W,W,W,W,W,W,W,
      R,R,R,R,R,R,R,R,
      W,W,W,W,W,W,W,W
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)
    sense.set_pixels(image3)
    sleep(1)    


def leonard():
    W = white
    B=Black
    O = yellow
    
    image1 = [   
    O,O,O,O,O,O,O,O,
    O,B,B,O,O,B,B,O,
    O,B,B,O,O,B,B,O,
    O,O,O,O,O,O,O,O,
    O,B,O,O,O,O,B,O,
    O,O,B,O,O,B,O,O,
    O,O,O,B,B,B,O,O,
    O,O,O,O,O,O,O,O
    ]
    
    sense.set_pixels(image1)
    sleep(1)    


def mathias():
    O = blue
    P = red
    
    image1 = [
      P,P,P,P,P,P,P,P, 
      P,O,O,P,P,O,O,P,
      P,O,O,P,P,O,O,P,
      P,P,P,P,P,P,P,P, 
      P,P,O,O,O,O,P,P,
      P,P,P,P,P,P,P,P,
      P,P,P,P,P,P,P,P,
      P,P,P,P,P,P,P,P
    ]
    
    O = nothing
    P = pink
    
    image2 = [
      P,P,P,P,P,P,P,P, 
      P,O,O,P,P,O,O,P,
      P,O,O,P,P,O,O,P,
      P,P,P,P,P,P,P,P, 
      P,P,O,O,O,O,P,P,
      P,P,P,P,P,P,P,P,
      P,P,P,P,P,P,P,P,
      P,P,P,P,P,P,P,P
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)


def mathilde():
    b = green
    w = white
    s = yellow
    a = nothing
    
    image1 = [
    b,b,b,b,b,b,b,b,
    b,a,a,b,b,a,a,b,
    b,a,a,b,b,a,a,b,
    b,b,b,a,a,b,b,b,
    b,b,a,a,a,a,b,b,
    b,b,a,a,a,a,b,b,
    b,b,a,b,b,a,b,b,
    b,b,b,b,b,b,b,b
    ]

    sense.set_pixels(image1)
    sleep(1)


def noen():
    B=blue
    O = nothing
    
    image1 = [
    O, O, O, O, O, O, O, O,
    O, B, B, O, B, B, O, O,
    B, B, B, B, B, B, B, O,   
    B, B, B, B, B, B, B, O,
    O, B, B, B, B, B, O, O,
    O, O, B, B, B, O, O, O,
    O, O, O, B, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    
    R = red
    Y = yellow
    B = blue
    G = green
    
    image2 = [
    G, Y, Y, Y, Y, Y, Y, G,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, B, Y, Y, B, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, R, Y, Y, Y, Y, R, Y,
    Y, Y, R, R, R, R, Y, Y,
    G, Y, Y, Y, Y, Y, Y, G
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)


def oliver():
    G = green
    Y = yellow
    B = blue
    L= lilla
    R=red
    O = nothing
    R =red
    
    image1 = [
      R,R,Y,Y,Y,Y,R,R,
      R,R,Y,Y,Y,Y,R,R,
      Y,Y,Y,Y,Y,Y,Y,Y,
      Y,Y,Y,Y,Y,Y,Y,Y,
      R,R,Y,Y,Y,Y,R,R,
      R,R,R,R,R,R,R,R,
      Y,Y,Y,Y,Y,Y,Y,Y,
      Y,Y,Y,Y,Y,Y,Y,Y
    ]
    
    G = green
    R = red
    O = nothing
    B = blue
    W= white
    
    image2 = [
        R,R,R,R,R,R,R,R,
        B,B,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        R,R,R,R,R,R,R,R,
        B,B,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        R,R,R,R,R,R,R,R,
        B,B,B,B,B,B,B,B
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)


def peter():
    W = white
    o = oransj
    B = blue
    R = red
    G = grey
    O = nothing
    
    image1 = [
    O, B, O, O, O, O, B, O, 
    O, B, B, B, B, B, B, O,
    O, R, G, R, R, G, R, O,
    O, R, B, R, R, B, R, O,
    O, R, G, G, G, G, R, O,
    O, R, W, G, G, W, R, O,
    O, O, R, W, W, R, O, O,
    O, O, O, R, R, O, O, O
    ]
    
    sense.set_pixels(image1)
    sleep(1)    


def sander():
    W = white
    P = pink
    B = blue
    R = red
    
    image1 = [
     R,R,R,R,R,R,R,R,
     P,R,R,B,R,R,R,P,
     P,R,R,B,R,R,R,P,
     P,R,R,B,R,R,R,P,
     P,R,R,B,R,R,R,P,
     P,R,R,B,R,R,R,P,
     P,W,W,B,W,W,W,P,
     R,W,W,B,W,W,W,R
    ]
    
    sense.set_pixels(image1)
    sleep(1)    


def sebastian():
    G = gray
    Y = yellow
    B = brown
    O = nothing
    W = nothing
    
    image1 = [
      W,W,W,W,W,W,G,G,
      W,W,W,W,W,G,G,G,
      W,W,W,W,G,G,G,W,
      W,W,W,G,G,G,W,W,
      B,W,G,G,G,W,W,W,
      W,B,G,G,W,W,W,W,
      W,G,B,W,W,W,W,W,
      G,W,W,B,W,W,W,W
    ]

    G = green
    R = red
    O = orange
    B = brown
    W = white
    
    image2 = [
      B,B,B,B,B,B,B,B,
      O,B,O,B,B,O,O,B,
      O,G,O,O,O,O,G,O,
      O,O,O,O,O,O,O,O,
      O,R,R,W,W,R,R,O,
      O,R,R,R,R,R,R,O,
      O,O,R,R,R,R,O,O,
      O,O,O,O,O,O,O,O
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)


def vilje():
    R = red
    Y = yellow
    B = blue
    G = green
    
    image1 = [
    G, Y, Y, Y, Y, Y, Y, G,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, B, Y, Y, B, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, R, Y, Y, Y, Y, R, Y,
    Y, Y, R, R, R, R, Y, Y,
    G, Y, Y, Y, Y, Y, Y, G
    ]
    
    G = green
    R = red
    O = nothing
    B = BRUN
    
    image2 = [
    O, G, G, O, B, O, G, G, 
    O, O, G, G, B, G, G, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O
    ]

    W = white
    B = blue
    R = red
  
    image3 = [
    R, R, W, B, B, W, R, R,  
    R, R, W, B, B, W, R, R, 
    W, W, W, B, B, W, W, W,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,  
    W, W, W, B, B, W, W, W,
    R, R, W, B, B, W, R, R,
    R, R, W, B, B, W, R, R
    ]
    
    G = green
    O = nothing
    
    image4 = [
    G, G, G, G, G, G, G, G, 
    G, O, O, G, G, O, O, G,
    G, O, O, G, G, O, O, G,
    G, G, G, O, O, G, G, G,
    G, G, O, O, O, O, G, G,
    G, G, O, O, O, O, G, G, 
    G, G, O, G, G, O, G, G, 
    G, G, G, G, G, G, G, G
    ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)
    sense.set_pixels(image3)
    sleep(1)
    sense.set_pixels(image4)
    sleep(1)


def show_animation():
    x = randint(1, 16)
    if x == 1:
        aina()
    elif x == 2:
        amalie()
    elif x == 3:
        arvan()
    elif x == 4:
        evelin()        
    elif x == 5:
        fabian()
    elif x == 6:
        haakon()
    elif x == 7:
        henrik()
    elif x == 8:
        leonard()        
    elif x == 9:
        mathias()
    elif x == 10:
        mathilde()
    elif x == 11:
        noen()
    elif x == 12:
        oliver()
    elif x == 13:
        peter()
    elif x == 14:
        sander()
    elif x == 15:
        sebastian()
    elif x == 16:
        vilje()