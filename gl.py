#Andrés Emilio Quinto Villagrán
#18288
#Lab 1 - point

import struct
def char(c):
    return struct.pack('=c' , c.encode('ascii'))

def word(c):
    return struct.pack('=h', c)

def dword(c):
    return struct.pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])

class Render(object):
    def __init__(self):
        self.framebuffer = []

    def clear(self, r, g, b):
        self.framebuffer =[
            [color(r, g, b) for x in range(self.width)]
            for y in range(self.height)
        ]
#Features gl
    #inicializa el frame buffer con un tamaño
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
    #Inicializa el framebuffer con especificaciones sobre donde puede dibujar
    def glViewport(self, x, y, width, height):
        self.viewPortWidth = width
        self.viewPortHeight = height
        self.xViewPort = x
        self.yViewPort = y
    #llena el mapa de un solo color
    def  glClear(self):
        self.clear()
    #Funcion con la cual podemos cambiar el color de gl clear (solo numeros de 0 a 1)
    def glClearcolor(self, r, g, b):
        #evitamos que se obtengan valores decimales
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        self.clear(r, g, b)
    #Función que nos permite cambiar el color de un punto en pantalla
    def glVertex(self, x,y):
        calcX = round((x+1)*(self.viewPortWidth/2)+self.xViewPort)
        calcY = round((y+1)*(self.viewPortHeight/2)+self.yViewPort)
        self.point(calcX, calcY)
    #Operacion la cual nos permite cambiar el color con el que funciona glVertex
    def glColor(self, r,g,b):
        r = round(r*255)
        g = round(g*255)
        b = round(b*255)
        return color(r, g, b)

    def write(self, filename):
        f = open(filename, 'bw')

        #Header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        #image header 
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #Pixel data

        for x in range(self.width):
                for y in range(self.height):
                        #print(self.width,' ', self.height,' hola')
                        f.write(self.framebuffer[y][x])

        f.close()

#function dot
    def point(self, x, y):
        self.framebuffer[x][y] = self.glColor(1,1,0)  


   
r = Render()
r.glCreateWindow(100, 100)
r.glClearcolor(0.14, 0.2018, 0.26)
r.glViewport(10, 00, 50, 50)
r.glVertex(1, 1)
r.write('out.bmp')