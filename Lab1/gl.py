#  gl.py

#Import struct to have c# alike structures with memory defined
import struct
#We import our object class to gl.py
from obj import Obj

#char 1 byte
def char(var):
    return struct.pack('=c',var.encode('ascii'))

#word 2 bytes
def word(var):
    return struct.pack('=h',var)

#double word 4 bytes
def dword(var):
    return struct.pack('=l',var)

#double double word 8 bytes
def ddword(var):
    return struct.pack('=q',var)

#color function ro return rgb in bytes
def color(r,g,b):
    return bytes([b,g,r])

#color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([round(b*255),round(g*255),round(r*255)])

#class Render for library of gl
class Render(object):
    #Inititalize function glInit
    #Takes width and height to initialize, also the color
    def __init__(self,width,height,color=None):
        self.glInit(width,height,color)

    def glInit(self,width,height,color=None):
        self.glCreateWindow(width,height)
        self.currentColor = colorScale(1,1,1) if color==None else color
        self.glClear()
        self.glViewPort(0,0,width-1,height-1)
  
    #Size of image result
    def glCreateWindow(self,width,height):
        self.width = width
        self.height = height
    
    #Change Viewport position
    def glViewPort(self,x, y, width, height):
        if(x>=self.width or y>=self.height):
            return False
        if(x+width>=self.width or y+height>=self.height):
            return False
        #We save the data necessary for the viewPort
        self.viewPortWidth= width
        self.viewPortHeight = height
        self.viewPortX = x
        self.viewPortY = y
        return True

    #Clear to set bitmap of one color default black
    def glClear(self):
        #Set to black
        self.glClearColorScaleRGB(0,0,0)

    #Set bitmap to specif color
    def glClearColorScaleRGB(self,r,g,b):
        self.backgroundColor = colorScale(r,g,b)
        #Basically painting background
        # for x in range(self.width):
        #     for y in range(self.height):
        #         self.pixels[x][y]=colorPixels
        # Easier to use nested list comprenhension
        #https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
        self.pixels= [[self.backgroundColor for x in range(self.width)] for y in range(self.height)]

    #Functions to create points as absolute position
    def glVertexRGBAbsolute(self,x,y,r,g,b):

        self.pixels[y][x]=colorScale(r,g,b)

    def glVertexColorAbsolute(self,x,y,color=None):
        try:
            self.pixels[y][x]=self.currentColor if color == None else color
           
        except:
            #If tries to draw outside scren
            pass
    #Functions to create points as relative position of ViewPort
    def glVertexRGBRelative(self,x,y,r,g,b):
        xAbs =round(((x+1)*(self.viewPortWidth/2))+ self.viewPortX)
        yAbs =round(((y+1)*(self.viewPortHeight/2))+ self.viewPortY)
        self.pixels[yAbs][xAbs]=colorScale(r,g,b)

    def glVertexColorRelative(self,x,y,color=None):
        try:
            xAbs =round(((x+1)*(self.viewPortWidth/2))+ self.viewPortX)
            yAbs =round(((y+1)*(self.viewPortHeight/2))+ self.viewPortY)
            self.pixels[yAbs][xAbs]=self.currentColor if color == None else color
        except:
            #If tries to draw outside scren
            pass
    #Change current vertex color
    def glColor(self,color):
        self.currentColor=color;

    def glColorRGB(self,r,g,b):
        self.currentColor=colorScale(r,g,b)
    
    #Function to write image in file
    def glFinish(self,filename):
        file = open(filename,'wb')
        #https://itnext.io/bits-to-bitmaps-a-simple-walkthrough-of-bmp-image-format-765dc6857393
        #Reference to construct BMP

        #File Type Data BMP Header 14 Bytes
        file.write(char('B'))
        file.write(char('M'))
        file.write(dword(14+40+self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(14+40))

        #File Image Header 40 Bytes
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        #Pixels 3 Bytes each
        for x in range(self.height):
            for y in range(self.width):
                 file.write(self.pixels[x][y])
        file.close()


    #Function for a line
    def glLine(self,x0,y0,x1,y1,color=None):
        #Convert to absolute coordinates
        x0Abs =round(((x0+1)*(self.viewPortWidth/2))+ self.viewPortX)
        y0Abs =round(((y0+1)*(self.viewPortHeight/2))+ self.viewPortY)
        x1Abs =round(((x1+1)*(self.viewPortWidth/2))+ self.viewPortX)
        y1Abs =round(((y1+1)*(self.viewPortHeight/2))+ self.viewPortY)
        dy=y1Abs-y0Abs
        dx=x1Abs-x0Abs
        #Graphic a point if is the same
        if(x0Abs==x1Abs and y0Abs==y1Abs):
             self.glVertexColorAbsolute(round(x0Abs),round(y0Abs))
        
        #If vertical line
        if(dx==0):
            #Vertical Line
            step= +1 if (y1Abs>y0Abs) else -1;
            
            for y in range(y0Abs,y1Abs,step):
                x=x0Abs
                self.glVertexColorAbsolute(round(x),round(y))
        #Any other line
        else:
           #Use mx+b=y if m<=1 else my+b=x m>1
           #This is better for points by set rather tan using just mx+b=y
            m=dy/dx
            if(abs(m)<=1 or dy==0):
                b=y0Abs-(m*x0Abs)
                step = 1 if (dx>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for x in range(x0Abs,x1Abs,step):
                    y=m*x+b
                    self.glVertexColorAbsolute(round(x),round(y))
            else:
                m=dx/dy
                b=x0Abs-(m*y0Abs)
                step = 1 if (dy>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for y in range(y0Abs,y1Abs,step):
                    x=m*y+b
                    self.glVertexColorAbsolute(round(x),round(y))
            
            
    #Function for a line Coordenadas absolutas
    def glLineAbsolute(self,x0Abs,y0Abs,x1Abs,y1Abs,color=None):
        if(x0Abs>self.width or y0Abs>self.height or x1Abs>self.width or y1Abs>self.height):
            return False
        dy=y1Abs-y0Abs
        dx=x1Abs-x0Abs
        #Graphic a point if is the same
        if(x0Abs==x1Abs and y0Abs==y1Abs):
             self.glVertexColorAbsolute(round(x0Abs),round(y0Abs))
        
        #If vertical line
        if(dx==0):
            #Vertical Line
            step= +1 if (y1Abs>y0Abs) else -1;
            
            for y in range(y0Abs,y1Abs,step):
                x=x0Abs
                self.glVertexColorAbsolute(round(x),round(y))
        #Any other line
        else:
           #Use mx+b=y if m<=1 else my+b=x m>1
           #This is better for points by set rather tan using just mx+b=y
            m=dy/dx
            if(abs(m)<=1 or dy==0):
                b=y0Abs-(m*x0Abs)
                step = 1 if (dx>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for x in range(x0Abs,x1Abs,step):
                    y=m*x+b
                    self.glVertexColorAbsolute(round(x),round(y))
            else:
                m=dx/dy
                b=x0Abs-(m*y0Abs)
                step = 1 if (dy>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for y in range(y0Abs,y1Abs,step):
                    x=m*y+b
                    self.glVertexColorAbsolute(round(x),round(y))
            
            
    #Function to load any obj model
    def loadObjModel(self,filename,translateX=None,translateY=None,scaleX=None,scaleY=None):
        #Load our objModel so we can draw it in our gl
        objModel = Obj(filename)
        
        #Our tranlations and scales to draw
        translateX= translateX if translateX!=None else round(self.width/2)
        translateY= translateY if translateY!=None else round(self.height/2)
        scaleX= scaleX if scaleX!=None else round(self.width/4)
        scaleY= scaleY if scaleY!=None else round(self.height/4)
        #For each face that has reference to v,vn,vt
        for face in objModel.faces:
            #For each reference to [v,vn and vt] as a list
            #Vertex[0] will make reference to each v referencing a vertexIndex to an actual vertex
            for i in range(len(face)):
                vertex=face[i]
                vertex1=face[(i+1)%len(face)]
                #We only focus on the first value of each f/// that is for just v
                #Vertex[0] has reference to the position of v starting counting in 1 for the actual coordinates of vertex
                try:
                    v0=objModel.vertexIndexes[vertex[0]-1]
                    x0=round(v0[0]*scaleX + translateX)
                    y0=round(v0[1]*scaleY + translateY)
                    v1=objModel.vertexIndexes[vertex1[0]-1]
                    x1=round(v1[0]*scaleX + translateX)
                    y1=round(v1[1]*scaleY + translateY)
                    # self.glVertexColorAbsolute(x0,y0)
                    self.glLineAbsolute(x0,y0,x1,y1)
                except:
                    #There must be an error on the files point
                    pass
                
     