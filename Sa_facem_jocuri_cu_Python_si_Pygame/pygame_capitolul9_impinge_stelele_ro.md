# Capitolul 9 – Star Pusher (Împinge Stelele)

Star Pusher este o clonă a jocului Sokoban sau "Împinge Stelele". Jucătorul se află într-o cameră cu mai multe stele. Există marcaje de stele pe podeaua unor sprite-uri de dale din cameră. Jucătorul trebuie să-și dea seama cum să împingă stelele deasupra dalelor cu marcaje de stele. Jucătorul nu poate împinge o stea dacă există un perete sau o altă stea în spatele ei. Jucătorul nu poate trage stele, deci dacă o stea este împinsă într-un colț, jucătorul va trebui să repornească nivelul. Când toate stelele au fost împinse pe dalele de podea marcate cu stele, nivelul este complet și începe următorul nivel.

Fiecare nivel este format dintr-o grilă 2D de imagini de dale. Sprite-urile de dale sunt imagini de aceeași dimensiune care pot fi plasate una lângă alta pentru a forma imagini mai complexe. Cu câteva dale de podea și perete, putem crea niveluri de multe forme și dimensiuni interesante.

## Fișierele necesare

Fișierele de nivel nu sunt incluse în codul sursă. În schimb, poți fie să creezi fișierele de nivel singur, fie să le descarci. Un fișier de nivel cu 201 niveluri poate fi descărcat de la http://invpy.com/starPusherLevels.txt.

Când rulezi programul Star Pusher, asigură-te că acest fișier de nivel se află în același folder cu fișierul `starpusher.py`. Altfel vei primi acest mesaj de eroare: `AssertionError: Cannot find the level file: starPusherLevels.txt`

Designurile nivelelor au fost create original de David W. Skinner. Poți descărca mai multe puzzle-uri de pe site-ul său la http://sneezingtiger.com/sokoban/levels.html.

### Descărcări necesare

- **Codul sursă:** http://invpy.com/starpusher.py
- **Fișierul de niveluri:** http://invpy.com/starPusherLevels.txt
- **Imaginile (dale):** http://invpy.com/starPusherImages.zip

Dacă primești mesaje de eroare, verifică numărul liniei menționat în mesajul de eroare și verifică codul pentru greșeli de tastare. De asemenea, poți copia și lipi codul în formularul web de la http://invpy.com/diff/starpusher pentru a vedea diferențele dintre codul tău și codul din carte.

> **Notă importantă:** La fel ca "obiectele" veveriță, iarbă și inamic din jocul Veverița Mănâncă Veveriță, când spun "obiecte hartă", "obiecte stare joc" sau "obiecte nivel" în acest capitol, nu mă refer la obiecte în sensul Programării Orientate pe Obiecte. Aceste "obiecte" sunt de fapt doar valori de dicționar, dar este mai ușor să ne referim la ele ca obiecte deoarece reprezintă lucruri din lumea jocului.

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
        # Mută jucătorul.
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
    instructionText = ['Împinge stelele peste marcaje.',
                       'Săgețile pentru mișcare, WASD pentru controlul camerei, P pentru schimbarea personajului.',
                       'Backspace pentru a reseta nivelul, Esc pentru a ieși.',
                       'N pentru următorul nivel, B pentru a merge înapoi la un nivel.']

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
    if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
        floodFill(mapObj, x, y+1, oldCharacter, newCharacter)  # apel jos
    if y > 0 and mapObj[x][y-1] == oldCharacter:
        floodFill(mapObj, x, y-1, oldCharacter, newCharacter)  # apel sus


def drawMap(mapObj, gameStateObj, goals):
    """Desenează harta pe un obiect Surface, inclusiv jucătorul și
    stelele. Această funcție nu apelează pygame.display.update(), nici
    nu desenează textul "Nivel" și "Pași" în colț."""

    # mapSurf va fi singurul obiect Surface pe care dalele sunt desenate,
    # astfel încât să fie ușor să poziționezi întreaga hartă pe obiectul
    # Surface DISPLAYSURF. Mai întâi, lățimea și înălțimea trebuie calculate.
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)  # începe cu o culoare goală pe suprafață.

    # Desenează sprite-urile de dale pe această suprafață.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * (TILEHEIGHT - TILEFLOORHEIGHT), TILEWIDTH, TILEHEIGHT))
            if mapObj[x][y] in TILEMAPPING:
                baseTile = TILEMAPPING[mapObj[x][y]]
            elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                baseTile = TILEMAPPING[' ']

            # Mai întâi desenează dala de bază sol/perete.
            mapSurf.blit(baseTile, spaceRect)

            if mapObj[x][y] in OUTSIDEDECOMAPPING:
                # Desenează orice decorațiuni copac/stâncă care sunt pe această dală.
                mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
            elif (x, y) in gameStateObj['stars']:
                if (x, y) in goals:
                    # Un obiectiv ȘI o stea sunt pe acest spațiu, desenează mai întâi obiectivul.
                    mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                # Apoi desenează sprite-ul steaua.
                mapSurf.blit(IMAGESDICT['star'], spaceRect)
            elif (x, y) in goals:
                # Desenează un obiectiv fără o stea pe el.
                mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)

            # La urmă desenează jucătorul pe tablă.
            if (x, y) == gameStateObj['player']:
                # Notă: Valoarea "currentImage" se referă
                # la o cheie în "PLAYERIMAGES" care are
                # imaginea specifică a jucătorului pe care vrem să o arătăm.
                mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

    return mapSurf


def isLevelFinished(levelObj, gameStateObj):
    """Returnează True dacă toate obiectivele au stele în ele."""
    for goal in levelObj['goals']:
        if goal not in gameStateObj['stars']:
            # Găsit un spațiu cu un obiectiv dar fără stea pe el.
            return False
    return True


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
```

## Explicarea detaliată a codului

### Constantele și configurarea inițială

Constantele sunt folosite în diverse părți ale programului. Variabilele `TILEWIDTH` și `TILEHEIGHT` arată că fiecare dintre imaginile de dale sunt de 50 de pixeli lățime și 85 de pixeli înălțime. Cu toate acestea, aceste dale se suprapun una peste alta când sunt desenate pe ecran.

`TILEFLOORHEIGHT` se referă la faptul că partea dalei care reprezintă podeaua are 45 de pixeli înălțime. Iată o diagramă a imaginii podelei simple:

```
|← 50 pixeli →|
┌─────────────┐ ↑
│             │ │
│             │ │ 85 pixeli
│             │ │ (TILEHEIGHT)
│─────────────│ ↓
│█████████████│ ← 45 pixeli (TILEFLOORHEIGHT)
└─────────────┘
```

Dalele ierboase din afara camerei nivelului vor avea uneori decorațiuni extra adăugate pe ele (cum ar fi copaci sau stânci). Constanta `OUTSIDE_DECORATION_PCT` arată ce procent din aceste dale vor avea aleatoriu aceste decorațiuni.

### Funcția main()

Primele câteva linii ale funcției `main()` sunt configurarea obișnuită Pygame care se întâmplă la începutul programului.

**IMAGESDICT** este un dicționar unde toate imaginile încărcate sunt stocate. Acest lucru face mai ușoară utilizarea în alte funcții, deoarece doar variabila `IMAGESDICT` trebuie făcută globală. Dacă am stocat fiecare dintre aceste imagini în variabile separate, atunci toate cele 18 variabile (pentru cele 18 imagini folosite în acest joc) ar trebui făcute globale. Un dicționar care conține toate obiectele Surface cu imaginile este mai ușor de gestionat.

Structura de date pentru hartă este doar o listă 2D de șiruri de caractere simple. Dicționarul **TILEMAPPING** leagă caracterele folosite în această structură de date hartă de imaginile pe care le reprezintă.

**OUTSIDEDECOMAPPING** este de asemenea un dicționar care leagă caracterele folosite în structura de date hartă de imaginile care au fost încărcate. Imaginile "decorațiune exterioară" sunt desenate deasupra dalei ierboase exterioare.

Lista **PLAYERIMAGES** stochează imaginile folosite pentru jucător. Variabila `currentImage` urmărește indexul imaginii jucătorului selectate în prezent. De exemplu, când `currentImage` este setat la 0, atunci `PLAYERIMAGES[0]`, care este imaginea jucătorului "princess", este desenată pe ecran.

### Funcția runLevel()

Funcția `runLevel()` gestionează toată acțiunea pentru joc. Îi este transmisă o listă de obiecte nivel și indexul întreg al nivelului din acea listă care urmează să fie jucat. Când jucătorul a terminat de jucat nivelul, `runLevel()` va returna unul dintre următoarele șiruri:

- `'solved'` - jucătorul a terminat punerea tuturor stelelor pe obiective
- `'next'` - jucătorul vrea să treacă la următorul nivel
- `'back'` - jucătorul vrea să se întoarcă la nivelul precedent
- `'reset'` - jucătorul vrea să înceapă să joace nivelul curent din nou

Lista `levels` conține toate obiectele nivel care au fost încărcate din fișierul de nivel. Obiectul nivel pentru nivelul curent este stocat în variabila `levelObj`. Un obiect hartă este returnat de funcția `decorateMap()`. Și pentru a urmări starea jocului în timp ce jucătorul joacă acest nivel, o copie a obiectului stare joc care este stocat în `levelObj` este făcută folosind funcția `copy.deepcopy()`.

**De ce folosim copy.deepcopy()?**

Copia obiectului stare joc este făcută deoarece obiectul stare joc stocat în `levelObj['startState']` reprezintă starea jocului chiar la începutul nivelului, și nu vrem să modificăm aceasta. Altfel, dacă jucătorul repornește nivelul, starea originală a jocului pentru acel nivel va fi pierdută.

Funcția `copy.deepcopy()` este folosită deoarece obiectul stare joc este un dicționar care conține tuple. Tehnic, dicționarul conține referințe la tuple. Folosirea unei instrucțiuni de atribuire pentru a face o copie a dicționarului va face o copie a referințelor dar nu a valorilor la care se referă, astfel încât atât copia cât și dicționarul original se vor referi în continuare la aceleași tuple.

### Structurile de date

Star Pusher are un format specific pentru niveluri, hărți și structurile de date ale stării jocului.

#### Obiectul stării jocului

Obiectul stării jocului va fi un dicționar cu trei chei: `'player'`, `'stepCounter'` și `'stars'`.

- Valoarea la cheia `'player'` va fi un tuplu de două întregi pentru poziția XY curentă a jucătorului.
- Valoarea la cheia `'stepCounter'` va fi un întreg care urmărește câte mișcări a făcut jucătorul în acest nivel (astfel jucătorul poate încerca să rezolve puzzle-ul în viitor cu mai puțini pași).
- Valoarea la cheia `'stars'` este o listă de tuple de două întregi cu valori XY pentru fiecare dintre stelele de pe nivelul curent.

#### Structura de date hartă

Structura de date hartă este pur și simplu o listă 2D de liste unde cei doi indici folosiți reprezintă coordonatele X și Y ale hărții. Valoarea la fiecare index din lista de liste este un șir de caractere cu un singur caracter care reprezintă dala care este pe acea hartă la fiecare spațiu:

- `#` – Un perete de lemn
- `x` – Un perete de colț
- `@` – Spațiul de pornire pentru jucător pe acest nivel
- `.` – Un spațiu obiectiv
- `# Capitolul 9 – Star Pusher (Împinge Stelele)

Star Pusher este o clonă a jocului Sokoban sau "Împinge Stelele". Jucătorul se află într-o cameră cu mai multe stele. Există marcaje de stele pe podeaua unor sprite-uri de dale din cameră. Jucătorul trebuie să-și dea seama cum să împingă stelele deasupra dalelor cu marcaje de stele. Jucătorul nu poate împinge o stea dacă există un perete sau o altă stea în spatele ei. Jucătorul nu poate trage stele, deci dacă o stea este împinsă într-un colț, jucătorul va trebui să repornească nivelul. Când toate stelele au fost împinse pe dalele de podea marcate cu stele, nivelul este complet și începe următorul nivel.

Fiecare nivel este format dintr-o grilă 2D de imagini de dale. Sprite-urile de dale sunt imagini de aceeași dimensiune care pot fi plasate una lângă alta pentru a forma imagini mai complexe. Cu câteva dale de podea și perete, putem crea niveluri de multe forme și dimensiuni interesante.

## Fișierele necesare

Fișierele de nivel nu sunt incluse în codul sursă. În schimb, poți fie să creezi fișierele de nivel singur, fie să le descarci. Un fișier de nivel cu 201 niveluri poate fi descărcat de la http://invpy.com/starPusherLevels.txt.

Când rulezi programul Star Pusher, asigură-te că acest fișier de nivel se află în același folder cu fișierul `starpusher.py`. Altfel vei primi acest mesaj de eroare: `AssertionError: Cannot find the level file: starPusherLevels.txt`

Designurile nivelelor au fost create original de David W. Skinner. Poți descărca mai multe puzzle-uri de pe site-ul său la http://sneezingtiger.com/sokoban/levels.html.

### Descărcări necesare

- **Codul sursă:** http://invpy.com/starpusher.py
- **Fișierul de niveluri:** http://invpy.com/starPusherLevels.txt
- **Imaginile (dale):** http://invpy.com/starPusherImages.zip

Dacă primești mesaje de eroare, verifică numărul liniei menționat în mesajul de eroare și verifică codul pentru greșeli de tastare. De asemenea, poți copia și lipi codul în formularul web de la http://invpy.com/diff/starpusher pentru a vedea diferențele dintre codul tău și codul din carte.

> **Notă importantă:** La fel ca "obiectele" veveriță, iarbă și inamic din jocul Veverița Mănâncă Veveriță, când spun "obiecte hartă", "obiecte stare joc" sau "obiecte nivel" în acest capitol, nu mă refer la obiecte în sensul Programării Orientate pe Obiecte. Aceste "obiecte" sunt de fapt doar valori de dicționar, dar este mai ușor să ne referim la ele ca obiecte deoarece reprezintă lucruri din lumea jocului.

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
        # Mută jucătorul.
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
    instructionText = ['Împinge stelele peste marcaje.',
                       'Săgețile pentru mișcare, WASD pentru controlul camerei, P pentru schimbarea personajului.',
                       'Backspace pentru a reseta nivelul, Esc pentru a ieși.',
                       'N pentru următorul nivel, B pentru a merge înapoi la un nivel.']

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
 – Un spațiu unde este o stea la începutul nivelului
- `+` – Un spațiu cu un obiectiv și spațiul de pornire al jucătorului
- `*` – Un spațiu cu un obiectiv și o stea la începutul nivelului
- ` ` (spațiu) – Un spațiu exterior ierbos
- `o` – Un spațiu de podea interioară (literă O mică, nu zero)
- `1` – O stâncă pe iarbă
- `2` – Un copac scurt pe iarbă
- `3` – Un copac înalt pe iarbă
- `4` – Un copac urât pe iarbă

#### Obiectul nivel

Obiectul nivel conține un obiect stare joc (care va fi starea folosită când nivelul începe pentru prima dată), un obiect hartă și câteva alte valori. Obiectul nivel în sine este un dicționar cu următoarele chei:

- `'width'` - câte dale lată este întreaga hartă
- `'height'` - câte dale înaltă este întreaga hartă
- `'mapObj'` - obiectul hartă pentru acest nivel
- `'goals'` - listă de tuple XY cu coordonatele fiecărui spațiu obiectiv
- `'startState'` - obiect stare joc pentru poziția inițială

### Lucrul cu fișiere text

Python are funcții pentru citirea fișierelor de pe hard disk-ul jucătorului. Acest lucru va fi util pentru a avea un fișier separat care păstrează toate datele pentru fiecare nivel.

**Fișierele text** sunt fișiere care conțin date text simple. Fișierele text sunt create în Windows de aplicația Notepad, Gedit pe Ubuntu și TextEdit pe Mac OS X.

**Diferența dintre editoare de text și procesoare de text** (precum Microsoft Word sau OpenOffice Writer) este că editoarele de text au doar text. Nu poți seta fontul, dimensiunea sau culoarea textului.

#### Crearea și scrierea fișierelor

Pentru a crea un fișier, apelează funcția `open()` și transmite-i două argumente: un șir pentru numele fișierului și șirul `'w'` pentru modul "scriere":

```python
>>> textFile = open('hello.txt', 'w')
>>> textFile.write('Acesta va fi conținutul fișierului.\nSalut lume!\n')
>>> textFile.close()
```

Modul "scriere" spune funcției `open()` să creeze fișierul dacă nu există. Dacă există, atunci `open()` va șterge acel fișier și va crea un fișier nou, gol. **Atenție:** Acest lucru poate fi periculos dacă transmiți accidental un nume de fișier important!

#### Citirea fișierelor

Pentru a citi conținutul unui fișier, transmite șirul `'r'` în loc de `'w'`:

```python
>>> textFile = open('hello.txt', 'r')
>>> content = textFile.readlines()
>>> textFile.close()
>>> content
['Acesta va fi conținutul fișierului.\n', 'Salut lume!\n']
```

Metoda `readlines()` returnează o listă de șiruri: un șir pentru fiecare linie de text din fișier.

Ca alternativă la `readlines()`, poți apela metoda `read()`, care va returna întregul conținut al fișierului ca un singur șir:

```python
>>> textFile = open('hello.txt', 'r')
>>> content = textFile.read()
>>> content
'Acesta va fi conținutul fișierului.\nSalut lume!\n'
```

### Formatul fișierului de niveluri

Formatul fișierului hartă pe care îl vom folosi este deja definit. Există multe jocuri Sokoban și toate folosesc același format de fișier hartă.

Exemplu de fișier de nivel:

```
; Star Pusher (clonă Sokoban)
; De Al Sweigart
;
; Tot ce este după ; este un comentariu
;
; @ - Poziția de pornire a jucătorului
; $ - Poziția de pornire pentru o stea
; . - Un obiectiv unde o stea trebuie împinsă
; + - Jucător & obiectiv
; * - Stea & obiectiv
; (spațiu) - un spațiu deschis gol
; # - Un perete
;
; Nivelurile sunt separate de o linie goală

  ########
  ##     #
  # .  # #
  # $    #
  # .$@$. #
  ####$   #
     #.   #
     #   ##
     #####
```

### Funcția readLevelsFile()

Funcția `readLevelsFile()` citește fișierul de niveluri și returnează o listă de obiecte nivel.

```python
def readLevelsFile(filename):
    assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
```

Funcția `os.path.exists()` va returna `True` dacă fișierul specificat de șirul transmis funcției există. Dacă nu există, `os.path.exists()` returnează `False`.

Fișierul este deschis pentru citire și tot textul este stocat ca o listă de șiruri în variabila `content`, cu o linie goală adăugată la final. (Motivul pentru care se face acest lucru este explicat mai târziu.)

Bucla `for` parcurge fiecare linie care a fost citită din fișierul de nivel câte o linie. Numărul liniei va fi stocat în `lineNum` și șirul de text pentru linie va fi stocat în `line`. Orice caractere newline de la sfârșitul șirului sunt eliminate.

### Funcții recursive

Înainte să poți învăța cum funcționează funcția `floodFill()`, trebuie să înveți despre **recursivitate**. 

**Recursivitatea** este un concept simplu: O funcție recursivă este doar o funcție care se apelează pe ea însăși.

```python
def passFortyTwoWhenYouCallThisFunction(param):
    print('Start of function.')
    if param != 42:
        print('You did not pass 42.')
        print('Fine. I will do it myself.')
        passFortyTwoWhenYouCallThisFunction(42)  # apelul recursiv
    if param == 42:
        print('Thank you for passing 42.')
    print('End of function.')

passFortyTwoWhenYouCallThisFunction(41)
```

Când rulezi acest program, funcția este apelată și 41 este transmis. Ca rezultat, funcția se apelează pe ea însăși și transmite 42. Numim acest apel **apelul recursiv**.

#### Cazul de bază și Stack Overflow

Pentru a preveni bug-urile de **stack overflow**, trebuie să ai un **caz de bază** unde funcția oprește efectuarea de noi apeluri recursive.

```python
def fizz(param):
    print(param)
    if param == 2:
        return  # acesta este cazul de bază
    fizz(param - 1)

fizz(5)
```

Output:
```
5
4
3
2
```

Acest program nu are o eroare de stack overflow deoarece odată ce parametrul `param` este setat la 2, condiția instrucțiunii `if` va fi `True` și funcția va returna.

**Exemplu de stack overflow:**

```python
def funky():
    funky()

funky()
```

Acest cod va cauza o eroare după aproximativ 1000 de apeluri:

```
RuntimeError: maximum recursion depth exceeded
```

### Algoritmul Flood Fill

Algoritmul flood fill este folosit în Star Pusher pentru a schimba toate dalele de podea din interiorul pereților nivelului să folosească imaginea dalei "podea interioară" în loc de dala "podea exterioară".

```python
def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    if mapObj[x][y] == oldCharacter:
        mapObj[x][y] = newCharacter

    if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
        floodFill(mapObj, x+1, y, oldCharacter, newCharacter)  # dreapta
    if x > 0 and mapObj[x-1][y] == oldCharacter:
        floodFill(mapObj, x-1, y, oldCharacter, newCharacter)  # stânga
    if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
        floodFill(mapObj, x, y+1, oldCharacter, newCharacter)  # jos
    if y > 0 and mapObj[x][y-1] == oldCharacter:
        floodFill(mapObj, x, y-1, oldCharacter, newCharacter)  # sus
```

Funcția convertește dala la coordonata XY în `newCharacter` dacă era inițial `oldCharacter`. Apoi face apeluri recursive pentru dalele la dreapta, stânga, jos și sus.

#### Versiune ne-recursivă a Flood Fill

Pentru a înțelege mai bine cum funcționează, iată o versiune care nu folosește apeluri recursive:

```python
def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    spacesToCheck = []
    if mapObj[x][y] == oldCharacter:
        spacesToCheck.append((x, y))
    
    while spacesToCheck != []:
        x, y = spacesToCheck.pop()
        mapObj[x][y] = newCharacter
        
        if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
            spacesToCheck.append((x+1, y))  # verifică dreapta
        if x > 0 and mapObj[x-1][y] == oldCharacter:
            spacesToCheck.append((x-1, y))  # verifică stânga
        if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
            spacesToCheck.append((x, y+1))  # verifică jos
        if y > 0 and mapObj[x][y-1] == oldCharacter:
            spacesToCheck.append((x, y-1))  # verifică sus
```

### Funcția drawMap()

Funcția `drawMap()` va returna un obiect Surface cu întreaga hartă (și jucătorul și stelele) desenate pe el. Lățimea și înălțimea necesare pentru acest Surface trebuie calculate din `mapObj`.

Harta nu trebuie redesenată la fiecare iterație prin bucla de joc. De fapt, acest program este suficient de complicat încât făcând acest lucru ar cauza o încetinire ușoară (dar vizibilă) în joc. Harta trebuie redesenată doar când ceva s-a schimbat (cum ar fi jucătorul mutându-se sau o stea fiind împinsă). Deci obiectul Surface în variabila `mapSurf` este actualizat doar cu un apel la funcția `drawMap()` când variabila `mapNeedsRedraw` este setată la `True`.

### Funcția isLevelFinished()

Funcția `isLevelFinished()` returnează `True` dacă toate obiectivele sunt acoperite de stele. Unele niveluri ar putea avea mai multe stele decât obiective, deci este important să verifici că toate obiectivele sunt acoperite de stele, mai degrabă decât să verifici dacă toate stelele sunt peste obiective.

Bucla `for` parcurge obiectivele din `levelObj['goals']` (care este o listă de tuple XY pentru fiecare obiectiv) și verifică dacă există o stea în lista `gameStateObj['stars']` care are aceleași coordonate XY. Prima dată când codul găsește un obiectiv fără stea în aceeași poziție, funcția returnează `False`.

Dacă trece prin toate obiectivele și găsește o stea pe fiecare dintre ele, `isLevelFinished()` returnează `True`.

## Rezumat

În jocul Veverița Mănâncă Veveriță, lumea jocului era destul de simplă: doar o câmpie verde infinită cu imagini de iarbă răspândite aleatoriu. Jocul Star Pusher a introdus ceva nou: **niveluri proiectate unic cu grafică de dale**. 

Pentru a stoca aceste niveluri într-un format pe care computerul îl poate citi, sunt tastate într-un fișier text și codul din program citește acele fișiere și creează structurile de date pentru nivel.

De fapt, mai degrabă decât să faci doar un joc simplu cu o singură hartă, programul Star Pusher este mai mult **un sistem pentru încărcarea hărților personalizate** bazate pe fișierul de nivel. Doar modificând fișierul de nivel, putem schimba unde apar pereții, stelele și obiectivele în lumea jocului. 

Programul Star Pusher poate gestiona orice configurație la care este setat fișierul de nivel (atâta timp cât trece instrucțiunile `assert` care asigură că harta are sens).

### Crearea propriilor niveluri

Nu va trebui nici măcar să știi cum să programezi Python pentru a-ți face propriile niveluri. Un program editor de text care modifică fișierul `starPusherLevels.txt` este tot ce are nevoie oricine pentru a avea propriul său editor de niveluri pentru jocul Star Pusher.

Pentru practică suplimentară de programare, poți descărca versiuni cu bug-uri ale Star Pusher de la http://invpy.com/buggy/starpusher și poți încerca să descoperi cum să remediezi bug-urile.

---

**Concepte cheie învățate în acest capitol:**

✅ Sisteme de dale (tiles) pentru crearea nivelurilor  
✅ Citirea și scrierea fișierelor text  
✅ Funcții recursive și cazuri de bază  
✅ Algoritmul Flood Fill  
✅ Structuri de date complexe (dicționare imbricate)  
✅ Copierea profundă vs. copierea superficială  
✅ Crearea unui sistem de încărcare a nivelurilor personalizate