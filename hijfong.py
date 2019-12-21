import random


def mandelbrot (re, Im, max_iter):
  c = complex (Re,Im)
  z = 0.0j

  for i in range (max_iter):
     c = complex(re,Im)
     z = z * z + c
     if ( z.real * z.real + z.imag * z.imag) > 4:
         return i
  return max_iter

columns = 10
rows = 10

print "HijFong"
for Re in range ( -2000, 1000, 333 ):
    for Im in range ( -1000, 1000, 200 ):
        print mandelbrot(Re/1000.0,Im/1000.0,100),
    print

mm = 40

# make sure 0,0 as first answer cannot win

while mm < 80 and mm > 20:
  r = random.randint(-2000, 1000) / 1000.0
  i = random.randint(-1000, 1000) / 1000.0
  mm = mandelbrot(r,i,100)

ro = 0.0
io = 0.0

while 1:
  
  real = raw_input("player 1: Real: ")
  imag = raw_input("player 1: Imag: ")
  
  r = r + float(real)/100.0;
  i = i + float(imag)/100.0;
  ro = ro + float(r)
  io = io + float(i)

  mm = mandelbrot(r,i,100)
  print "Stability factor=",mm," x=",ro*100,"y=",io*100
  if mm > 20 and mm < 80:
    print "you won"
  
  real = raw_input("player 2: Real: ")
  imag = raw_input("player 2: Imag: ")
  
  r = r + float(real)/100.0;
  i = i + float(imag)/100.0;
  ro = ro + float(r)
  io = io + float(i)
  
  mm =  mandelbrot(r,i,100)
  print "Stability factor=",mm," x=",ro*100,"y=",io*100
  if mm > 20 and mm < 80:
    print "you won"
  
