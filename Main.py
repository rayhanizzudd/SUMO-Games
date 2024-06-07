from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# from ikann import iwak
import math, fixarena, mainsumo, ikann, apel_berjalan,nasi,supsumo, nasibusuk
import random
import pygame 


w,h= 1000,800
play_game = False
menu1 = True
menu2 = False
menu3 = False
menu4 = False
mouse = None
x,y = 0,0
speed = 5
point = 0
health = 3
# health = [True, True, True]



def input_mouse(button, state, x, y):
    global mouse, menu2,menu1
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # # Dapatkan warna piksel pada koordinat x, y saat klik kiri
        viewport = glGetIntegerv(GL_VIEWPORT)
        y = viewport[3] - y  # Flip koordinat Y karena Pygame memiliki asal koordinat yang berbeda
        if x>= 396 and x <= 638 and y >= 110 and y <= 197 : 
            menu1 = False
            menu2 = True
            print("Warna piksel yang diklik (Klik Kiri):",x,y)

        if menu3 : 
            if x>= 366 and x <= 608 and y >= 100 and y <= 177 : 
                glutLeaveMainLoop()

        
def load_texture(file_path):
    image = pygame.image.load(file_path)
    image_data = pygame.image.tostring(image, "RGBA", 1)

    width, height = image.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id


# Fungsi untuk menggambar gambar di layar
def draw_image(texture_id, x, y, width, height):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)

    glTexCoord2f(1, 0)
    glVertex2f(x + width, y)

    glTexCoord2f(1, 1)
    glVertex2f(x + width, y + height)

    glTexCoord2f(0, 1)
    glVertex2f(x, y + height)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def draw_text(text, x, y):
    glPushMatrix()
    glTranslatef(x, y, 0)
    # increase spacing between characters
    glLineWidth(5)
    glScalef(0.25, 0.25, 0.25)
    for ch in text:
        # Draw each character using the arial font
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(ch))

    glPopMatrix()

def allitem():
    global point,health,menu2,menu3
    glClearColor(0.4, 0.2, 0.0, 1.0)
    fixarena.Arena(300)
    b = ikann.ikan(20)
    c = apel_berjalan.Apel()
    aa = nasi.Mangkok()
    d = supsumo.supersumo() 
    e = mainsumo.mainchar(5)
    f = nasibusuk.Busuk()
    glLoadIdentity()
    kondisi = True


    #COLLISION NASIII BERSIH
    if (aa[0] >= e[0] and aa[0] <= e[1]) and (aa[1] >= e[2] and aa[1] <= e[3]): 
        if kondisi :
            point += 100
            kondisi = False
        print("POINT KAMU : ",point)   
        print("NYAWA KAMU : ", health) 
        # print("coliosionn")
        nasi.ynasi = random.uniform(-200, -10)
        nasi.xnasi = random.uniform(-200, 900)

    #COLLISION NASIII BUSUK
    if (f[0] >= e[0] and f[0] <= e[1]) and (f[1] >= e[2] and f[1] <= e[3]): 
        if kondisi :
            point -= 100
            kondisi = False
        print("kapokk berat badanmu turun")
        print("POINT KAMU : ",point)   
        print("NYAWA KAMU : ", health) 
        nasibusuk.ynasibusuk = random.uniform(-200, -10)
        nasibusuk.xnasibusuk = random.uniform(-200, 900)

    #COLLISION IKAN
    if (b[0] >= e[0] and b[0] <= e[1]) and (b[1] >= e[2] and b[1] <= e[3]):
        if kondisi :
            point -= 100
            kondisi = False
        print("POINT KAMU : ",point)    
        print("NYAWA KAMU : ", health)
        # print("coliosionn")
        ikann.yikan = random.randrange(0,800,10)
        ikann.xikan = 2500


    #COLLISION APELL
    if (c[0] >= e[0] and c[0] <= e[1]) and (c[1] >= e[2] and c[1] <= e[3]):
        if kondisi :
            point += 100
            kondisi = False
        print("POINT KAMU : ",point) 
        print("NYAWA KAMU : ", health)   
        # print("apelll")
        apel_berjalan.xapel = random.randrange(-2200, -100, 10) 
        apel_berjalan.yapel = random.randrange(0, 1000, 10)

    #COLLISION SUPER SUMO
    if ((e[0] >= d[0] and e[0] <= d[1]) or (e[1] >= d[0] and e[1] <= d[1])) and ((e[2] >= d[2] and e[2] <= d[3]) or (e[3] >= d[2] and e[3] <= d[3])) and ((475 != e[0] and 520 != e[1]) or (387 != e[2] and 430 != e[3])):
        if kondisi : 
            health -= 1
            kondisi = False
        mainsumo.xmainchar = 0
        mainsumo.ymainchar = 0
        print("POINT KAMU : ",point)    
        print("NYAWA KAMU : ", health)

    if health == 0 :
        menu2 = False
        menu3 = True

    if point < 0:
        health -= 1
        point = 0
    else:
        draw_text(f"Score: {point}", 100, 750)
        draw_text(f"Heart: {health}", 700,750)

        #level2
    if point >= 500 :
        apel_berjalan.speedapel= 3
        nasi.speednasi = 3
        supsumo.speedsuper = 3
        ikann.speedikan = 3
        nasibusuk.speednasibusuk = 3

        #level3
    elif point >= 600 :
        apel_berjalan.speedapel= 4
        nasi.speednasi = 4
        supsumo.speedsuper = 4
        ikann.speedikan = 4
        nasibusuk.speednasibusuk = 4

    elif point <= 400:
            apel_berjalan.speedapel= 1
            nasi.speednasi = 1
            supsumo.speedsuper = 1
            ikann.speedikan = 1
            nasibusuk.speednasibusuk = 1
    glutSwapBuffers()
    
    
    
    # FITUR MAPHACK
    a = [b[0]-20, b[0]+20, b[1]-15, b[1]+15]
    aaa = [aa[0]-22, aa[0]+22,aa[1]-20,aa[1]+20]
    ap = (c[0]-15,c[0]+15,c[1]-15,c[1]+15)
    # MAPhack((475,520,387, 430),e,aaa,ap,d)

def MAPhack(a,e,aaa,ap,d):

    #ikan
    glColor3ub(0,255,0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)


    glVertex(e[1],e[2])
    glVertex(e[0],e[2])
    glVertex(e[0],e[3])
    glVertex(e[1],e[3])
    glVertex(e[1],e[2])

    glColor3ub(255,255,0)
    glVertex(a[1],a[2])
    glVertex(a[0],a[2]) 
    glVertex(a[0],a[3])
    glVertex(a[1],a[3]) 
    glVertex(a[1],a[2])
    glEnd()

    # #nasi
    # glColor3ub(0,0,255)
    # glLineWidth(2.0)
    # glBegin(GL_LINE_STRIP)

    # glVertex(e[0],e[3])
    # glVertex(e[1],e[3])
    # glVertex(e[1],e[2])
    # glVertex(e[0],e[2])
    # glVertex(e[0],e[3])-
    # glColor3ub(255,0,255)
    
    # glVertex(aaa[0],aaa[3])
    # glVertex(aaa[1],aaa[3])
    # glVertex(aaa[1],aaa[2])
    # glVertex(aaa[0],aaa[2])
    # glVertex(aaa[0],aaa[3])
    
    # glEnd()

    # # apel
    # # ap = (15,45,15,45)
    # # (30,30)
    # glColor3ub(255,0,0)
    # glLineWidth(2.0)
    # glBegin(GL_LINE_STRIP)

    # glVertex(ap[0],ap[2])
    # glVertex(ap[0],ap[3])
    # glVertex(ap[1],ap[3])
    # glVertex(ap[1],ap[2])
    # glVertex(ap[0],ap[2])
    
    # glVertex(e[0],e[2])
    # glVertex(e[0],e[3])
    # glVertex(e[1],e[3])
    # glVertex(e[1],e[2])
    # glVertex(e[0],e[2])
    
    # glEnd()

    # #super sumo
    # glColor3ub(255,0,0)
    # glLineWidth(2.0)
    # glBegin(GL_LINE_STRIP)

    # glVertex(d[0],d[2])
    # glVertex(d[0],d[3])
    # glVertex(d[1],d[3])
    # glVertex(d[1],d[2])
    # glVertex(d[0],d[2])

    # glVertex(e[0],e[2])
    # glVertex(e[0],e[3])
    # glVertex(e[1],e[3])
    # glVertex(e[1],e[2])
    # glVertex(e[0],e[2])
    
    # glEnd()

    # glutSwapBuffers()
    # # print(b)
    # # print(c)
    # # print(d)


def iterate():
    glViewport(0, 20, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global point
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glClearColor(0.4, 0.2, 0.0, 1.0)
    if menu1 :
        draw_image(load_texture('game1/1.png'), 0, 0, w, h)
    if menu2 : 
        allitem()
    if menu3 : 
        draw_image(load_texture('game1/4.png'), 0, 0, w, h)
        draw_text(f"{point}", 480 - (len(f"{point}")*10), 250)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(200, 0)
wind = glutCreateWindow("SUMO ARENA")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mainsumo.mySpecialKeyboard)
glutMouseFunc(input_mouse)
glutMainLoop() 

