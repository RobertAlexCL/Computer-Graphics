# Laboratorio 2 Main.py

#Import our gl library
from gl import Render,colorScale

#Main for gl

#Messages along the program
welcome=''''
Bienvenido al programa del laboratorio 1. 
Este programa servirá para comprobar el funcionamiento de nuestra librería GL.
'''
enterWindowSize = "Primero debe ingresar el tamaño de la ventana de la imagen BMP."
generalRules="Ahora puede comenzar a editar su ventana. El viewport actual es sobre toda la ventana."
menu='''
Cuenta con el siguiente menu para modificar graphic.bmp en esta misma carpeta.
    1. Cambiar color background de la ventana.
    2. Cambiar color del pincel de puntos.
    3. Cambiar viewPort.
    4. Crear un nuevo punto.
    5. Crear una línea.
    6. Finalizar y guardar el archivo graphic.bmp.
    7. Cualquier otra tecla para salir. (Ojo si sale y no guarda primero, se perderán los cambios.)
    Ingrese su opción: 
'''

#Variables along the program
windowHeight=-1
windowWidth=-1
viewPortX=-1
viewPortY=-1
viewPortWidth=-1
viewPortHeight=-1
r=-1
g=-1
b=-1
vertexX=-1
vertexY=-1
mainOption=1

#Functions that verify stuff along the program
#Verify a positive int is used
def askForPositiveInt(message):
    while True:
        try:
            number = int(input(message))
            if(number>0):
                return number
            print("Error. El valor ingresado debe ser positivo.")
        except: 
            print("Error. El valor ingresado debe ser un entero")
            continue

#Verify number is between 0 and 1, 2nd param if -1 to 1
def askForNumberBetween0and1(message,negativesAllowed=False):
    while True:
        try:
            number = float(input(message))
            if(abs(number)<=1 and negativesAllowed):
                return number
            elif(number<=1 and number>=0):
                return number
            if(negativesAllowed):
                print("Error. El valor ingresado debe encontrarse entre -1 y 1")
            else:
                print("Error. El valor ingresado debe encontrarse entre 0 y 1")
        except: 
            print("Error. El valor ingresado debe ser un número")
            continue


#Start printing options for program
print(welcome)
print(enterWindowSize)

windowWidth=(askForPositiveInt('Ingrese el ancho de la ventana: '))
windowHeight=(askForPositiveInt('Ingrese la altura de la ventana: '))
#Initialize mainGL
mainGl=Render(windowWidth,windowHeight)
print(generalRules)
while(True):
    mainOption=input(menu)
    #glClearColor change color for window background
    if(mainOption=="1"):
        
        r=(askForNumberBetween0and1('Ingrese el valor R del color: '))
        g=(askForNumberBetween0and1('Ingrese el valor G del color: '))
        b=(askForNumberBetween0and1('Ingrese el valor B del color: '))
        mainGl.glClearColorScaleRGB(r,g,b)
        continue
    #glColor change color for points
    elif(mainOption=="2"):
        r=(askForNumberBetween0and1('Ingrese el valor R del color: '))
        g=(askForNumberBetween0and1('Ingrese el valor G del color: '))
        b=(askForNumberBetween0and1('Ingrese el valor B del color: '))
        mainGl.glColorRGB(r,g,b)  
        continue
    #glViewPort change viewPort
    elif(mainOption=="3"):
        viewPortX=(askForPositiveInt('Ingrese la coordenada absoluta en x: '))
        viewPortY=(askForPositiveInt('Ingrese la coordenada absoluta en y: '))
        viewPortWidth=(askForPositiveInt('Ingrese el ancho del viewPort: '))
        viewPortHeight=(askForPositiveInt('Ingrese la altura del viewPort: '))
        if(mainGl.glViewPort(viewPortX,viewPortY,viewPortWidth,viewPortHeight)==False):
            print("Error en los datos ingresados de tamaños y coordenadas.")
        continue
    #glVertex create point
    elif(mainOption=="4"):
         vertexX=(askForNumberBetween0and1('Ingrese el valor entre -1 y 1 en x relativo al viewPort para el punto: ',True))
         vertexY=(askForNumberBetween0and1('Ingrese el valor entre -1 y 1 en y relativo al viewPort para el punto: ',True))
         mainGl.glVertexColorRelative(vertexX,vertexY)
         continue
    #glVertex create line
    elif(mainOption=="5"):
         vertexX0=(askForNumberBetween0and1('Ingrese el valor entre -1 y 1 en x relativo al viewPort para el punto x0: ',True))
         vertexY0=(askForNumberBetween0and1('Ingrese el valor entre -1 y 1 en y relativo al viewPort para el punto y0: ',True))
         vertexX1=(askForNumberBetween0and1('Ingrese el valor entre -1 y 1 en x relativo al viewPort para el punto x1: ',True))
         vertexY1=(askForNumberBetween0and1('Ingrese el valor entre -1 y 1 en y relativo al viewPort para el punto y1: ',True))
         mainGl.glLine(vertexX0,vertexY0,vertexX1,vertexY1)
         continue
    #glFinish save
    elif(mainOption=="6"):
        mainGl.glFinish('graphic.bmp')
        continue
    #exit
    else:
        break
   
