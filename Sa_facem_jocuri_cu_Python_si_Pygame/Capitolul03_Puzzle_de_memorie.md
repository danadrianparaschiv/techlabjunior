# Capitolul 3 – Puzzle-ul de Memorie

În jocul Memory Puzzle, mai multe icoane sunt acoperite de cutii albe. Există două din fiecare iconiță. Jucătorul poate face clic pe două cutii pentru a vedea ce iconiță este în spatele lor. Dacă iconițele se potrivesc, atunci acele cutii rămân descoperite. Jucătorul câștigă când toate cutiile de pe tablă sunt descoperite. Pentru a-i da jucătorului un indiciu, cutiile sunt rapid descoperite o dată la începutul jocului.

## Bucle for imbricate

Un concept pe care îl vei vedea în Memory Puzzle (și majoritatea jocurilor din această carte) este folosirea unei bucle for în interiorul altei bucle for. Acestea se numesc bucle for imbricate. Buclele for imbricate sunt utile pentru a parcurge fiecare combinație posibilă din două liste. Tastează următorul în shell-ul interactiv:

```python
>>> for x in [0, 1, 2, 3, 4]:
...     for y in ['a', 'b', 'c']:
...         print(x, y)
...
0 a
0 b
0 c
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
>>>
```

Există de mai multe ori în codul Memory Puzzle când trebuie să iterăm prin fiecare coordonată X și Y posibilă pe tablă. Vom folosi bucle for imbricate pentru a ne asigura că obținem fiecare combinație. Observă că bucla for interioară (bucla for din interiorul celeilalte bucle for) va parcurge toate iterațiile sale înainte de a merge la următoarea iterație a buclei for exterioare.

Acest cod sursă poate fi descărcat de la [http://invpy.com/memorypuzzle.py](http://invpy.com/memorypuzzle.py).

Du-te înainte și tastează întregul program în editorul de fișiere IDLE, salvează-l ca memorypuzzle.py și rulează-l. Dacă primești orice mesaj de eroare, uită-te la numărul liniei care este menționat în mesajul de eroare și verifică-ți codul pentru orice greșeli de tastare.

## Codul sursă pentru Memory Puzzle

```python
# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#        R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
YELLOW = (255, 255,   0)
ORANGE = (255, 128,   0)
PURPLE = (255,   0, 255)
CYAN = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # set the box as "revealed"
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else: # the current box was the second box clicked
                    # Check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): # check if all pairs found
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        startGameAnimation(mainBoard)
                    firstSelection = None # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half = int(BOXSIZE * 0.5) # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))


def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


def startGameAnimation(board):
    # Randomly reveal the boxes 8 at a time.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            return False # return False if any boxes are covered.
    return True


if __name__ == '__main__':
    main()
```

## Importuri și setarea constantelor

```python
import random, pygame, sys
from pygame.locals import *
```

În partea de sus a programului sunt comentarii despre ce este jocul, cine l-a făcut și unde utilizatorul ar putea găsi mai multe informații. Există de asemenea o notă că codul sursă este liber copiabil sub o licență "Simplified BSD".

Acest program face uz de multe funcții din alte module, așa că importă acele module pe linia 6. Linia 7 este de asemenea o instrucțiune import în formatul `from (nume modul) import *`, ceea ce înseamnă că nu trebuie să tastezi numele modulului în fața ei.

### Constante de configurare

```python
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
```

Programele de joc din această carte folosesc multe variabile constante. S-ar putea să nu îți dai seama de ce sunt atât de utile. De exemplu, în loc să folosim variabila BOXSIZE în codul nostru, am putea să tastăm pur și simplu întregul 40 direct în cod. Dar există două motive pentru a folosi variabile constante.

Primul, dacă am vrea vreodată să schimbăm dimensiunea fiecărei cutii mai târziu, ar trebui să parcurgem întregul program și să găsim și să înlocuim de fiecare dată când am tastat 40. Prin folosirea constantei BOXSIZE, trebuie doar să schimbăm linia 13 și restul programului este deja actualizat.

Al doilea, face codul mai lizibil. Constantele chiar ajută lizibilitatea codului sursă.

### Setarea tablei de joc

```python
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
```

Instrucțiunea assert de pe linia 17 se asigură că lățimea și înălțimea tablei pe care le-am selectat vor rezulta într-un număr par de cutii (deoarece vom avea perechi de iconițe în acest joc). Există trei părți la o instrucțiune assert: cuvântul cheie assert, o expresie care, dacă este False, rezultă în prăbușirea programului. A treia parte (după virgula de după expresie) este un șir care apare dacă programul se prăbușește din cauza afirmației.

Instrucțiunea assert cu o expresie spune în esență: "Programatorul afirmă că această expresie trebuie să fie True, altfel prăbușește programul." Aceasta este o modalitate bună de a adăuga o verificare de sănătate programului tău pentru a te asigura că dacă execuția trece vreodată o afirmație, putem cel puțin să știm că acel cod funcționează așa cum este de așteptat.

### Culori și forme

```python
#        R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
YELLOW = (255, 255,   0)
ORANGE = (255, 128,   0)
PURPLE = (255,   0, 255)
CYAN = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'
```

Amintește-ți că culorile în Pygame sunt reprezentate de un tuple de trei întregi de la 0 la 255. Acești trei întregi reprezintă cantitatea de roșu, verde și albastru din culoare, motiv pentru care aceste tuple-uri sunt numite valori RGB.

Programul setează de asemenea variabile constante pentru unele șiruri. Aceste constante vor fi folosite în structura de date pentru tablă, urmărind care spații pe tablă au care iconițe. Folosirea unei variabile constante în loc de valoarea șirului este o idee bună.

```python
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."
```

Pentru ca programul nostru de joc să poată crea iconițe din fiecare combinație posibilă de culoare și formă, trebuie să facem un tuple care să conțină toate aceste valori. Există de asemenea o altă afirmație pe linia 46 pentru a ne asigura că există suficiente combinații culoare/formă pentru dimensiunea tablei pe care o avem.

### Tuple vs Liste

S-ar putea să ai observat că variabilele ALLCOLORS și ALLSHAPES sunt tuple-uri în loc de liste. Când vrem să folosim tuple-uri și când vrem să folosim liste? Și care este diferența dintre ele oricum?

Tuple-urile și listele sunt la fel în toate privințele cu excepția a două: tuple-urile folosesc paranteze în loc de paranteze pătrate, și elementele din tuple-uri nu pot fi modificate (dar elementele din liste pot fi modificate). Adesea numim listele mutabile (însemnând că pot fi schimbate) și tuple-urile imutabile (însemnând că nu pot fi schimbate).

## Funcția main()

```python
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Memory Game')
```

Aceasta este începutul funcției main(), care este locul unde (în mod ciudat) partea principală a codului jocului este. Linia 49 este o instrucțiune global. Orice valori atribuite lor în funcția main() vor persista în afara funcției main().

### Inițializarea structurilor de date

```python
mainBoard = getRandomizedBoard()
revealedBoxes = generateRevealedBoxesData(False)
```

Funcția getRandomizedBoard() returnează o structură de date care reprezintă starea tablei. Funcția generateRevealedBoxesData() returnează o structură de date care reprezintă care cutii sunt acoperite. Valorile returnate ale acestor funcții sunt liste bidimensionale (2D), sau liste de liste.

### Bucla principală de joc

```python
while True: # main game loop
    mouseClicked = False

    DISPLAYSURF.fill(BGCOLOR) # drawing the window
    drawBoard(mainBoard, revealedBoxes)

    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True
```

Bucla de joc este o buclă infinită care începe pe linia 66 care continuă să itereze atât timp cât jocul este în progres. Bucla de joc gestionează evenimente, actualizează starea jocului și desenează starea jocului pe ecran.

### Gestionarea clicurilor de mouse

```python
boxx, boxy = getBoxAtPixel(mousex, mousey)
if boxx != None and boxy != None:
    # The mouse is currently over a box.
    if not revealedBoxes[boxx][boxy]:
        drawHighlightBox(boxx, boxy)
    if not revealedBoxes[boxx][boxy] and mouseClicked:
        revealBoxesAnimation(mainBoard, [(boxx, boxy)])
        revealedBoxes[boxx][boxy] = True # set the box as "revealed"
```

Funcția getBoxAtPixel() va returna un tuple de două întregi. Întregii reprezintă coordonatele XY ale tablei cutiei peste care sunt coordonatele mouse-ului. Dacă cursorul mouse-ului nu era peste nicio cutie, atunci tuple-ul (None, None) este returnat de funcție.

## Funcțiile auxiliare

### generateRevealedBoxesData()

```python
def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes
```

Funcția generateRevealedBoxesData() trebuie să creeze o listă de liste de valori Boolean. Valoarea Boolean va fi doar cea care este pasată funcției ca parametrul val.

### getRandomizedBoard()

```python
def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board
```

Structura de date a tablei este doar o listă de liste de tuple-uri, unde fiecare tuple are două valori: una pentru forma iconiței și una pentru culoarea iconiței. Dar crearea acestei structuri de date este puțin complicată.

### Funcții de desenare

```python
def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half = int(BOXSIZE * 0.5) # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    # ... alte forme
```

Funcția drawIcon() va desena o iconiță (cu forma și culoarea specificate) la spațiul ale cărui coordonate sunt date în parametrii boxx și boxy. Fiecare formă posibilă are un set diferit de apeluri de funcții de desenare Pygame pentru ea.

### Animații

```python
def revealBoxesAnimation(board, boxesToReveal):
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)
```

Amintește-ți că o animație este pur și simplu afișarea unor imagini diferite pentru scurte momente de timp, și împreună fac să pară că lucrurile se mișcă pe ecran. Funcțiile revealBoxesAnimation() și coverBoxesAnimation() trebuie doar să deseneze o iconiță cu o cantitate variabilă de acoperire de către cutia albă.

## Concluzie

Acest capitol acoperă întreaga explicație despre cum funcționează programul Memory Puzzle. Citește din nou capitolul și codul sursă pentru a-l înțelege mai bine. Multe dintre celelalte programe de joc din această carte fac uz de aceleași concepte de programare (precum buclele for imbricate, zahărul sintactic și sistemele de coordonate diferite în același program) astfel încât nu vor fi explicate din nou pentru a menține această carte scurtă.