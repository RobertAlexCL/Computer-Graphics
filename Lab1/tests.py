# Laboratorio 1 Tests.py

#Import our gl library
import math
from gl import Render,colorScale


#We draw our MainGL
mainGl=Render(1000,500)

#We define our polygons

polygon1=[(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), 
        (250, 380), (220, 385), (205, 410), (193, 383)]
polygon2=[(321, 335), (288, 286), (339, 251), (374, 302)]
polygon3=[(377, 249), (411, 197), (436, 249)]
polygon4=[(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
            (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), 
            (580, 230),(597, 215), (552, 214), (517, 144), (466, 180)]
polygon5=[(682, 175), (708, 120), (735, 148), (739, 170)]
polygon6=[(100, 100), (100, 400), (800,400 ), (800, 100)]

mainGl.glColorRGB(0,0,1)
mainGl.glDrawAndPaintPolygon(polygon1)
mainGl.glColorRGB(0,1,0)
mainGl.glDrawAndPaintPolygon(polygon2)
mainGl.glColorRGB(1,0,0)
mainGl.glDrawAndPaintPolygon(polygon3)
mainGl.glColorRGB(0,1,1)
mainGl.glDrawAndPaintPolygon(polygon4)
mainGl.glColorRGB(1,1,0)
mainGl.glDrawAndPaintPolygon(polygon5)





mainGl.glFinish('graphic1.bmp')
