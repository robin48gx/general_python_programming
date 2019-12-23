import random
#from graphics import *
#win = GraphWin()
# library
#import seaborn as sns
#import pandas as pd
#import numpy as np
import math

from Tkinter import *

# (c) R P Clark 2019
def redrawAll(canvas):
    canvas.delete(ALL)
    # draw a red rectangle on the left half
    canvas.create_rectangle(0, 0, 1000, 1000, fill="grey")
    # draw semi-transparent rectangles in the middle

def leftclick(event):
    print("player 1")
    #print event.x, event.y
    r = event.x/1000.0*3.0 -2.0 + rseed
    i = (1000-event.y)/1000.0*2.0 -1.0 + iseed
    #print "as coords in mandel plane r=",r," i=",i
    ro = event.x
    io = 1000-event.y
    #print "as coords to plot x=",ro," y=",1000-io
    mm = mandelbrot(r,i,100)
    col = get_col(mm)
    io = 1000 - io
    canvas.create_rectangle(ro, io, ro+10, io+10, fill=col)
    if mm > 98:
      print "you are in the STABLE zone "
    if mm < 21 and mm > 2:
      print "you are in the CHAOS zone "
    print "Stability factor=",mm," x=",ro,"y=",io
    if mm > 65 and mm < 80:
      print "you found the RAGGED EDGE OF CHAOS YOU WON"
      draw_complete()
def rightclick(event):
    print("player 2")
    print event.x, event.y
    r = event.x/1000.0*3.0 -2.0 + rseed
    i = (1000-event.y)/1000.0*2.0 -1.0 + iseed
    #print "as coords in mandel plane r=",r," i=",i
    ro = event.x
    io = 1000-event.y
    #print "as coords to plot x=",ro," y=",1000-io
    mm = mandelbrot(r,i,100)
    col = get_col(mm)
    io = 1000 - io
    canvas.create_rectangle(ro, io, ro+10, io+10, fill=col)
    if mm > 98:
      print "you are in the STABLE zone "
    if mm < 21 and mm > 2:
      print "you are in the CHAOS zone "
    print "Stability factor=",mm," x=",ro,"y=",io
    if mm > 20 and mm < 80:
      print "you found the RAGGED EDGE OF CHAOS YOU WON"
      draw_complete()
def middleclick(event):
    print("middle")

# create the root and the canvas
root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
canvas.bind("<Button-1>", leftclick)
canvas.bind("<Button-2>", middleclick)
canvas.bind("<Button-3>", rightclick)

# Store canvas in root and in canvas itself for callbacks
root.canvas = canvas.canvas = canvas
# Set up canvas data and call init
canvas.data = { }
redrawAll(canvas)

rot = random.randint(-1570, 1570) / 1000.0
zz = complex(math.cos(rot), math.sin(rot))
print " rotation ", rot, "degrees ", 90*rot/1.57, "zz ",  zz
def mandelbrot (re, Im, max_iter):
  c = complex (Re,Im) 
  #print " complex c ",c
  c = c * zz
  #print " complex c after rotaion with zz",zz, " c is now ", c
  z = 0.0j
  for i in range (max_iter):
     c = complex(re,Im) 
     c = c * zz
     z = z * z + c
     if ( z.real * z.real + z.imag * z.imag) > 4:
         return i
  return max_iter

def get_col(mm):
    if ( mm > 99 ):
        return "black"
    if ( mm > 90 ):
        return "blue"
    if ( mm > 80 ):
        return "cornflowerblue"
    if ( mm > 69 ):
        return "green"
    if ( mm > 60 ):
        return "cyan"
    if ( mm > 30 ):
        return "pink"
    if ( mm > 16 ):
        return "magenta"
    if ( mm > 12 ):
        return "red"
    if ( mm > 9 ):
        return "yellow" 
    if ( mm > 7 ):
        return "gold" 
    if ( mm > 5 ):
        return "orange" 
    if ( mm >= 3 ):
        return "grey"
    if ( mm >= 2 ):
        return "lightgrey"
    if ( mm <= 1 ):
        return "white"

columns = 10
rows = 10

print "HijFong"
for Re in range ( -2000, 1000, 333 ):
    for Im in range ( -1000, 1000, 200 ):
        print mandelbrot(Re/1000.0,Im/1000.0,100),
    print

mm = 40

# make sure 0,0 as first answer cannot win
# i.e. in the stable or very chaotic area
while mm < 90 and mm > 10:
  r = random.randint(-2000, 1000) / 1000.0
  i = random.randint(-1000, 1000) / 1000.0
  r = r/3.0
  i = i/2.0
  mm = mandelbrot(r,i,100)

rseed = r
iseed = i

def draw_complete():
  print "draw complete called"
  for rr in range (0, 1000, 10):
   for ii in range (0, 1000, 10):
     r = rr/1000.0*3.0 -2.0 + rseed
     i = ii/1000.0*2.0 -1.0 + iseed
     #print "as coords in mandel plane r=",r," i=",i
     ro = rr
     io = 1000-ii
     #print "as coords to plot x=",ro," y=",1000-io
     mm = mandelbrot(r,i,100)
     col = get_col(mm)
     #io = 1000 - io
     canvas.create_rectangle(ro, io, ro+10, io+10, fill=col)
 


#rseed = 0
#iseed = 0
#draw_complete()


ro = 0.0
io = 0.0

while 1:
  
  real = raw_input("player 1: Real: ")
  imag = raw_input("player 1: Imag: ")
  
  r = r + float(real)/100.0;
  i = i - float(imag)/100.0;
  ro = ro + float(real)
  io = io - float(imag)

  mm = mandelbrot(r,i,100)
  col = get_col(mm)
  canvas.create_rectangle(ro+500, io+500, ro+500+10, io+500+10, fill=col)
  if mm > 98:
      print "you are in the STABLE zone "
  if mm < 21:
      print "you are in the CHAOS zone "
  print "Stability factor=",mm," x=",ro,"y=",io
  if mm == 99: #if mm > 70 and mm < 75:
    print "you found the RAGGED EDGE OF CHAOS YOU WON"
    draw_complete()

  real = raw_input("player 2: Real: ")
  imag = raw_input("player 2: Imag: ")
  
  r = r + float(real)/100.0;
  i = i - float(imag)/100.0;
  ro = ro + float(real)
  io = io - float(imag)
  
  mm =  mandelbrot(r,i,100)
  col = get_col(mm)
  canvas.create_rectangle(ro+500, io+500, ro+500+10, io+500+10, fill=col)
  if mm > 98:
      print "you are in the STABLE zone "
  if mm < 21:
      print "you are in the CHAOS zone "
  print "Stability factor=",mm," x=",ro,"y=",io
  if mm == 99: #if mm > 70 and mm < 75:
    print "you found the RAGGED EDGE OF CHAOS YOU WON"
    draw_complete()
  
