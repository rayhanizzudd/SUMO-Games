from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# from ikann import iwak
import math

w,h= 1000,785
def Arena(radius, center1= (500, 375) , center2=(500, 375) ):
    #HORIZONTAL1
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(80, 20)   
    glVertex2f(920, 20)
    glEnd()
    #HORIZONTAL2
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(80, 730)   
    glVertex2f(920, 730)
    glEnd()

    #VERTIKAL1
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(30, 80)
    glVertex2f(30, 670)
    glEnd()
    #VERTIKAL2
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(970, 80)
    glVertex2f(970, 670)
    glEnd()
    
    #MIRING1
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(920, 32)
    glVertex2f(964, 78)
    glEnd()
    #MIRING2
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(80, 32)
    glVertex2f(36, 78)
    glEnd()
    #MIRING3
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(36, 672)
    glVertex2f(80, 718)
    glEnd()
    #MIRING4
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(964, 672)
    glVertex2f(920, 718)
    glEnd()

    #BAGIAN KIRI
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINE_LOOP)
    for i in range(720):
        angle = math.radians(i)
        x = radius * math.cos(angle) + center1[0]
        y = radius * math.sin(angle) + center1[1]
        glVertex2f(x, y)
    glEnd()

     #BAGIAN KANAN
    glColor3ub(218, 195, 149)
    glBegin(GL_LINE_STRIP)
    for i in range(720):
        angle = math.radians(i)
        x = radius * math.cos(angle) + center2[0]
        y = radius * math.sin(angle) + center2[1]
        glVertex2f(x, y)
    glEnd()

    #KANAN
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(815,420)
    glVertex2f(815,330)
    glEnd()
    #KIRI
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(185,420)
    glVertex2f(185,330)
    glEnd()
    #ATAS
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(545,690)
    glVertex2f(455,690)
    glEnd()
    #BAWAH
    glColor3ub(218, 195, 149)
    glLineWidth(20.0)
    glBegin(GL_LINES)
    glVertex2f(545,60)
    glVertex2f(455,60)
    glEnd()
    # TENGAH1
    glColor(1,1,1)
    glLineWidth(10.0)
    glBegin(GL_LINES)
    glVertex2f(550,430)
    glVertex2f(550,320)
    glEnd()
    #TENGAH2
    glColor(1,1,1)
    glLineWidth(10.0)
    glBegin(GL_LINES)
    glVertex2f(450,430)
    glVertex2f(450,320)
    glEnd()

# def iterate():
#     glViewport(0, 0, w, h)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     glClearColor(0.4, 0.2, 0.0, 1.0)
#     Arena(300)
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(w, h)
# glutInitWindowPosition(200, 0)
# wind = glutCreateWindow("SUMO ARENA")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()