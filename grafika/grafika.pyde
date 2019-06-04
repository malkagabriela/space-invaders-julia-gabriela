#space invaders

def setup():
    size(700,550)
    background(30,50,125,235)
    global i
    global img
    global gracz
    global imgc
    global imgz
    global nazwa
    global nazwa2
    global nazwa3
    global nazwa4
    global nazwa5
    global ext
    nazwa = "wrog1"
    nazwa2 = "wrog2"
    nazwa3 = "gracz"
    nazwa4 = "pociskc"
    nazwa5 = "pociskz"
    ext = ".png"
    i = loadImage(nazwa+ext)
    image(i, 10, 10, 35, 35)
    img = loadImage(nazwa2+ext)
    image(img, 10, 10, 35, 35)
    gracz = loadImage(nazwa3+ext)
    image(gracz, 320, 450, 60, 60)
    imgc = loadImage(nazwa4+ext)
    image(imgc, 10, 10, 60, 60)
    imgz = loadImage(nazwa5+ext)
    image(imgz, 10, 10, 65, 65)
    
def draw():
    global i
    global img
    global gracz
    global imgc
    global imgz
    global nazwa
    global nazwa2
    global nazwa3
    global nazwa4
    global nazwa5
    global ext
