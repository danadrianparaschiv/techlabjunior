# Capitolul 8 – Veverița Mănâncă Veveriță

Veverița Mănâncă Veveriță este bazat vag pe jocul "Katamari Damacy". Jucătorul controlează o veveriță mică care trebuie să sară pe ecran mâncând veverițe mai mici și evitând veverițele mai mari. De fiecare dată când veverița jucătorului mănâncă o veveriță mai mică decât ea, crește mai mare. Dacă veverița jucătorului este lovită de o veveriță mai mare, pierde un punct de viață. Jucătorul câștigă când veverița devine o veveriță monstruos de mare numită Veverița Omega. Jucătorul pierde dacă veverița sa este lovită de trei ori.

Nu știu exact de unde mi-a venit ideea unui joc video în care veverițele se mănâncă între ele. Sunt puțin ciudat uneori.

Există trei tipuri de structuri de date în acest joc, care sunt reprezentate ca valori de dicționar. Tipurile sunt veverițele jucătorului, veverițele inamice și obiectele de iarbă. Există un singur obiect veveriță jucător la un moment dat în joc.

**Notă:** Tehnic, "obiect" înseamnă ceva specific în Programarea Orientată pe Obiecte. Python are caracteristici OOP, dar acestea nu sunt acoperite în această carte. Tehnic, obiectele Pygame precum "obiectul Rect" sau "obiectul Surface" sunt obiecte. Dar voi folosi termenul "obiect" în această carte pentru a se referi la "lucruri care există în lumea jocului". Dar de fapt, veverița jucătorului, veverițele inamice și "obiectele" de iarbă sunt doar valori de dicționar.

Toate obiectele au următoarele chei în valoarea lor de dicționar: `'x'`, `'y'` și `'rect'`. Valorile cheilor `'x'` și `'y'` oferă coordonatele din colțul stânga sus al obiectului în coordonatele lumii jocului. Acestea sunt diferite de coordonatele în pixeli (care este ceea ce urmărește valoarea cheii `'rect'`). Diferența dintre lumea jocului și coordonatele în pixeli va fi explicată când vei învăța despre conceptul de camere.

În plus, veverița jucătorului, veverița inamică și obiectele de iarbă au alte chei care sunt explicate într-un comentariu mare la începutul codului sursă.

Acest cod sursă poate fi descărcat de la http://invpy.com/squirrel.py.

Dacă primești mesaje de eroare, verifică numărul liniei menționat în mesajul de eroare și verifică codul pentru greșeli de tastare. De asemenea, poți copia și lipi codul în formularul web de la http://invpy.com/diff/squirrel pentru a vedea diferențele dintre codul tău și codul din carte.

Va trebui să descarci și următoarele fișiere imagine:
- http://invpy.com/gameicon.png
- http://invpy.com/squirrel.png

## Codul sursă complet

```python
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
```

## Explicarea codului

### Constantele

Începutul programului atribuie mai multe variabile constante. Acest program folosește frecvent jumătatea lungimii lățimii și înălțimii ferestrei, astfel încât variabilele `HALF_WINWIDTH` și `HALF_WINHEIGHT` stochează aceste numere.

**CAMERASLACK** = 90 înseamnă că camera va începe să urmărească veverița jucătorului când se mișcă la 90 de pixeli depărtare de centrul ferestrei.

Comentariile de lângă aceste constante explică pentru ce este folosită fiecare variabilă constantă.

### Structurile de date

Comentariile de la liniile 37-61 sunt într-un șir mare, multi-linie. Ele descriu cheile din obiectele veveriță jucător, veveriță inamică și iarbă. În Python, o valoare de șir multi-linie de sine stătătoare funcționează ca un comentariu multi-linie.

### Funcția main()

Primele câteva linii ale funcției `main()` sunt același cod de configurare pe care l-am văzut în programele noastre anterioare de jocuri. Funcția `pygame.display.set_icon()` este o funcție Pygame care setează iconița în bara de titlu a ferestrei (la fel cum `pygame.display.set_caption()` setează textul caption în bara de titlu).

### Încărcarea imaginilor

Imaginea pentru jucător și veverițele inamice este încărcată din `squirrel.png`. Asigură-te că acest fișier PNG este în același folder cu `squirrel.py`, altfel vei primi eroarea `pygame.error: Couldn't open squirrel.png`.

Funcția `pygame.transform.flip()` primește trei parametri: obiectul Surface cu imaginea de inversat, o valoare Boolean pentru o inversare orizontală și o valoare Boolean pentru o inversare verticală. Prin trecerea `True` pentru al doilea parametru și `False` pentru al treilea parametru, obiectul Surface care returnează are imaginea veveriței îndreptată spre dreapta.

### Camera în joc

Variabilele `camerax` și `cameray` urmăresc coordonatele jocului ale "camerei". Imaginează-ți lumea jocului ca un spațiu 2D infinit. Aceasta, desigur, nu ar putea încăpea niciodată pe niciun ecran. Putem desena doar o porțiune din spațiul 2D infinit pe ecran. Numim zona acestei porțiuni o cameră, pentru că este ca și cum ecranul nostru ar fi doar zona lumii jocului în fața a ceea ce ar vedea o cameră.

Coordonatele lumii jocului continuă să crească și să scadă pentru totdeauna. Originea lumii jocului este unde sunt coordonatele lumii jocului (0, 0).

Dar putem afișa doar o zonă de 640 x 480 de pixeli pe ecran (deși acest lucru se poate schimba dacă trecem numere diferite la funcția `pygame.display.set_mode()`), așa că trebuie să urmărim unde este localizată originea camerei în coordonatele lumii jocului.

### Zona activă

"Zona activă" este doar un nume pe care l-am inventat pentru a descrie zona lumii jocului pe care o vizualizează camera plus o zonă în jurul acesteia de dimensiunea zonei camerei.

Când creăm noi obiecte veveriță inamică sau iarbă, nu vrem să fie create în interiorul vizualizării camerei, deoarece va părea că apar din nicăieri.

Dar nici nu vrem să le creăm prea departe de cameră, pentru că atunci este posibil să nu ajungă niciodată în vizualizarea camerei. În interiorul zonei active dar în afara camerei este locul unde obiectele veveriță și iarbă pot fi create în siguranță.

De asemenea, când obiectele veveriță și iarbă sunt dincolo de granița zonei active, atunci sunt suficient de departe pentru a fi șterse astfel încât să nu mai consume memorie. Obiectele atât de departe nu sunt necesare deoarece este mult mai puțin probabil să revină în vizualizarea camerei.

### Când ștergi elemente dintr-o listă, iterează peste listă în sens invers

În timpul fiecărei iterații a buclei de joc, codul va verifica toate obiectele de iarbă și veveriță inamică pentru a vedea dacă se află în afara "zonei active". Funcția `isOutsideActiveArea()` primește coordonatele curente ale camerei (care sunt stocate în `camerax` și `cameray`) și obiectul de iarbă/veveriță inamică, și returnează `True` dacă obiectul nu este localizat în zona activă.

Dacă acesta este cazul, acest obiect este șters. Ștergerea obiectelor veveriță și iarbă se face cu operatorul `del`. Cu toate acestea, observă că bucla `for` trece argumente la funcția `range()` astfel încât numerotarea începe la indexul ultimului element și apoi decrementează cu -1 (spre deosebire de incrementarea cu 1 așa cum o face în mod normal) până când ajunge la numărul -1. Iterăm înapoi peste indexurile listei comparativ cu cum se face în mod normal. Acest lucru se face pentru că iterăm peste lista din care ștergem și elemente.

Pentru a vedea de ce este necesară această ordine inversă, să spunem că avem următoarea valoare de listă:

```python
animals = ['cat', 'mouse', 'dog', 'horse']
```

Dacă am dori să scriem cod pentru a șterge orice instanțe ale șirului `'dog'` din această listă, am putea gândi să scriem cod ca acesta:

```python
for i in range(len(animals)):
    if animals[i] == 'dog':
        del animals[i]
```

Dar dacă am rula acest cod, am primi o eroare `IndexError` care arată astfel:

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range
```

Pentru a vedea de ce apare această eroare, să parcurgem codul. Mai întâi, lista `animals` ar fi setată la `['cat', 'mouse', 'dog', 'horse']` și `len(animals)` ar returna 4. Aceasta înseamnă că apelul la `range(4)` ar face ca bucla `for` să itereze cu valorile 0, 1, 2 și 3.

Când bucla `for` iterează cu `i` setat la 2, condiția instrucțiunii `if` va fi `True` și instrucțiunea `del animals[i]` va șterge `animals[2]`. Aceasta înseamnă că după aceea lista `animals` va fi `['cat', 'mouse', 'horse']`. Indexurile tuturor elementelor după `'dog'` sunt toate mutate în jos cu unul deoarece valoarea `'dog'` a fost eliminată.

Dar la următoarea iterație prin bucla `for`, `i` este setat la 3. Dar `animals[3]` este în afara limitelor deoarece indexurile valide ale listei `animals` nu mai sunt 0 până la 3 ci 0 până la 2. Apelul original la `range()` a fost pentru o listă cu 4 elemente în ea. Lista s-a schimbat în lungime, dar bucla `for` este configurată pentru lungimea originală.

Cu toate acestea, dacă iterăm de la ultimul index al listei la 0, nu întâmpinăm această problemă. Următorul program șterge șirul `'dog'` din lista `animals` fără a cauza o eroare `IndexError`:

```python
animals = ['cat', 'mouse', 'dog', 'horse']
for i in range(len(animals) - 1, -1, -1):
    if animals[i] == 'dog':
        del animals[i]
```

Motivul pentru care acest cod nu cauzează o eroare este că bucla `for` iterează peste 3, 2, 1 și 0. La prima iterație, codul verifică dacă `animals[3]` este egal cu `'dog'`. Nu este (animals[3] este `'horse'`) astfel că codul trece la următoarea iterație. Apoi `animals[2]` este verificat dacă este egal cu `'dog'`. Este, așa că `animals[2]` este șters.

După ce `animals[2]` este șters, lista `animals` este setată la `['cat', 'mouse', 'horse']`. La următoarea iterație, `i` este setat la 1. Există o valoare la `animals[1]` (valoarea `'mouse'`), așa că nu este cauzată nicio eroare. Nu contează că toate elementele din listă după `'dog'` au fost mutate în jos cu unul, deoarece din moment ce am început de la sfârșitul listei și mergem spre față, toate acele elemente au fost deja verificate.

În mod similar, putem șterge obiectele de iarbă și veveriță din listele `grassObjs` și `squirrelObjs` fără eroare deoarece bucla `for` iterează în ordine inversă.

### Adăugarea de noi obiecte

Constantele `NUMGRASS` și `NUMSQUIRRELS` au fost setate la 80 și respectiv 30 la începutul programului. Aceste variabile sunt setate astfel încât să fim siguri că există întotdeauna destule obiecte de iarbă și veveriță în zona activă în orice moment. Dacă lungimea `grassObjs` sau `squirrelObjs` scade sub `NUMGRASS` sau `NUMSQUIRRELS` respectiv, atunci sunt create noi obiecte de iarbă și veveriță.

### Camera Slack

Poziția camerei (care este stocată ca întregi în variabilele `camerax` și `cameray`) trebuie actualizată când jucătorul se mișcă. Am numit numărul de pixeli cu care jucătorul se poate mișca înainte ca camera să fie actualizată "camera slack". CAMERASLACK a fost setată la 90, ceea ce programul nostru va considera că înseamnă că veverița jucătorului se poate mișca 90 de pixeli de la centru înainte ca poziția camerei să fie actualizată pentru a urma veverița.

Pentru a înțelege ecuațiile folosite în instrucțiunile `if`, ar trebui să observi că `(camerax + HALF_WINWIDTH)` și `(cameray + HALF_WINHEIGHT)` sunt coordonatele XY ale lumii jocului aflate în prezent în centrul ecranului. `playerCenterx` și `playerCentery` sunt setate la mijlocul poziției veveriței jucătorului, de asemenea în coordonatele lumii jocului.

### Desenarea pe ecran

Bucla `for` care desenează toate obiectele de iarbă pe ecran este similară cu bucla `for` precedentă, cu excepția faptului că obiectul `Rect` pe care îl creează este salvat în valoarea cheii `'rect'` a dicționarului veveriță. Motivul pentru care codul face acest lucru este că vom folosi acest obiect `Rect` mai târziu pentru a verifica dacă veverițele inamice au intrat în coliziune cu veverița jucătorului.

### Efectul de clipire

Când jucătorul se ciocnește cu o veveriță inamică mai mare, jucătorul ia damage și clipește puțin pentru a indica că jucătorul este temporar invulnerabil. Acest efect de clipire se face prin desenarea veveriței jucătorului la unele iterații prin bucla de joc dar nu și la altele.

Veverița jucătorului va fi desenată la iterațiile buclei de joc pentru o zecime de secundă, și apoi nu va fi desenată la iterațiile buclei de joc pentru o zecime de secundă. Acest lucru se repetă iar și iar atâta timp cât jucătorul este invulnerabil.

### Gestionarea evenimentelor

Codul pentru gestionarea evenimentelor de tastatură este similar cu cel din jocurile anterioare. Când sunt apăsate tastele săgeată sau echivalentele lor WASD, variabilele de mișcare sunt actualizate corespunzător.

### Detectarea coliziunilor

Bucla `for` va rula cod pe fiecare dintre obiectele de joc veveriță inamică din `squirrelObjs`. Observă că parametrii la `range()` încep la ultimul index al `squirrelObjs` și decrementează. Acest lucru se face pentru că codul din interiorul acestei bucle `for` poate ajunge să șteargă unele dintre aceste obiecte de joc veveriță inamică (dacă veverița jucătorului ajunge să le mănânce).

Dacă veverița jucătorului este egală sau mai mare decât dimensiunea veveriței inamice cu care s-a ciocnit, atunci veverița jucătorului va mânca acea veveriță și va crește. Numărul care este adăugat la cheia `'size'` în obiectul jucător (adică creșterea) este calculat pe baza dimensiunii veveriței inamice.

### Funcția getBounceAmount()

Există o funcție matematică (care este similară funcțiilor în programare prin faptul că ambele "returnează" sau "evaluează" la un număr bazat pe parametrii lor) numită sinus (pronunțat "sain" și adesea abreviat ca "sin"). Python are această funcție matematică ca o funcție Python în modulul `math`.

Funcția sinus este un concept din matematica trigonometrică. Dacă vrei să înveți mai multe despre unda sinusoidală, pagina Wikipedia are informații detaliate.

Motivul pentru care apelăm `float()` pentru a converti `bounceRate` într-un număr cu virgulă mobilă este pur și simplu pentru ca acest program să funcționeze în Python versiunea 2. În Python versiunea 3, operatorul de împărțire va evalua la o valoare cu virgulă mobilă chiar dacă ambii operanzi sunt întregi.

Făcând aceste modificări astfel încât codul nostru să funcționeze cu versiuni mai vechi de software se numește compatibilitate retroactivă. Este important să menținem compatibilitatea retroactivă, deoarece nu toată lumea va rula întotdeauna cea mai recentă versiune de software și vrei să te asiguri că codul pe care îl scrii funcționează cu cât mai multe calculatoare posibil.

### Funcția getRandomVelocity()

Funcția `getRandomVelocity()` este folosită pentru a determina aleatoriu cât de repede se va mișca o veveriță inamică. Intervalul acestei viteze este setat în constantele `SQUIRRELMINSPEED` și `SQUIRRELMAXSPEED`, dar pe lângă asta, viteza este fie negativă (indicând că veverița merge la stânga sau sus) fie pozitivă (indicând că veverița merge la dreapta sau jos). Există o șansă de cincizeci-cincizeci ca viteza aleatorie să fie pozitivă sau negativă.

### Funcția getRandomOffCameraPos()

Când un nou obiect veveriță sau iarbă este creat în lumea jocului, vrem ca acesta să fie în zona activă (astfel încât să fie aproape de veverița jucătorului) dar nu în vizualizarea camerei (astfel încât să nu apară brusc în existență pe ecran). Pentru a face asta, creăm un obiect `Rect` care reprezintă zona camerei.

Apoi, generăm aleatoriu numere pentru coordonatele XY care ar fi în zona activă. Zona activă are marginea stângă și de sus la `WINWIDTH` și `WINHEIGHT` pixeli la stânga și sus de `camerax` și `cameray`. Deci marginea stângă și de sus a zonei active sunt la `camerax - WINWIDTH` și `cameray - WINHEIGHT`.

### Funcția makeNewSquirrel()

Crearea obiectelor de joc veveriță inamică este similară cu crearea obiectelor de joc iarbă. Datele pentru fiecare veveriță inamică sunt de asemenea stocate într-un dicționar. Lățimea și înălțimea sunt setate la dimensiuni aleatorii. Variabila `generalSize` este folosită astfel încât lățimea și înălțimea fiecărei veverițe să nu fie prea diferite una de cealaltă.

Poziția XY originală a veveriței va fi o locație aleatorie pe care camera nu o poate vedea, pentru a preveni veverițele să "apară" brusc în existență pe ecran.

Viteza și direcția sunt de asemenea selectate aleatoriu de funcția `getRandomVelocity()`.

### Funcția makeNewGrass()

Obiectele de joc iarbă sunt dicționare cu cheile obișnuite `'x'`, `'y'`, `'width'`, `'height'` și `'rect'` dar și o cheie `'grassImage'` care este un număr de la 0 la unul mai puțin decât lungimea listei `GRASSIMAGES`. Acest număr va determina ce imagine are obiectul de joc iarbă.

### Funcția isOutsideActiveArea()

Funcția `isOutsideActiveArea()` va returna `True` dacă obiectul pe care îl transmiți este în afara "zonei active" care este dictată de parametrii `camerax` și `cameray`.

Putem crea un obiect `Rect` care reprezintă zona activă trecând `camerax - WINWIDTH` pentru valoarea marginii stângi și `cameray - WINHEIGHT` pentru valoarea marginii de sus, și apoi `WINWIDTH * 3` și `WINHEIGHT * 3` pentru lățime și înălțime. Odată ce avem zona activă reprezentată ca un obiect `Rect`, putem folosi metoda `colliderect()` pentru a determina dacă obiectul din parametrul `obj` se ciocnește cu (adică, este în interiorul) obiectului `Rect` al zonei active.

Deoarece veverița jucătorului, veverițele inamice și obiectele de iarbă au toate cheile `'x'`, `'y'`, `'width'` și `'height'`, codul `isOutsideActiveArea()` poate funcționa cu oricare tip dintre aceste obiecte de joc.

## Rezumat

Veverița Mănâncă Veveriță a fost primul nostru joc care a avut mai mulți inamici mișcându-se prin joc simultan. Cheia pentru a avea mai mulți inamici a fost utilizarea unei valori de dicționar cu chei identice pentru fiecare veveriță inamică, astfel încât același cod să poată fi rulat pe fiecare dintre ele în timpul unei iterații prin bucla de joc.

Conceptul de cameră a fost de asemenea introdus. Camerele nu erau necesare pentru jocurile noastre anterioare deoarece întreaga lume a jocului încăpea pe un singur ecran. Cu toate acestea, când faci propriile tale jocuri care implică un jucător mișcându-se printr-o lume de joc mare, vei avea nevoie de cod pentru a gestiona conversia între sistemul de coordonate al lumii jocului și sistemul de coordonate în pixeli al ecranului.

În cele din urmă, funcția matematică sinus a fost introdusă pentru a oferi sărituri realiste ale veveriței (indiferent de cât de înalte sau lungi erau fiecare săritură). Nu trebuie să știi multă matematică pentru a face programare. În majoritatea cazurilor, doar să știi adunare, înmulțire și numere negative este suficient. Cu toate acestea, dacă studiezi matematica, vei găsi adesea mai multe utilizări pentru matematică pentru a face jocurile tale mai cool.

Pentru practică suplimentară de programare, poți descărca versiuni cu bug-uri ale Veverița Mănâncă Veveriță de la http://invpy.com/buggy/squirrel și poți încerca să descoperi cum să remediezi bug-urile.
