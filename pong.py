from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

dx = 0.2
dz = 0.2
xFundo = 0
xPerto = 0
xBola = 0
zBola = 3
raioBola = 0.3
largPalet = 1.8
altPalet = 0.3
limiteFundo = -10
limitePerto = 10
limiteLatEsq = -4.5
limiteLatDir = 4.5
largMureta = 1.8
altMureta = 0.6




def iniciar():

    mat_ambiente = (0.5, 0.0, 0.7, 1.0) 
    mat_difusa = (0.5, 0.5, 0.5, 1.0)
    mat_especular = (1.0, 1.0, 1.0, 1.0)
    mat_brilho = (50,) 
    posicao_luz = (xPerto, 0, limitePerto)
    glClearColor(0.,0.,1.,1.)
    glShadeModel(GL_SMOOTH) 

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambiente)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_difusa)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_especular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_brilho)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT,mat_ambiente)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def calculaNormalFace(face,vertices):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z]) 
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def Mureta(x,y,z0,zf,w,h):
    x0 = x - 0.5*w
    xf = x + 0.5*w
    y0 = y - 0.5*h
    yf = y + 0.5*h

    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    faces = ( (0,1,2,3), (0,5,6,1), (0,5,4,3), (2,3,4,7), (2,1,6,7), (5,6,7,4))

    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glNormal3fv(calculaNormalFace(face,vertices))
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()


    
def Bola(x,y,z,w,h):
    x0 = x - 0.5*w
    xf = x + 0.5*w
    z0 = z - 0.5*h
    zf = z + 0.5*h
    y0 = y - 0.5*h
    yf = y + 0.5*h

    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    faces = ( (0,1,2,3), (0,5,6,1), (0,5,4,3), (2,3,4,7), (2,1,6,7), (5,6,7,4))

    glBegin(GL_QUADS) 
    i = 0
    for face in faces:
        glNormal3fv(calculaNormalFace(face,vertices))
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

def Paleta(x,y,z,w,h):
    x0 = x - 0.5*w
    xf = x + 0.5*w
    z0 = z - 0.5*h
    zf = z + 0.5*h
    y0 = y - 0.5*h
    yf = y + 0.5*h

    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    faces = ( (0,1,2,3), (0,5,6,1), (0,5,4,3), (2,3,4,7), (2,1,6,7), (5,6,7,4))

    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glNormal3fv(calculaNormalFace(face,vertices))
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

   

def jogo():
    global xBola,zBola,dx,dz
        
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    Paleta(xFundo,0,limiteFundo,largPalet,altPalet)  
    Bola(xBola,0,zBola,raioBola,raioBola)
    Paleta(xPerto,0,limitePerto,largPalet,altPalet)
    Mureta(limiteLatEsq-(largMureta/2),0,limitePerto,limiteFundo,largMureta,altMureta)
    Mureta(limiteLatDir+(largMureta/2),0,limitePerto,limiteFundo,largMureta,altMureta)  

    xBola = xBola+dx
    zBola = zBola+dz
    if(xBola>limiteLatEsq): dx=-dx
    if(zBola>(limitePerto+altPalet)-raioBola):
        #Se tiver colisao com a paleta
        if((xBola>=xPerto-largPalet/2) and (xBola<=xPerto+largPalet/2)):
            dz=-dz
        elif zBola>limitePerto+altPalet+0.5:
           glutLeaveMainLoop()            
    if(xBola<limiteLatDir): dx=-dx
    if(zBola<(limiteFundo+altPalet)-raioBola):
        #Se tiver colisao com a paleta
        if((xBola>=xFundo-largPalet/2) and (xBola<=xFundo+largPalet/2)):
            dz=-dz
        elif zBola<limiteFundo+altPalet-0.5:
           glutLeaveMainLoop()
    glutSwapBuffers()

def teclaPressionada(key,x,y):
    global xFundo,largPalet
    if key == b'a'  or key == b'A':
        if xFundo>limiteLatEsq+largPalet/2:
            xFundo = xFundo - 0.3
    elif key == b'd' or key == b'D':
        if xFundo<limiteLatDir-largPalet/2:
            xFundo = xFundo + 0.3

def teclaEspecialPressionada(tecla,x,y):
    global xPerto,largPalet;
    if tecla == GLUT_KEY_LEFT:
        if xPerto>limiteLatEsq+largPalet/2:
            xPerto = xPerto - 0.3
    elif tecla == GLUT_KEY_RIGHT:
        if xPerto<limiteLatDir-largPalet/2:
            xPerto = xPerto + 0.3


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reprojetar(w,h):
    if h == 0:                        
        h = 1
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,800.0/600.0,0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,13.5,0,0,3,0,1,0)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow(b'Pong')
glutDisplayFunc(jogo)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glutKeyboardFunc(teclaPressionada)
glutSpecialFunc(teclaEspecialPressionada)
glClearColor(0.,0.,1.,1.)
gluPerspective(60,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-14)
glRotatef(10,1,0,0) 
glRotatef(5,0,1,0) 
glutTimerFunc(50,timer,1) 
iniciar()
glutReshapeFunc(reprojetar)
glutMainLoop()
