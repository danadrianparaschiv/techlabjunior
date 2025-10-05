# Squirrel Eat Squirrel (o clonă 2D Katamari Damacy)
# De Al Sweigart [email protected]
# http://inventwithpython.com/pygame
# Creative Commons BY-NC-SA 3.0 US

import random, sys, time, math, pygame
from pygame.locals import *

FPS = 30  # cadre pe secundă pentru actualizarea ecranului
WINWIDTH = 640  # lățimea ferestrei programului, în pixeli
WINHEIGHT = 480  # înălțimea în pixeli
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

GRASSCOLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

CAMERASLACK = 90  # cât de departe de centru se mișcă veverița înainte de a mișca camera
MOVERATE = 9  # cât de repede se mișcă jucătorul
BOUNCERATE = 6  # cât de repede sare jucătorul (mai mare este mai încet)
BOUNCEHEIGHT = 30  # cât de sus sare jucătorul
STARTSIZE = 25  # cât de mare începe jucătorul
WINSIZE = 300  # cât de mare trebuie să fie jucătorul pentru a câștiga
INVULNTIME = 2  # cât timp este invulnerabil jucătorul după ce este lovit în secunde
GAMEOVERTIME = 4  # cât timp rămâne textul "game over" pe ecran în secunde
MAXHEALTH = 3  # câtă viață are jucătorul la început

NUMGRASS = 80  # numărul de obiecte de iarbă în zona activă
NUMSQUIRRELS = 30  # numărul de veverițe în zona activă
SQUIRRELMINSPEED = 3  # viteza minimă a veveriței
SQUIRRELMAXSPEED = 7  # viteza maximă a veveriței
DIRCHANGEFREQ = 2  # % șansă de schimbare a direcției per cadru
LEFT = 'left'
RIGHT = 'right'

"""
Acest program are trei structuri de date pentru a reprezenta jucătorul, 
veverițele inamice și obiectele de fundal cu iarbă. Structurile de date 
sunt dicționare cu următoarele chei:

Chei folosite de toate cele trei structuri de date:
'x' - coordonata marginii stângi a obiectului în lumea jocului 
      (nu o coordonată în pixeli pe ecran)
'y' - coordonata marginii de sus a obiectului în lumea jocului 
      (nu o coordonată în pixeli pe ecran)
'rect' - obiectul pygame.Rect care reprezintă unde pe ecran se află obiectul.

Chei ale structurii de date a jucătorului:
'surface' - obiectul pygame.Surface care stochează imaginea veveriței 
            care va fi desenată pe ecran.
'facing' - setat fie la LEFT sau RIGHT, stochează în ce direcție se uită jucătorul.
'size' - lățimea și înălțimea jucătorului în pixeli. 
         (Lățimea și înălțimea sunt întotdeauna aceleași.)
'bounce' - reprezintă în ce punct al unei sărituri se află jucătorul. 
           0 înseamnă în picioare (fără săritură), până la BOUNCERATE 
           (finalizarea sărituri)
'health' - un întreg care arată de câte ori mai poate fi lovit jucătorul 
           de o veveriță mai mare înainte de a muri.

Chei ale structurii de date a veveriței inamice:
'surface' - obiectul pygame.Surface care stochează imaginea veveriței 
            care va fi desenată pe ecran.
'movex' - câți pixeli pe cadru se mișcă veverița pe orizontală. 
          Un întreg negativ se mișcă spre stânga, unul pozitiv spre dreapta.
'movey' - câți pixeli pe cadru se mișcă veverița pe verticală. 
          Un întreg negativ se mișcă în sus, unul pozitiv în jos.
'width' - lățimea imaginii veveriței, în pixeli
'height' - înălțimea imaginii veveriței, în pixeli
'bounce' - reprezintă în ce punct al unei sărituri se află jucătorul. 
           0 înseamnă în picioare (fără săritură), până la BOUNCERATE 
           (finalizarea sărituri)
'bouncerate' - cât de repede sare veverița. Un număr mai mic înseamnă 
               o săritură mai rapidă.
'bounceheight' - cât de sus (în pixeli) sare veverița

Chei ale structurii de date a ierbii:
'grassImage' - un întreg care se referă la indexul obiectului pygame.Surface 
               în GRASSIMAGES folosit pentru acest obiect de iarbă
"""

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Squirrel Eat Squirrel')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # încarcă fișierele imagine
    L_SQUIR_IMG = pygame.image.load('squirrel.png')
    R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)
    GRASSIMAGES = []
    for i in range(1, 5):
        GRASSIMAGES.append(pygame.image.load('grass%s.png' % i))

    while True:
        runGame()


def runGame():
    # configurează variabilele pentru începutul unui joc nou
    invulnerableMode = False  # dacă jucătorul este invulnerabil
    invulnerableStartTime = 0  # timpul când jucătorul a devenit invulnerabil
    gameOverMode = False  # dacă jucătorul a pierdut
    gameOverStartTime = 0  # timpul când jucătorul a pierdut
    winMode = False  # dacă jucătorul a câștigat

    # creează suprafețele pentru a stoca textul jocului
    gameOverSurf = BASICFONT.render('Game Over', True, WHITE)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    winSurf = BASICFONT.render('You have achieved OMEGA SQUIRREL!', True, WHITE)
    winRect = winSurf.get_rect()
    winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    winSurf2 = BASICFONT.render('(Press "r" to restart.)', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect2.center = (HALF_WINWIDTH, HALF_WINHEIGHT + 30)

    # camerax și cameray sunt unde este mijlocul vizualizării camerei
    camerax = 0
    cameray = 0

    grassObjs = []  # stochează toate obiectele de iarbă din joc
    squirrelObjs = []  # stochează toate obiectele veveriță non-jucător
    # stochează obiectul jucător:
    playerObj = {'surface': pygame.transform.scale(L_SQUIR_IMG, (STARTSIZE, STARTSIZE)),
                'facing': LEFT,
                'size': STARTSIZE,
                'x': HALF_WINWIDTH,
                'y': HALF_WINHEIGHT,
                'bounce':0,
                'health': MAXHEALTH}

    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    # începe cu câteva imagini aleatorii de iarbă pe ecran
    for i in range(10):
        grassObjs.append(makeNewGrass(camerax, cameray))
        grassObjs[i]['x'] = random.randint(0, WINWIDTH)
        grassObjs[i]['y'] = random.randint(0, WINHEIGHT)

    while True:  # bucla principală a jocului
        # Verifică dacă ar trebui să dezactivăm invulnerabilitatea
        if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
            invulnerableMode = False

        # mișcă toate veverițele
        for sObj in squirrelObjs:
            # mișcă veverița și ajustează pentru săritura lor
            sObj['x'] += sObj['movex']
            sObj['y'] += sObj['movey']
            sObj['bounce'] += 1
            if sObj['bounce'] > sObj['bouncerate']:
                sObj['bounce'] = 0  # resetează cantitatea de săritură

            # șansă aleatorie să schimbe direcția
            if random.randint(0, 99) < DIRCHANGEFREQ:
                sObj['movex'] = getRandomVelocity()
                sObj['movey'] = getRandomVelocity()
                if sObj['movex'] > 0:  # se uită spre dreapta
                    sObj['surface'] = pygame.transform.scale(R_SQUIR_IMG, (sObj['width'], sObj['height']))
                else:  # se uită spre stânga
                    sObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (sObj['width'], sObj['height']))

        # trece prin toate obiectele și vezi dacă trebuie șters vreunul.
        for i in range(len(grassObjs) - 1, -1, -1):
            if isOutsideActiveArea(camerax, cameray, grassObjs[i]):
                del grassObjs[i]
        for i in range(len(squirrelObjs) - 1, -1, -1):
            if isOutsideActiveArea(camerax, cameray, squirrelObjs[i]):
                del squirrelObjs[i]

        # adaugă mai multă iarbă și veverițe dacă nu avem suficiente.
        while len(grassObjs) < NUMGRASS:
            grassObjs.append(makeNewGrass(camerax, cameray))
        while len(squirrelObjs) < NUMSQUIRRELS:
            squirrelObjs.append(makeNewSquirrel(camerax, cameray))

        # ajustează camerax și cameray dacă depășește "camera slack"
        playerCenterx = playerObj['x'] + int(playerObj['size'] / 2)
        playerCentery = playerObj['y'] + int(playerObj['size'] / 2)
        if (camerax + HALF_WINWIDTH) - playerCenterx > CAMERASLACK:
            camerax = playerCenterx + CAMERASLACK - HALF_WINWIDTH
        elif playerCenterx - (camerax + HALF_WINWIDTH) > CAMERASLACK:
            camerax = playerCenterx - CAMERASLACK - HALF_WINWIDTH
        if (cameray + HALF_WINHEIGHT) - playerCentery > CAMERASLACK:
            cameray = playerCentery + CAMERASLACK - HALF_WINHEIGHT
        elif playerCentery - (cameray + HALF_WINHEIGHT) > CAMERASLACK:
            cameray = playerCentery - CAMERASLACK - HALF_WINHEIGHT

        # desenează fundalul verde
        DISPLAYSURF.fill(GRASSCOLOR)

        # desenează toate obiectele de iarbă pe ecran
        for gObj in grassObjs:
            gRect = pygame.Rect((gObj['x'] - camerax,
                                gObj['y'] - cameray,
                                gObj['width'],
                                gObj['height']))
            DISPLAYSURF.blit(GRASSIMAGES[gObj['grassImage']], gRect)

        # desenează celelalte veverițe
        for sObj in squirrelObjs:
            sObj['rect'] = pygame.Rect((sObj['x'] - camerax,
                                       sObj['y'] - cameray - getBounceAmount(sObj['bounce'], sObj['bouncerate'], sObj['bounceheight']),
                                       sObj['width'],
                                       sObj['height']))
            DISPLAYSURF.blit(sObj['surface'], sObj['rect'])

        # desenează veverița jucătorului
        flashIsOn = round(time.time(), 1) * 10 % 2 == 1
        if not gameOverMode and not (invulnerableMode and flashIsOn):
            playerObj['rect'] = pygame.Rect((playerObj['x'] - camerax,
                                            playerObj['y'] - cameray - getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT),
                                            playerObj['size'],
                                            playerObj['size']))
            DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])

        # desenează indicatorul de viață
        drawHealthMeter(playerObj['health'])

        for event in pygame.event.get():  # bucla de gestionare a evenimentelor
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    moveDown = False
                    moveUp = True
                elif event.key in (K_DOWN, K_s):
                    moveUp = False
                    moveDown = True
                elif event.key in (K_LEFT, K_a):
                    moveRight = False
                    moveLeft = True
                    if playerObj['facing'] == RIGHT:  # schimbă imaginea jucătorului
                        playerObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                        playerObj['facing'] = LEFT
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False
                    moveRight = True
                    if playerObj['facing'] == LEFT:  # schimbă imaginea jucătorului
                        playerObj['surface'] = pygame.transform.scale(R_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                        playerObj['facing'] = RIGHT
                elif winMode and event.key == K_r:
                    return

            elif event.type == KEYUP:
                # oprește mișcarea veveriței jucătorului
                if event.key in (K_LEFT, K_a):
                    moveLeft = False
                elif event.key in (K_RIGHT, K_d):
                    moveRight = False
                elif event.key in (K_UP, K_w):
                    moveUp = False
                elif event.key in (K_DOWN, K_s):
                    moveDown = False

                elif event.key == K_ESCAPE:
                    terminate()

        if not gameOverMode:
            # mișcă efectiv jucătorul
            if moveLeft:
                playerObj['x'] -= MOVERATE
            if moveRight:
                playerObj['x'] += MOVERATE
            if moveUp:
                playerObj['y'] -= MOVERATE
            if moveDown:
                playerObj['y'] += MOVERATE

            if (moveLeft or moveRight or moveUp or moveDown) or playerObj['bounce'] != 0:
                playerObj['bounce'] += 1

            if playerObj['bounce'] > BOUNCERATE:
                playerObj['bounce'] = 0  # resetează cantitatea de săritură

            # verifică dacă jucătorul a intrat în coliziune cu vreo veveriță
            for i in range(len(squirrelObjs)-1, -1, -1):
                sqObj = squirrelObjs[i]
                if 'rect' in sqObj and playerObj['rect'].colliderect(sqObj['rect']):
                    # a avut loc o coliziune jucător/veveriță

                    if sqObj['width'] * sqObj['height'] <= playerObj['size']**2:
                        # jucătorul este mai mare și mănâncă veverița
                        playerObj['size'] += int((sqObj['width'] * sqObj['height'])**0.2) + 1
                        del squirrelObjs[i]

                        if playerObj['facing'] == LEFT:
                            playerObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                        if playerObj['facing'] == RIGHT:
                            playerObj['surface'] = pygame.transform.scale(R_SQUIR_IMG, (playerObj['size'], playerObj['size']))

                        if playerObj['size'] > WINSIZE:
                            winMode = True  # activează "modul de câștig"

                    elif not invulnerableMode:
                        # jucătorul este mai mic și ia damage
                        invulnerableMode = True
                        invulnerableStartTime = time.time()
                        playerObj['health'] -= 1
                        if playerObj['health'] == 0:
                            gameOverMode = True  # activează "modul game over"
                            gameOverStartTime = time.time()
        else:
            # jocul s-a terminat, arată textul "game over"
            DISPLAYSURF.blit(gameOverSurf, gameOverRect)
            if time.time() - gameOverStartTime > GAMEOVERTIME:
                return  # încheie jocul curent

        # verifică dacă jucătorul a câștigat.
        if winMode:
            DISPLAYSURF.blit(winSurf, winRect)
            DISPLAYSURF.blit(winSurf2, winRect2)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawHealthMeter(currentHealth):
    for i in range(currentHealth):  # desenează barele de viață roșii
        pygame.draw.rect(DISPLAYSURF, RED, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10))
    for i in range(MAXHEALTH):  # desenează contururile albe
        pygame.draw.rect(DISPLAYSURF, WHITE, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10), 1)


def terminate():
    pygame.quit()
    sys.exit()


def getBounceAmount(currentBounce, bounceRate, bounceHeight):
    # Returnează numărul de pixeli de offset bazat pe săritură.
    # BounceRate mai mare înseamnă o săritură mai lentă.
    # BounceHeight mai mare înseamnă o săritură mai înaltă.
    # currentBounce va fi întotdeauna mai mic decât bounceRate
    return int(math.sin((math.pi / float(bounceRate)) * currentBounce) * bounceHeight)


def getRandomVelocity():
    speed = random.randint(SQUIRRELMINSPEED, SQUIRRELMAXSPEED)
    if random.randint(0, 1) == 0:
        return speed
    else:
        return -speed


def getRandomOffCameraPos(camerax, cameray, objWidth, objHeight):
    # creează un Rect al vizualizării camerei
    cameraRect = pygame.Rect(camerax, cameray, WINWIDTH, WINHEIGHT)
    while True:
        x = random.randint(camerax - WINWIDTH, camerax + (2 * WINWIDTH))
        y = random.randint(cameray - WINHEIGHT, cameray + (2 * WINHEIGHT))
        # creează un obiect Rect cu coordonatele aleatorii și folosește colliderect()
        # pentru a te asigura că marginea dreaptă nu este în vizualizarea camerei.
        objRect = pygame.Rect(x, y, objWidth, objHeight)
        if not objRect.colliderect(cameraRect):
            return x, y


def makeNewSquirrel(camerax, cameray):
    sq = {}
    generalSize = random.randint(5, 25)
    multiplier = random.randint(1, 3)
    sq['width'] = (generalSize + random.randint(0, 10)) * multiplier
    sq['height'] = (generalSize + random.randint(0, 10)) * multiplier
    sq['x'], sq['y'] = getRandomOffCameraPos(camerax, cameray, sq['width'], sq['height'])
    sq['movex'] = getRandomVelocity()
    sq['movey'] = getRandomVelocity()
    if sq['movex'] < 0:  # veverița se uită spre stânga
        sq['surface'] = pygame.transform.scale(L_SQUIR_IMG, (sq['width'], sq['height']))
    else:  # veverița se uită spre dreapta
        sq['surface'] = pygame.transform.scale(R_SQUIR_IMG, (sq['width'], sq['height']))
    sq['bounce'] = 0
    sq['bouncerate'] = random.randint(10, 18)
    sq['bounceheight'] = random.randint(10, 50)
    return sq


def makeNewGrass(camerax, cameray):
    gr = {}
    gr['grassImage'] = random.randint(0, len(GRASSIMAGES) - 1)
    gr['width'] = GRASSIMAGES[0].get_width()
    gr['height'] = GRASSIMAGES[0].get_height()
    gr['x'], gr['y'] = getRandomOffCameraPos(camerax, cameray, gr['width'], gr['height'])
    gr['rect'] = pygame.Rect((gr['x'], gr['y'], gr['width'], gr['height']))
    return gr


def isOutsideActiveArea(camerax, cameray, obj):
    # Returnează False dacă camerax și cameray sunt mai mult de
    # o jumătate de lungime a ferestrei dincolo de marginea ferestrei.
    boundsLeftEdge = camerax - WINWIDTH
    boundsTopEdge = cameray - WINHEIGHT
    boundsRect = pygame.Rect(boundsLeftEdge, boundsTopEdge, WINWIDTH * 3, WINHEIGHT * 3)
    objRect = pygame.Rect(obj['x'], obj['y'], obj['width'], obj['height'])
    return not boundsRect.colliderect(objRect)


if __name__ == '__main__':
    main()
