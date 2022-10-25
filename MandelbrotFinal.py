#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:06:41 2021

@author: shenlu
"""
"""
Erik Ely
OMH

used to see find interesting parts of the mandelbrot https://www.atopon.org/mandel/#
found the part of the julia set I used here https://www.karlsims.com/julia.html

For this project, I first found the general part of the fractal that I wanted to use.
Next, I would sketch out an idea of what I wanted the fractal to look like after I colored it in.
After that, I would try to use math to think about how to get the colors correctly.
Then I'd use a bit of trial and error to see if my initial guess was correct, and then if it
wasn't right, I'd rethink it through.

For my fractal of choice, I chose the julia set which uses the same equation as the mandelbrot,
just with a few changes. First, the initial z values are determined by the position in the
picture. Second, the C value is the same for all over the fractal. (Basically, the c and z switch, but c doesn't start as 0+0i)
"""


from PIL import Image


global imgnum
imgnum = 1

#This is the mandelbrot function. It sets z as 0+0i. The c value is determined in a function below, and is used to see how many escapes it takes in a while loop.
#If it takes too many iterations for it to escape, the loop is cut off
def mandelbrot():
    global imgx, imgy, maxIteration, iterations, cx, cy, c, xmax, xmin, ymax, ymin, image1, image2, image3, imgnum
    z = complex(0,0)
    iterations = 0
    while abs(z) < 2 or iterations < maxIteration:
        z = z**2 +c
        iterations += 1
        if abs(z) >= 2 or iterations >= maxIteration:
            break
        
#This is the julia function. It sets c at an interesting value. The z value is determined in a function below, and is used to see how many escapes it takes in a while loop.
#If it takes too many iterations for it to escape, the loop is cut off
def juliaset():
    global imgx, imgy, maxIteration, iterations, cx, cy, c, xmax, xmin, ymax, ymin, image1, image2, image3, imgnum, z
    c = complex(-0.162,1.04)
    iterations = 0
    while abs(z) < 2 or iterations < maxIteration:
        z = z**2 +c
        iterations += 1
        if abs(z) >= 2 or iterations >= maxIteration:
            break

maxIteration = 255
#image size
imgx, imgy = 1000, 1000

#this is the function responsible for choosing the zoom in images and coloring them in.
#It determines the cx and cy value each loop through. In the mandelbrot images, those are used in the c. But in the julia set, that's used for the z.
#if statements are used to let me use just one function to generate all 3 images

def makeimage():
    global imgx, imgy, maxIteration, iterations, cx, cy, c, xmax, xmin, ymax, ymin, image1, image2, image3, imgnum, z
    if imgnum == 1:    
        image1 = Image.new("RGB",(imgx, imgy))
        xmin, xmax, ymin, ymax = 0.4218, 0.4257, 0.2059, 0.2099
        imgnum = 2
    elif imgnum == 2:
        image2 = Image.new("RGB",(imgx, imgy))
        xmin, xmax, ymin, ymax = -0.8128, -0.8093, 0.1826, 0.1861
        imgnum = 3
    elif imgnum == 3:
        image3 = Image.new("RGB",(imgx, imgy))
        xmin, xmax, ymin, ymax = 0.065, 0.095, 0.085, 0.115
        imgnum = 4
        
    for y in range(imgy):
        cy = y * (ymax-ymin)/(imgy) + ymin
        for x in range(imgx):
            cx = x * (xmax-xmin)/(imgx) + xmin
            if imgnum == 2 or imgnum == 3:
                c = complex(cx,cy)
                mandelbrot()
            if imgnum == 4:
                z = complex(cx,cy)
                juliaset()
            if imgnum == 2:
                r = (int(iterations*1.25))%256
                #this makes it so that there are 3 main colors that compose the picture
                g = (iterations*80)%256
                b = maxIteration-iterations
                image1.putpixel((x,y), (r,g,b))
            if imgnum == 3:
                #this colors in the spiral part of the fractal as green, but darkens it
                g = (iterations)%256 - 80
                if g < 0:
                    g = 0
                r=0
                b=0
                #this colors outside of the spiral and shades it in a range of grey to black
                if iterations < 90:
                    g, r, b = 90 - iterations,90 - iterations,90 - iterations
                
                image2.putpixel((x,y), (r,g,b))
            if imgnum == 4:
                #makes the red pop out a lot
                r = ((iterations*5) + 90)
                if r > 256:
                    r = 256
                g = maxIteration - iterations - 50
                b = maxIteration - iterations - 90
                #this gives the red a lighting effect
                if iterations < 90:
                    r, g, b = (iterations*7)%256, 90 - iterations,90 - iterations
  
                image3.putpixel((x,y), (r,g,b))                   
            

makeimage()
image1.show()
image1.save("ELYMandelbrot1","PNG")


makeimage()
image2.show()
image2.save("ELYMandelbrot2", "PNG")


makeimage()
image3.show()
image3.save("ELYJuliaset", "PNG")

"""
I got help from Caelan with coloring my images in. He not only helped me with the math aspects,
but also the design aspects and choosing what looked the best. He especaially helped me with
changing the brigthness levels on my images to look best.
"""





























