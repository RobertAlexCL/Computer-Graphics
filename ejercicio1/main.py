# Programa principal
from gl import Renderer

width = 960
height = 540

rend = Renderer(width, height)

rend.glClearColor(0,0,0)

rend.glClear()

rend.glVertex(150, 100)

rend.glFinish("output.bmp")


