# Capitolul 9 – Împinge Stelele

Star Pusher este o clonă a jocului Sokoban sau "Box Pusher" (Împingător de cutii). Jucătorul se află într-o cameră cu mai multe stele. Există marcaje de stele pe podeaua unor sprite-uri de dale din cameră. Jucătorul trebuie să-și dea seama cum să împingă stelele deasupra dalelor cu marcaje de stele. Jucătorul nu poate împinge o stea dacă există un perete sau o altă stea în spatele ei. Jucătorul nu poate trage stele, deci dacă o stea este împinsă într-un colț, jucătorul va trebui să repornească nivelul. Când toate stelele au fost împinse pe dalele de podea marcate cu stele, nivelul este complet și începe următorul nivel.

Fiecare nivel este format dintr-o grilă 2D de imagini de dale. Sprite-urile de dale sunt imagini de aceeași dimensiune care pot fi plasate una lângă alta pentru a forma imagini mai complexe. Cu câteva dale de podea și perete, putem crea niveluri de multe forme și dimensiuni interesante.

## Fișierele necesare

Fișierele de nivel nu sunt incluse în codul sursă. În schimb, poți fie să creezi fișierele de nivel singur, fie să le descarci. Un fișier de nivel cu 201 niveluri poate fi descărcat de la http://invpy.com/starPusherLevels.txt.

Când rulezi programul Star Pusher, asigură-te că acest fișier de nivel se află în același folder cu fișierul `starpusher.py`. Altfel vei primi acest mesaj de eroare: `AssertionError: Cannot find the level file: starPusherLevels.txt`

Designurile nivelelor au fost create original de David W. Skinner. Poți descărca mai multe puzzle-uri de pe site-ul său la http://sneezingtiger.com/sokoban/levels.html.

### Descărcări

- Codul sursă: http://invpy.com/starpusher.py
- Fișierul de niveluri: http://invpy.com/starPusherLevels.txt
- Imaginile (dale): http://invpy.com/starPusherImages.zip

Dacă primești mesaje de eroare, verifică numărul liniei menționat în mesajul de eroare și verifică codul pentru greșeli de tastare. De asemenea, poți copia și lipi codul în formularul web de la http://invpy.com/diff/starpusher pentru a vedea diferențele dintre codul tău și codul din carte.

> **Notă:** La fel ca "obiectele" veveriță, iarbă și inamic din jocul Veverița Mănâncă Veveriță, când spun "obiecte hartă", "obiecte stare joc" sau "obiecte nivel" în acest capitol, nu mă refer la obiecte în sensul Programării Orientate pe Obiecte. Aceste "obiecte" sunt de fapt doar valori de dicționar, dar este mai ușor să ne referim la ele ca obiecte deoarece reprezintă lucruri din lumea jocului.

## Codul sursă complet

```python
# Star Pusher (o clonă Sokoban)
# De Al Sweigart [email protected]
# http://inventwithpython.com/pygame
# Creative Commons BY-NC-SA 3.0 US

import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30  # cadre pe secundă pentru actualizarea ecranului
WINWIDTH = 800  # lățimea ferestrei programului, în pixeli
WINHEIGHT = 600  # înălțimea în pixeli
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# Lățimea și înălțimea totală a fiecărei dale în pixeli.
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45

CAM_MOVE_SPEED = 5  # câți pixeli pe cadru se mișcă camera

# Procentul de dale exterioare care au decorațiuni
# adiționale pe ele, cum ar fi un copac sau o stâncă.
OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = (0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    # Inițializarea Pygame și configurarea de bază a variabilelor globale.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    # Deoarece obiectul Surface stocat în DISPLAYSURF a fost returnat
    # de funcția pygame.display.set_mode(), acesta este obiectul
    # Surface care este desenat pe ecranul real al computerului
    # când pygame.display.update() este apelat.
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    pygame.display.set_caption('Star Pusher')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    # Un dicționar global care va conține toate obiectele
    # Pygame Surface returnate de pygame.image.load().
    IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
                  'covered goal': pygame.image.load('Selector.png'),
                  'star': pygame.image.load('Star.png'),
                  'corner': pygame.image.load('Wall Block Tall.png'),
                  'wall': pygame.image.load('Wood Block Tall.png'),
                  'inside floor': pygame.image.load('Plain Block.png'),
                  'outside floor': pygame.image.load('Grass Block.png'),
                  'title': pygame.image.load('star_title.png'),
                  'solved': pygame.image.load('star_solved.png'),
                  'princess': pygame.image.load('princess.png'),
                  'boy': pygame.image.load('boy.png'),
                  'catgirl': pygame.image.load('catgirl.png'),
                  'horngirl': pygame.image.load('horngirl.png'),
                  'pinkgirl': pygame.image.load('pinkgirl.png'),
                  'rock': pygame.image.load('Rock.png'),
                  'short tree': pygame.image.load('Tree_Short.png'),
                  'tall tree': pygame.image.load('Tree_Tall.png'),
                  'ugly tree': pygame.image.load('Tree_Ugly.png')}

    # Aceste valori de dicționar sunt globale și mapează caracterul care apare
    # în fișierul de nivel la obiectul Surface pe care îl reprezintă.
    TILEMAPPING = {'x': IMAGESDICT['corner'],
                   '#': IMAGESDICT['wall'],
                   'o': IMAGESDICT['inside floor'],
                   ' ': IMAGESDICT['outside floor']}
    OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                          '2': IMAGESDICT['short tree'],
                          '3': IMAGESDICT['tall tree'],
                          '4': IMAGESDICT['ugly tree']}

    # PLAYERIMAGES este o listă cu toate personajele posibile pe care le poate fi jucătorul.
    # currentImage este indexul imaginii curente a jucătorului.
    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pinkgirl']]

    startScreen()  # arată ecranul de titlu până când utilizatorul apasă o tastă

    # Citește nivelurile din fișierul text. Vezi readLevelsFile() pentru
    # detalii despre formatul acestui fișier și cum să-ți faci propriile niveluri.
    levels = readLevelsFile('starPusherLevels.txt')
    currentLevelIndex = 0

    # Bucla principală a jocului. Această buclă rulează un singur nivel, când utilizatorul
    # termină acel nivel, următorul/precedentul nivel este încărcat.
    while True:  # bucla principală a jocului
        # Rulează nivelul pentru a începe efectiv să joci jocul:
        result = runLevel(levels, currentLevelIndex)

        if result in ('solved', 'next'):
            # Mergi la următorul nivel.
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                # Dacă nu mai sunt niveluri, revino la primul.
                currentLevelIndex = 0
        elif result == 'back':
            # Mergi la nivelul precedent.
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                # Dacă nu există niveluri precedente, mergi la ultimul.
                currentLevelIndex = len(levels) - 1
        elif result == 'reset':
            pass  # Nu face nimic. Bucla re-apelează runLevel() pentru a reseta nivelul


def runLevel(levels, levelNum):
    global currentImage
    levelObj = levels[levelNum]
    mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
    gameStateObj = copy.deepcopy(levelObj['startState'])
    mapNeedsRedraw = True  # setează la True pentru a apela drawMap()
    levelSurf = BASICFONT.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (20, WINHEIGHT - 35)
    mapWidth = len(mapObj) * TILEWIDTH
    mapHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT
    MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH
    MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT

    levelIsComplete = False
    # Urmărește cât s-a mutat camera:
    cameraOffsetX = 0
    cameraOffsetY = 0
    # Urmărește dacă tastele pentru a muta camera sunt ținute apăsate:
    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False

    while True:  # bucla principală a jocului
        # Resetează aceste variabile:
        playerMoveTo = None
        keyPressed = False

        for event in pygame.event.get():  # bucla de gestionare a evenimentelor
            if event.type == QUIT:
                # Jucătorul a dat clic pe "X" din colțul ferestrei.
                terminate()

            elif event.type == KEYDOWN:
                # Gestionează apăsările de taste
                keyPressed = True
                if event.key == K_LEFT:
                    playerMoveTo = LEFT
                elif event.key == K_RIGHT:
                    playerMoveTo = RIGHT
                elif event.key == K_UP:
                    playerMoveTo = UP
                elif event.key == K_DOWN:
                    playerMoveTo = DOWN

                # Setează modul de mișcare a camerei.
                elif event.key == K_a:
                    cameraLeft = True
                elif event.key == K_d:
                    cameraRight = True
                elif event.key == K_w:
                    cameraUp = True
                elif event.key == K_s:
                    cameraDown = True

                elif event.key == K_n:
                    return 'next'
                elif event.key == K_b:
                    return 'back'

                elif event.key == K_ESCAPE:
                    terminate()  # Tasta Esc închide jocul.
                elif event.key == K_BACKSPACE:
                    return 'reset'  # Resetează nivelul.
                elif event.key == K_p:
                    # Schimbă imaginea jucătorului la următoarea.
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        # După ultima imagine a jucătorului, folosește prima.
                        currentImage = 0
                    mapNeedsRedraw = True

            elif event.type == KEYUP:
                # Dezactivează modul de mișcare a camerei.
                if event.key == K_a:
                    cameraLeft = False
                elif event.key == K_d:
                    cameraRight = False
                elif event.key == K_w:
                    cameraUp = False
                elif event.key == K_s:
                    cameraDown = False

        if playerMoveTo != None and not levelIsComplete:
            # Dacă jucătorul a apăsat o tastă pentru a se mișca, fă mișcarea
            # (dacă este posibil) și împinge orice stele care pot fi împinse.
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)

            if moved:
                # incrementează contorul de pași.
                gameStateObj['stepCounter'] += 1
                mapNeedsRedraw = True

            if isLevelFinished(levelObj, gameStateObj):
                # nivelul este rezolvat, ar trebui să arătăm imaginea "Rezolvat!".
                levelIsComplete = True
                keyPressed = False

        DISPLAYSURF.fill(BGCOLOR)

        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])
            mapNeedsRedraw = False

        if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:
            cameraOffsetY += CAM_MOVE_SPEED
        elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:
            cameraOffsetY -= CAM_MOVE_SPEED
        if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:
            cameraOffsetX += CAM_MOVE_SPEED
        elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:
            cameraOffsetX -= CAM_MOVE_SPEED

        # Ajustează obiectul Rect al mapSurf bazat pe offset-ul camerei.
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)

        # Desenează mapSurf pe obiectul Surface DISPLAYSURF.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        DISPLAYSURF.blit(levelSurf, levelRect)
        stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)
        stepRect = stepSurf.get_rect()
        stepRect.bottomleft = (20, WINHEIGHT - 10)
        DISPLAYSURF.blit(stepSurf, stepRect)

        if levelIsComplete:
            # este rezolvat, arată imaginea "Rezolvat!" până când jucătorul
            # a apăsat o tastă.
            solvedRect = IMAGESDICT['solved'].get_rect()
            solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
            DISPLAYSURF.blit(IMAGESDICT['solved'], solvedRect)

            if keyPressed:
                return 'solved'

        pygame.display.update()  # desenează DISPLAYSURF pe ecran.
        FPSCLOCK.tick()


def isWall(mapObj, x, y):
    """Returnează True dacă poziția (x, y) pe
    hartă este un perete, altfel returnează False."""
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False  # x și y nu sunt de fapt pe hartă.
    elif mapObj[x][y] in ('#', 'x'):
        return True  # peretele blochează
    return False


def decorateMap(mapObj, startxy):
    """Face o copie a obiectului hartă dat și îl modifică.
    Iată ce se face cu el:
    * Pereții care sunt colțuri sunt transformați în piese de colț.
    * Se face distincția între dalele de podea exterior/interior.
    * Decorațiunile copac/stâncă sunt adăugate aleatoriu la dalele exterioare.

    Returnează obiectul hartă decorat."""

    startx, starty = startxy  # Zahăr sintactic

    # Copiază obiectul hartă astfel încât să nu modificăm originalul transmis
    mapObjCopy = copy.deepcopy(mapObj)

    # Elimină caracterele non-perete din datele hărții
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):
                mapObjCopy[x][y] = ' '

    # Umple cu flood pentru a determina dalele de podea interior/exterior.
    floodFill(mapObjCopy, startx, starty, ' ', 'o')

    # Convertește pereții adiacenți în dale de colț.
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):

            if mapObjCopy[x][y] == '#':
                if (isWall(mapObjCopy, x, y-1) and isWall(mapObjCopy, x+1, y)) or \
                   (isWall(mapObjCopy, x+1, y) and isWall(mapObjCopy, x, y+1)) or \
                   (isWall(mapObjCopy, x, y+1) and isWall(mapObjCopy, x-1, y)) or \
                   (isWall(mapObjCopy, x-1, y) and isWall(mapObjCopy, x, y-1)):
                    mapObjCopy[x][y] = 'x'

            elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < OUTSIDE_DECORATION_PCT:
                mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))

    return mapObjCopy


def isBlocked(mapObj, gameStateObj, x, y):
    """Returnează True dacă poziția (x, y) pe hartă este
    blocată de un perete sau o stea, altfel returnează False."""

    if isWall(mapObj, x, y):
        return True

    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True  # x și y nu sunt de fapt pe hartă.

    elif (x, y) in gameStateObj['stars']:
        return True  # o stea blochează

    return False


def makeMove(mapObj, gameStateObj, playerMoveTo):
    """Dat fiind un obiect hartă și stare joc, vezi dacă este posibil pentru
    jucător să facă mișcarea dată. Dacă este, atunci schimbă poziția jucătorului
    (și poziția oricărei stele împinse). Dacă nu, nu face nimic.

    Returnează True dacă jucătorul s-a mutat, altfel False."""

    # Asigură-te că jucătorul poate să se miște în direcția dorită.
    playerx, playery = gameStateObj['player']

    # Această variabilă este "zahăr sintactic". A tasta "stars" este mai
    # ușor de citit decât a tasta "gameStateObj['stars']" în codul nostru.
    stars = gameStateObj['stars']

    # Codul pentru gestionarea fiecăreia dintre direcții este atât de asemănător în afară
    # de adăugarea sau scăderea 1 la coordonatele x/y. Putem
    # să-l simplificăm folosind variabilele xOffset și yOffset.
    if playerMoveTo == UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == RIGHT:
        xOffset = 1
        yOffset = 0
    elif playerMoveTo == DOWN:
        xOffset = 0
        yOffset = 1
    elif playerMoveTo == LEFT:
        xOffset = -1
        yOffset = 0

    # Vezi dacă jucătorul poate să se miște în acea direcție.
    if isWall(mapObj, playerx + xOffset, playery + yOffset):
        return False
    else:
        if (playerx + xOffset, playery + yOffset) in stars:
            # Există o stea în cale, vezi dacă jucătorul o poate împinge.
            if not isBlocked(mapObj, gameStateObj, playerx + (xOffset*2), playery + (yOffset*2)):
                # Mută steaua.
                ind = stars.index((playerx + xOffset, playery + yOffset))
                stars[ind] = (stars[ind][0] + xOffset, stars[ind][1] + yOffset)
            else:
                return False
        # Mută jucătorul în sus.
        gameStateObj['player'] = (playerx + xOffset, playery + yOffset)
        return True


def startScreen():
    """Afișează ecranul de start (care are titlul și instrucțiunile)
    până când jucătorul apasă o tastă. Returnează None."""

    # Poziționează imaginea titlului.
    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = 50  # topCoord urmărește unde să poziționeze partea de sus a textului
    titleRect.top = topCoord
    titleRect.centerx = HALF_WINWIDTH
    topCoord += titleRect.height

    # Din păcate, sistemul de font și text al Pygame arată doar o linie la
    # un moment dat, deci nu putem folosi șiruri cu caractere newline \n în ele.
    # Deci vom folosi o listă cu fiecare linie în ea.
    instructionText = ['Push the stars over the marks.',
                       'Arrow keys to move, WASD for camera control, P to change character.',
                       'Backspace to reset level, Esc to quit.',
                       'N for next level, B to go back a level.']

    # Începe prin a desena o culoare goală pe întreaga fereastră:
    DISPLAYSURF.fill(BGCOLOR)

    # Desenează imaginea titlului pe fereastră:
    DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)

    # Poziționează și desenează textul.
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10  # 10 pixeli vor merge între fiecare linie de text.
        instRect.top = topCoord
        instRect.centerx = HALF_WINWIDTH
        topCoord += instRect.height  # Ajustează pentru înălțimea liniei.
        DISPLAYSURF.blit(instSurf, instRect)

    while True:  # Bucla principală pentru ecranul de start.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return  # utilizatorul a apăsat o tastă, deci returnează.

        # Afișează conținutul DISPLAYSURF pe ecranul real.
        pygame.display.update()
        FPSCLOCK.tick()


def readLevelsFile(filename):
    assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
    mapFile = open(filename, 'r')
    # Fiecare nivel trebuie să se termine cu o linie goală
    content = mapFile.readlines() + ['\r\n']
    mapFile.close()

    levels = []  # Va conține o listă de obiecte nivel.
    levelNum = 0
    mapTextLines = []  # conține liniile pentru harta unui singur nivel.
    mapObj = []  # obiectul hartă făcut din datele din mapTextLines
    for lineNum in range(len(content)):
        # Procesează fiecare linie care era în fișierul de nivel.
        line = content[lineNum].rstrip('\r\n')

        if ';' in line:
            # Ignoră liniile cu ;, sunt comentarii în fișierul de nivel.
            line = line[:line.find(';')]

        if line != '':
            # Această linie face parte din hartă.
            mapTextLines.append(line)
        elif line == '' and len(mapTextLines) > 0:
            # O linie goală indică sfârșitul hărții unui nivel în fișier.
            # Convertește textul din mapTextLines într-un obiect nivel.

            # Găsește cel mai lung rând din hartă.
            maxWidth = -1
            for i in range(len(mapTextLines)):
                if len(mapTextLines[i]) > maxWidth:
                    maxWidth = len(mapTextLines[i])
            # Adaugă spații la sfârșitul rândurilor mai scurte. Acest lucru
            # asigură că harta va fi dreptunghiulară.
            for i in range(len(mapTextLines)):
                mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

            # Convertește mapTextLines într-un obiect hartă.
            for x in range(len(mapTextLines[0])):
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    mapObj[x].append(mapTextLines[y][x])

            # Parcurge spațiile din hartă și găsește caracterele @, ., și $
            # pentru starea de joc de început.
            startx = None  # X și y pentru poziția de start a jucătorului
            starty = None
            goals = []  # listă de tuple (x, y) pentru fiecare obiectiv.
            stars = []  # listă de (x, y) pentru poziția de start a fiecărei stele.
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@', '+'):
                        # '@' este jucător, '+' este jucător & obiectiv
                        startx = x
                        starty = y
                    if mapObj[x][y] in ('.', '+', '*'):
                        # '.' este obiectiv, '*' este stea & obiectiv
                        goals.append((x, y))
                    if mapObj[x][y] in ('$', '*'):
                        # '$' este stea
                        stars.append((x, y))

            # Verificări de bază ale sanității designului nivelului:
            assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, filename)
            assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (levelNum+1, lineNum, filename)
            assert len(stars) >= len(goals), 'Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars.' % (levelNum+1, lineNum, filename, len(goals), len(stars))

            # Creează obiectul nivel și obiectul stare joc de început.
            gameStateObj = {'player': (startx, starty),
                            'stepCounter': 0,
                            'stars': stars}
            levelObj = {'width': maxWidth,
                        'height': len(mapObj),
                        'mapObj': mapObj,
                        'goals': goals,
                        'startState': gameStateObj}

            levels.append(levelObj)

            # Resetează variabilele pentru citirea următoarei hărți.
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelNum += 1
    return levels


def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    """Schimbă orice valori care se potrivesc cu oldCharacter pe obiectul hartă în
    newCharacter la poziția (x, y), și face la fel pentru
    pozițiile la stânga, dreapta, jos și sus de (x, y), recursiv."""

    # În acest joc, algoritmul de umplere cu flood creează distincția
    # podea interior/exterior. Aceasta este o funcție "recursivă".
    # Pentru mai multe informații despre algoritmul Flood Fill, vezi:
    # http://en.wikipedia.org/wiki/Flood_fill
    if mapObj[x][y] == oldCharacter:
        mapObj[x][y] = newCharacter

    if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
        floodFill(mapObj, x+1, y, oldCharacter, newCharacter)  # apel dreapta
    if x > 0 and mapObj[x-1][y] == oldCharacter:
        floodFill(mapObj, x-1, y, oldCharacter, newCharacter)  # apel stânga
    if y < len(mapObj[x]) - 1 and map