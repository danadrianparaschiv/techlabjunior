# Capitolul 6 – Wormy (Viermele)

Wormy este o clonă a jocului Nibbles. Jucătorul începe prin a controla un vierme scurt care se mișcă constant pe ecran. Jucătorul nu poate opri sau încetini viermele, dar poate controla în ce direcție se întoarce. Un măr roșu apare aleatoriu pe ecran, iar jucătorul trebuie să miște viermele astfel încât să mănânce mărul. De fiecare dată când viermele mănâncă un măr, viermele crește mai lung cu un segment și un nou măr apare aleatoriu pe ecran. Jocul se termină dacă viermele se izbiește de el însuși sau de marginile ecranului.

## Descărcarea Codului

Acest cod sursă poate fi descărcat de la [http://invpy.com/wormy.py](http://invpy.com/wormy.py).

Dacă primiți orice mesaje de eroare, uitați-vă la numărul liniei menționat în mesajul de eroare și verificați codul pentru eventuale greșeli de tastare. Puteți, de asemenea, să copiați și să lipiți codul în formularul web de la [http://invpy.com/diff/wormy](http://invpy.com/diff/wormy) pentru a vedea diferențele dintre codul vostru și codul din carte.

## Sistemul de Grilă

Dacă jucați jocul puțin, veți observa că mărul și segmentele corpului viermei se potrivesc întotdeauna de-a lungul unei grile de linii. Vom numi fiecare dintre pătratele din această grilă o **celulă**. Celulele au propriul lor sistem de coordonate carteziene, cu (0, 0) fiind celula din stânga sus și (31, 23) fiind celula din dreapta jos.

## Codul Sursă Complet

```python
1. # Wormy (o clonă Nibbles)
2. # By Al Sweigart al@inventwithpython.com
3. # http://inventwithpython.com/pygame
4. # Creative Commons BY-NC-SA 3.0 US
5.
6. import random, pygame, sys
7. from pygame.locals import *
8.
9. FPS = 15
10. WINDOWWIDTH = 640
11. WINDOWHEIGHT = 480
12. CELLSIZE = 20
13. assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
14. assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
15. CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
16. CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
17.
18. # R G B
19. WHITE = (255, 255, 255)
20. BLACK = ( 0, 0, 0)
21. RED = (255, 0, 0)
22. GREEN = ( 0, 255, 0)
23. DARKGREEN = ( 0, 155, 0)
24. DARKGRAY = ( 40, 40, 40)
25. BGCOLOR = BLACK
26.
27. UP = 'up'
28. DOWN = 'down'
29. LEFT = 'left'
30. RIGHT = 'right'
31.
32. HEAD = 0 # zahăr sintactic: indexul capului viermei
33.
34. def main():
35.     global FPSCLOCK, DISPLAYSURF, BASICFONT
36.
37.     pygame.init()
38.     FPSCLOCK = pygame.time.Clock()
39.     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
40.     BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
41.     pygame.display.set_caption('Wormy')
42.
43.     showStartScreen()
44.     while True:
45.         runGame()
46.         showGameOverScreen()
47.
48.
49. def runGame():
50.     # Setează un punct de început aleatoriu.
51.     startx = random.randint(5, CELLWIDTH - 6)
52.     starty = random.randint(5, CELLHEIGHT - 6)
53.     wormCoords = [{'x': startx, 'y': starty},
54.                   {'x': startx - 1, 'y': starty},
55.                   {'x': startx - 2, 'y': starty}]
56.     direction = RIGHT
57.
58.     # Începe mărul într-un loc aleatoriu.
59.     apple = getRandomLocation()
60.
61.     while True: # bucla principală de joc
62.         for event in pygame.event.get(): # bucla de gestionare a evenimentelor
63.             if event.type == QUIT:
64.                 terminate()
65.             elif event.type == KEYDOWN:
66.                 if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
67.                     direction = LEFT
68.                 elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
69.                     direction = RIGHT
70.                 elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
71.                     direction = UP
72.                 elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
73.                     direction = DOWN
74.                 elif event.key == K_ESCAPE:
75.                     terminate()
76.
77.         # verifică dacă viermele s-a lovit de el însuși sau de margine
78.         if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
79.             return # sfârșitul jocului
80.         for wormBody in wormCoords[1:]:
81.             if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
82.                 return # sfârșitul jocului
83.
84.         # verifică dacă viermele a mâncat un măr
85.         if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
86.             # nu elimina segmentul de la coada viermei
87.             apple = getRandomLocation() # setează un măr nou undeva
88.         else:
89.             del wormCoords[-1] # elimină segmentul de la coada viermei
90.
91.         # mută viermele prin adăugarea unui segment în direcția în care se mișcă
92.         if direction == UP:
93.             newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
94.         elif direction == DOWN:
95.             newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
96.         elif direction == LEFT:
97.             newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
98.         elif direction == RIGHT:
99.             newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
100.        wormCoords.insert(0, newHead)
101.        
102.        DISPLAYSURF.fill(BGCOLOR)
103.        drawGrid()
104.        drawWorm(wormCoords)
105.        drawApple(apple)
106.        drawScore(len(wormCoords) - 3)
107.        pygame.display.update()
108.        FPSCLOCK.tick(FPS)
109.
110. def drawPressKeyMsg():
111.     pressKeySurf = BASICFONT.render('Apasă o tastă pentru a juca.', True, DARKGRAY)
112.     pressKeyRect = pressKeySurf.get_rect()
113.     pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
114.     DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
115.
116.
117. def checkForKeyPress():
118.     if len(pygame.event.get(QUIT)) > 0:
119.         terminate()
120.
121.     keyUpEvents = pygame.event.get(KEYUP)
122.     if len(keyUpEvents) == 0:
123.         return None
124.     if keyUpEvents[0].key == K_ESCAPE:
125.         terminate()
126.     return keyUpEvents[0].key
127.
128.
129. def showStartScreen():
130.     titleFont = pygame.font.Font('freesansbold.ttf', 100)
131.     titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
132.     titleSurf2 = titleFont.render('Wormy!', True, GREEN)
133.
134.     degrees1 = 0
135.     degrees2 = 0
136.     while True:
137.         DISPLAYSURF.fill(BGCOLOR)
138.         rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
139.         rotatedRect1 = rotatedSurf1.get_rect()
140.         rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
141.         DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
142.
143.         rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
144.         rotatedRect2 = rotatedSurf2.get_rect()
145.         rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
146.         DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
147.
148.         drawPressKeyMsg()
149.
150.         if checkForKeyPress():
151.             pygame.event.get() # curăță coada de evenimente
152.             return
153.         pygame.display.update()
154.         FPSCLOCK.tick(FPS)
155.         degrees1 += 3 # rotește cu 3 grade la fiecare cadru
156.         degrees2 += 7 # rotește cu 7 grade la fiecare cadru
157.
158.
159. def terminate():
160.     pygame.quit()
161.     sys.exit()
162.
163.
164. def getRandomLocation():
165.     return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
166.
167.
168. def showGameOverScreen():
169.     gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
170.     gameSurf = gameOverFont.render('Game', True, WHITE)
171.     overSurf = gameOverFont.render('Over', True, WHITE)
172.     gameRect = gameSurf.get_rect()
173.     overRect = overSurf.get_rect()
174.     gameRect.midtop = (WINDOWWIDTH / 2, 10)
175.     overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
176.
177.     DISPLAYSURF.blit(gameSurf, gameRect)
178.     DISPLAYSURF.blit(overSurf, overRect)
179.     drawPressKeyMsg()
180.     pygame.display.update()
181.     pygame.time.wait(500)
182.     checkForKeyPress() # curăță orice apăsări de taste din coada de evenimente
183.
184.     while True:
185.         if checkForKeyPress():
186.             pygame.event.get() # curăță coada de evenimente
187.             return
188.
189. def drawScore(score):
190.     scoreSurf = BASICFONT.render('Scor: %s' % (score), True, WHITE)
191.     scoreRect = scoreSurf.get_rect()
192.     scoreRect.topleft = (WINDOWWIDTH - 120, 10)
193.     DISPLAYSURF.blit(scoreSurf, scoreRect)
194.
195.
196. def drawWorm(wormCoords):
197.     for coord in wormCoords:
198.         x = coord['x'] * CELLSIZE
199.         y = coord['y'] * CELLSIZE
200.         wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
201.         pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
202.         wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
203.         pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)
204.
205.
206. def drawApple(coord):
207.     x = coord['x'] * CELLSIZE
208.     y = coord['y'] * CELLSIZE
209.     appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
210.     pygame.draw.rect(DISPLAYSURF, RED, appleRect)
211.
212.
213. def drawGrid():
214.     for x in range(0, WINDOWWIDTH, CELLSIZE): # desenează linii verticale
215.         pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
216.     for y in range(0, WINDOWHEIGHT, CELLSIZE): # desenează linii orizontale
217.         pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))
218.
219.
220. if __name__ == '__main__':
221.     main()
```

## Explicația Codului

### Configurarea Constantelor

Codul de la începutul programului doar stabilește câteva variabile constante folosite în joc:

```python
12. CELLSIZE = 20
13. assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
14. assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
15. CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
16. CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
```

- **`CELLSIZE`**: Lățimea și înălțimea celulelor sunt stocate în `CELLSIZE`
- **Instrucțiunile assert**: Se asigură că celulele se potrivesc perfect în fereastră
- **`CELLWIDTH` și `CELLHEIGHT`**: Numărul de celule pe lățime și înălțime

### Constanta HEAD

```python
32. HEAD = 0 # zahăr sintactic: indexul capului viermei
```

Constanta `HEAD` este setată la 0 pentru a face codul mai lizibil. Capul viermei va fi întotdeauna partea corpului de la `wormCoords[0]`. Pentru a face acest cod mai lizibil, putem folosi `wormCoords[HEAD]` în loc de `wormCoords[0]`.

### Funcția main()

```python
43. showStartScreen()
44. while True:
45.     runGame()
46.     showGameOverScreen()
```

În programul jocului Wormy, am pus partea principală a codului într-o funcție numită `runGame()`. Aceasta este pentru că vrem să afișăm "ecranul de start" doar o dată când programul începe. Apoi vrem să apelăm `runGame()`, care va începe un joc de Wormy. Această funcție va returna când viermele jucătorului se ciocnește de un perete sau de el însuși.

### Funcția runGame()

#### Inițializarea Jocului

```python
50. # Setează un punct de început aleatoriu.
51. startx = random.randint(5, CELLWIDTH - 6)
52. starty = random.randint(5, CELLHEIGHT - 6)
53. wormCoords = [{'x': startx, 'y': starty},
54.               {'x': startx - 1, 'y': starty},
55.               {'x': startx - 2, 'y': starty}]
56. direction = RIGHT
```

La începutul unui joc, vrem ca viermele să înceapă într-o poziție aleatorie, dar nu prea aproape de marginile tablei. Corpul viermei va fi stocat într-o listă de valori dicționar - câte o valoare dicționar per segment de corp al viermei.

#### Gestionarea Evenimentelor

```python
65. elif event.type == KEYDOWN:
66.     if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
67.         direction = LEFT
68.     elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
69.         direction = RIGHT
70.     elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
71.         direction = UP
72.     elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
73.         direction = DOWN
```

Vrem o verificare suplimentară astfel încât viermele să nu se întoarcă în el însuși. De exemplu, dacă viermele se mișcă spre stânga, atunci dacă jucătorul apasă accidental tasta săgeată dreapta, viermele ar începe imediat să meargă la dreapta și s-ar lovi în el însuși.

#### Verificarea Coliziunilor

```python
77. # verifică dacă viermele s-a lovit de el însuși sau de margine
78. if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
79.     return # sfârșitul jocului
80. for wormBody in wormCoords[1:]:
81.     if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
82.         return # sfârșitul jocului
```

Viermele s-a prăbușit când:
1. **Capul s-a mutat în afara grilei**: coordonatele sunt -1 sau egale cu `CELLWIDTH`/`CELLHEIGHT`
2. **Capul se mută pe o celulă ocupată deja** de un alt segment de corp

#### Mâncatul Mărului

```python
84. # verifică dacă viermele a mâncat un măr
85. if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
86.     # nu elimina segmentul de la coada viermei
87.     apple = getRandomLocation() # setează un măr nou undeva
88. else:
89.     del wormCoords[-1] # elimină segmentul de la coada viermei
```

Dacă capul nu s-a ciocnit cu un măr, atunci ștergem ultimul segment de corp din lista `wormCoords`. Codul de mai jos va adăuga un nou segment de corp (pentru cap) în direcția în care merge viermele. Prin a nu șterge ultimul segment de corp când viermele mănâncă un măr, lungimea totală a viermei crește cu unul.

#### Mutarea Viermei

```python
91. # mută viermele prin adăugarea unui segment în direcția în care se mișcă
92. if direction == UP:
93.     newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
94. elif direction == DOWN:
95.     newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
96. elif direction == LEFT:
97.     newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
98. elif direction == RIGHT:
99.     newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
100. wormCoords.insert(0, newHead)
```

Pentru a muta viermele, adăugăm un nou segment de corp la începutul listei `wormCoords`. Deoarece segmentul de corp este adăugat la începutul listei, va deveni noul cap.

**Metoda `insert()`**: Spre deosebire de metoda `append()` care poate adăuga doar elemente la sfârșitul unei liste, metoda `insert()` poate adăuga elemente oriunde în interiorul listei:

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(0, 'frog')
>>> spam
['frog', 'cat', 'dog', 'bat']
>>> spam.insert(10, 42)
>>> spam
['frog', 'cat', 'dog', 'bat', 42]
>>> spam.insert(2, 'horse')
>>> spam
['frog', 'cat', 'horse', 'dog', 'bat', 42]
```

### Funcțiile de Afișare

#### Ecranul de Start cu Animație

```python
129. def showStartScreen():
130.     titleFont = pygame.font.Font('freesansbold.ttf', 100)
131.     titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
132.     titleSurf2 = titleFont.render('Wormy!', True, GREEN)
```

Ecranul de start al Wormy necesită două obiecte Surface cu textul "Wormy!" desenat pe ele. Primul text "Wormy!" va avea text alb cu fundal verde închis, iar celălalt va avea text verde cu fundal transparent.

#### Rotirea Imaginilor

```python
137. rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
138. rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
```

Funcția `pygame.transform.rotate()`:
- **Nu schimbă** obiectul Surface pe care îl transmiteți
- **Returnează** un nou obiect Surface cu imaginea rotită desenată pe acesta
- Noul obiect Surface va fi probabil mai mare decât cel original (pentru a încadra colțurile rotite)

**Rotația se măsoară în grade**:
- **0 grade**: Deloc rotit
- **90 grade**: Un sfert contraclockwise
- **180 grade**: Jumătate de rotație
- **360 grade**: O rotație completă (același cu 0 grade)

#### De ce nu refolosim variabilele?

Există două motive pentru care stocăm imaginea rotită în variabile separate:

1. **Rotirea unei imagini 2D nu este niciodată perfect exactă**. Imaginea rotită este întotdeauna aproximativă. Dacă rotiți o imagine cu 10 grade și apoi o rotiți înapoi cu -10 grade, imaginea nu va fi exact aceeași cu cea cu care ați început.

2. **Imaginea rotită va fi ușor mai mare decât imaginea originală**. Dacă continuați să rotiți aceeași imagine, aceasta va deveni din ce în ce mai mare până când devine prea mare pentru ca Pygame să o gestioneze.

### Funcțiile de Desenare

#### Desenarea Viermei

```python
196. def drawWorm(wormCoords):
197.     for coord in wormCoords:
198.         x = coord['x'] * CELLSIZE
199.         y = coord['y'] * CELLSIZE
200.         wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
201.         pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
202.         wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
203.         pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)
```

Pentru fiecare segment al corpului viermei:
1. Se convertesc coordonatele grilei la coordonate pixel
2. Se desenează un dreptunghi verde închis pentru segment
3. Se desenează un dreptunghi verde strălucitor mai mic deasupra (pentru aspect mai frumos)

#### Desenarea Grilei

```python
213. def drawGrid():
214.     for x in range(0, WINDOWWIDTH, CELLSIZE): # desenează linii verticale
215.         pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
216.     for y in range(0, WINDOWHEIGHT, CELLSIZE): # desenează linii orizontale
217.         pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))
```

Pentru a face mai ușor de vizualizat grila de celule, apelăm `pygame.draw.line()` pentru a desena fiecare dintre liniile verticale și orizontale ale grilei.

**Observarea modelelor regulate** și utilizarea buclelor este un truc inteligent de programator pentru a ne salva de multă tastare. Am fi putut tasta toate cele 56 de apeluri `pygame.draw.line()` și programul ar fi funcționat exact la fel. Dar fiind puțin inteligenți, ne putem economisi multă muncă.

### Lizibilitatea Codului vs. Economisirea Memoriei

Să ne uităm la câteva linii de cod din funcția `drawWorm()`:

```python
199. wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
200. pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
201. wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
202. pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)
```

De ce nu reutilizăm variabila `wormSegmentRect` pentru ambele obiecte Rect? Tehnic, am economisi câțiva bytes de memorie, dar:

1. **Calculatoarele moderne** au memorie de mai multe miliarde de bytes
2. **Economiile nu sunt mari**
3. **Reutilizarea variabilelor reduce lizibilitatea codului**

**Lizibilitatea codului este mult mai importantă** decât economisirea câtorva bytes de memorie aici și acolo. Când vă uitați la propriul cod câteva săptămâni după ce l-ați scris, este posibil să aveți dificultăți în a-și aminti exact cum funcționează.

## Exerciții Practice

Pentru practică suplimentară de programare, puteți descărca versiuni cu bug-uri ale jocului Wormy de la [http://invpy.com/buggy/wormy](http://invpy.com/buggy/wormy) și să încercați să descoperiți cum să reparați bug-urile.
