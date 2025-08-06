# Capitolul 7 - Tetromino

Tetromino este o clonă Tetris. Blocuri cu forme diferite (fiecare fiind alcătuit din patru cutii) cad din partea de sus a ecranului, iar jucătorul trebuie să le ghideze în jos pentru a forma rânduri complete care nu au goluri în ele. Când se formează un rând complet, rândul dispare și fiecare rând de deasupra acestuia se mișcă în jos cu un rând. Jucătorul încearcă să continue să formeze linii complete până când ecranul se umple și un nou bloc care cade nu mai poate încăpea pe ecran.

## Terminologia Jocului

În acest capitol, am venit cu un set de termeni pentru lucrurile diferite din programul jocului:

- **Board (Tabla)** – Tabla este alcătuită din 10 x 20 spații în care blocurile cad și se stivuiesc.
- **Box (Cutia)** – O cutie este un singur spațiu pătrat umplut pe tablă.
- **Piece (Piesa)** – Lucrurile care cad din partea de sus a tablei pe care jucătorul le poate rota și poziția. Fiecare piesă are o formă și este alcătuită din 4 cutii.
- **Shape (Forma)** – Formele sunt tipurile diferite de piese din joc. Numele formelor sunt T, S, Z, J, L, I și O.
- **Template (Șablon)** – O listă de structuri de date de formă care reprezintă toate rotațiile posibile ale unei forme. Acestea sunt stocate în variabile cu nume precum S_SHAPE_TEMPLATE sau J_SHAPE_TEMPLATE.
- **Landed (Aterizat)** – Când o piesă a ajuns fie la partea de jos a tablei, fie atinge o cutie pe tablă, spunem că piesa a aterizat. La acel punct, următoarea piesă ar trebui să înceapă să cadă.

## Descărcarea Codului

Acest cod sursă poate fi descărcat de la [http://invpy.com/tetromino.py](http://invpy.com/tetromino.py).

Dacă primiți orice mesaje de eroare, uitați-vă la numărul liniei menționat în mesajul de eroare și verificați codul pentru eventuale greșeli de tastare. Puteți, de asemenea, să copiați și să lipiți codul în formularul web de la [http://invpy.com/diff/tetromino](http://invpy.com/diff/tetromino) pentru a vedea diferențele dintre codul vostru și codul din carte.

Veți avea nevoie și de fișierele de muzică de fundal în același folder cu fișierul tetromino.py:
- [http://invpy.com/tetrisb.mid](http://invpy.com/tetrisb.mid)
- [http://invpy.com/tetrisc.mid](http://invpy.com/tetrisc.mid)

## Codul Sursă Complet

```python
1. # Tetromino (o clonă Tetris)
2. # By Al Sweigart al@inventwithpython.com
3. # http://inventwithpython.com/pygame
4. # Creative Commons BY-NC-SA 3.0 US
5.
6. import random, time, pygame, sys
7. from pygame.locals import *
8.
9. FPS = 25
10. WINDOWWIDTH = 640
11. WINDOWHEIGHT = 480
12. BOXSIZE = 20
13. BOARDWIDTH = 10
14. BOARDHEIGHT = 20
15. BLANK = '.'
16.
17. MOVESIDEWAYSFREQ = 0.15
18. MOVEDOWNFREQ = 0.1
19.
20. XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
21. TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5
22.
23. # R G B
24. WHITE = (255, 255, 255)
25. GRAY = (185, 185, 185)
26. BLACK = ( 0, 0, 0)
27. RED = (155, 0, 0)
28. LIGHTRED = (175, 20, 20)
29. GREEN = ( 0, 155, 0)
30. LIGHTGREEN = ( 20, 175, 20)
31. BLUE = ( 0, 0, 155)
32. LIGHTBLUE = ( 20, 20, 175)
33. YELLOW = (155, 155, 0)
34. LIGHTYELLOW = (175, 175, 20)
35.
36. BORDERCOLOR = BLUE
37. BGCOLOR = BLACK
38. TEXTCOLOR = WHITE
39. TEXTSHADOWCOLOR = GRAY
40. COLORS = ( BLUE, GREEN, RED, YELLOW)
41. LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
42. assert len(COLORS) == len(LIGHTCOLORS) # fiecare culoare trebuie să aibă culoare deschisă
43.
44. TEMPLATEWIDTH = 5
45. TEMPLATEHEIGHT = 5
46.
47. S_SHAPE_TEMPLATE = [['.....',
48.                      '.....',
49.                      '..OO.',
50.                      '.OO..',
51.                      '.....'],
52.                     ['.....',
53.                      '..O..',
54.                      '..OO.',
55.                      '...O.',
56.                      '.....']]
57.
58. Z_SHAPE_TEMPLATE = [['.....',
59.                      '.....',
60.                      '.OO..',
61.                      '..OO.',
62.                      '.....'],
63.                     ['.....',
64.                      '..O..',
65.                      '.OO..',
66.                      '.O...',
67.                      '.....']]
68.
69. I_SHAPE_TEMPLATE = [['..O..',
70.                      '..O..',
71.                      '..O..',
72.                      '..O..',
73.                      '.....'],
74.                     ['.....',
75.                      '.....',
76.                      'OOOO.',
77.                      '.....',
78.                      '.....']]
79.
80. O_SHAPE_TEMPLATE = [['.....',
81.                      '.....',
82.                      '.OO..',
83.                      '.OO..',
84.                      '.....']]
85.
86. J_SHAPE_TEMPLATE = [['.....',
87.                      '.O...',
88.                      '.OOO.',
89.                      '.....',
90.                      '.....'],
91.                     ['.....',
92.                      '..OO.',
93.                      '..O..',
94.                      '..O..',
95.                      '.....'],
96.                     ['.....',
97.                      '.....',
98.                      '.OOO.',
99.                      '...O.',
100.                     '.....'],
101.                    ['.....',
102.                     '..O..',
103.                     '..O..',
104.                     '.OO..',
105.                     '.....']]
106.
107. L_SHAPE_TEMPLATE = [['.....',
108.                      '...O.',
109.                      '.OOO.',
110.                      '.....',
111.                      '.....'],
112.                     ['.....',
113.                      '..O..',
114.                      '..O..',
115.                      '..OO.',
116.                      '.....'],
117.                     ['.....',
118.                      '.....',
119.                      '.OOO.',
120.                      '.O...',
121.                      '.....'],
122.                     ['.....',
123.                      '.OO..',
124.                      '..O..',
125.                      '..O..',
126.                      '.....']]
127.
128. T_SHAPE_TEMPLATE = [['.....',
129.                      '..O..',
130.                      '.OOO.',
131.                      '.....',
132.                      '.....'],
133.                     ['.....',
134.                      '..O..',
135.                      '..OO.',
136.                      '..O..',
137.                      '.....'],
138.                     ['.....',
139.                      '.....',
140.                      '.OOO.',
141.                      '..O..',
142.                      '.....'],
143.                     ['.....',
144.                      '..O..',
145.                      '.OO..',
146.                      '..O..',
147.                      '.....']]
148.
149. SHAPES = {'S': S_SHAPE_TEMPLATE,
150.          'Z': Z_SHAPE_TEMPLATE,
151.          'J': J_SHAPE_TEMPLATE,
152.          'L': L_SHAPE_TEMPLATE,
153.          'I': I_SHAPE_TEMPLATE,
154.          'O': O_SHAPE_TEMPLATE,
155.          'T': T_SHAPE_TEMPLATE}
156.
157.
158. def main():
159.     global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
160.     pygame.init()
161.     FPSCLOCK = pygame.time.Clock()
162.     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
163.     BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
164.     BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
165.     pygame.display.set_caption('Tetromino')
166.
167.     showTextScreen('Tetromino')
168.     while True: # bucla de joc
169.         if random.randint(0, 1) == 0:
170.             pygame.mixer.music.load('tetrisb.mid')
171.         else:
172.             pygame.mixer.music.load('tetrisc.mid')
173.         pygame.mixer.music.play(-1, 0.0)
174.         runGame()
175.         pygame.mixer.music.stop()
176.         showTextScreen('Game Over')
177.
178.
179. def runGame():
180.     # configurează variabilele pentru începutul jocului
181.     board = getBlankBoard()
182.     lastMoveDownTime = time.time()
183.     lastMoveSidewaysTime = time.time()
184.     lastFallTime = time.time()
185.     movingDown = False # notă: nu există variabilă movingUp
186.     movingLeft = False
187.     movingRight = False
188.     score = 0
189.     level, fallFreq = calculateLevelAndFallFreq(score)
190.
191.     fallingPiece = getNewPiece()
192.     nextPiece = getNewPiece()
193.
194.     while True: # bucla principală de joc
195.         if fallingPiece == None:
196.             # Nicio piesă care cade în joc, așa că începe o piesă nouă în vârf
197.             fallingPiece = nextPiece
198.             nextPiece = getNewPiece()
199.             lastFallTime = time.time() # resetează lastFallTime
200.
201.             if not isValidPosition(board, fallingPiece):
202.                 return # nu poate încăpea o piesă nouă pe tablă, sfârșitul jocului
203.
204.         checkForQuit()
205.         for event in pygame.event.get(): # bucla de gestionare a evenimentelor
206.             if event.type == KEYUP:
207.                 if (event.key == K_p):
208.                     # Pune jocul în pauză
209.                     DISPLAYSURF.fill(BGCOLOR)
210.                     pygame.mixer.music.stop()
211.                     showTextScreen('Pauză') # pauză până la apăsarea unei taste
212.                     pygame.mixer.music.play(-1, 0.0)
213.                     lastFallTime = time.time()
214.                     lastMoveDownTime = time.time()
215.                     lastMoveSidewaysTime = time.time()
216.                 elif (event.key == K_LEFT or event.key == K_a):
217.                     movingLeft = False
218.                 elif (event.key == K_RIGHT or event.key == K_d):
219.                     movingRight = False
220.                 elif (event.key == K_DOWN or event.key == K_s):
221.                     movingDown = False
222.
223.             elif event.type == KEYDOWN:
224.                 # mută blocul lateral
225.                 if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
226.                     fallingPiece['x'] -= 1
227.                     movingLeft = True
228.                     movingRight = False
229.                     lastMoveSidewaysTime = time.time()
230.
231.                 elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
232.                     fallingPiece['x'] += 1
233.                     movingRight = True
234.                     movingLeft = False
235.                     lastMoveSidewaysTime = time.time()
236.
237.                 # rotește blocul (dacă există spațiu pentru a rota)
238.                 elif (event.key == K_UP or event.key == K_w):
239.                     fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(SHAPES[fallingPiece['shape']])
240.                     if not isValidPosition(board, fallingPiece):
241.                         fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(SHAPES[fallingPiece['shape']])
242.                 elif (event.key == K_q): # rotește în cealaltă direcție
243.                     fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(SHAPES[fallingPiece['shape']])
244.                     if not isValidPosition(board, fallingPiece):
245.                         fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(SHAPES[fallingPiece['shape']])
246.
247.                 # face blocul să cadă mai repede cu tasta jos
248.                 elif (event.key == K_DOWN or event.key == K_s):
249.                     movingDown = True
250.                     if isValidPosition(board, fallingPiece, adjY=1):
251.                         fallingPiece['y'] += 1
252.                     lastMoveDownTime = time.time()
253.
254.                 # mută blocul curent până jos de tot
255.                 elif event.key == K_SPACE:
256.                     movingDown = False
257.                     movingLeft = False
258.                     movingRight = False
259.                     for i in range(1, BOARDHEIGHT):
260.                         if not isValidPosition(board, fallingPiece, adjY=i):
261.                             break
262.                     fallingPiece['y'] += i - 1
263.
264.         # gestionează mutarea blocului din cauza input-ului utilizatorului
265.         if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
266.             if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
267.                 fallingPiece['x'] -= 1
268.             elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
269.                 fallingPiece['x'] += 1
270.             lastMoveSidewaysTime = time.time()
271.
272.         if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
273.             fallingPiece['y'] += 1
274.             lastMoveDownTime = time.time()
275.
276.         # lasă piesa să cadă dacă este timpul să cadă
277.         if time.time() - lastFallTime > fallFreq:
278.             # vezi dacă piesa a aterizat
279.             if not isValidPosition(board, fallingPiece, adjY=1):
280.                 # piesa care cade a aterizat, pune-o pe tablă
281.                 addToBoard(board, fallingPiece)
282.                 score += removeCompleteLines(board)
283.                 level, fallFreq = calculateLevelAndFallFreq(score)
284.                 fallingPiece = None
285.             else:
286.                 # piesa nu a aterizat, doar mută blocul în jos
287.                 fallingPiece['y'] += 1
288.                 lastFallTime = time.time()
289.
290.         # desenează totul pe ecran
291.         DISPLAYSURF.fill(BGCOLOR)
292.         drawBoard(board)
293.         drawStatus(score, level)
294.         drawNextPiece(nextPiece)
295.         if fallingPiece != None:
296.             drawPiece(fallingPiece)
297.
298.         pygame.display.update()
299.         FPSCLOCK.tick(FPS)
300.
301.
302. def makeTextObjs(text, font, color):
303.     surf = font.render(text, True, color)
304.     return surf, surf.get_rect()
305.
306.
307. def terminate():
308.     pygame.quit()
309.     sys.exit()
310.
311.
312. def checkForKeyPress():
313.     # Parcurge coada de evenimente căutând un eveniment KEYUP.
314.     # Prinde evenimentele KEYDOWN pentru a le elimina din coada de evenimente.
315.     checkForQuit()
316.
317.     for event in pygame.event.get([KEYDOWN, KEYUP]):
318.         if event.type == KEYDOWN:
319.             continue
320.         return event.key
321.     return None
322.
323.
324. def showTextScreen(text):
325.     # Această funcție afișează text mare în
326.     # centrul ecranului până când o tastă este apăsată.
327.     # Desenează umbra textului
328.     titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
329.     titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
330.     DISPLAYSURF.blit(titleSurf, titleRect)
331.
332.     # Desenează textul
333.     titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
334.     titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
335.     DISPLAYSURF.blit(titleSurf, titleRect)
336.
337.     # Desenează textul suplimentar "Apasă o tastă pentru a juca."
338.     pressKeySurf, pressKeyRect = makeTextObjs('Apasă o tastă pentru a juca.', BASICFONT, TEXTCOLOR)
339.     pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
340.     DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
341.
342.     while checkForKeyPress() == None:
343.         pygame.display.update()
344.         FPSCLOCK.tick()
345.
346.
347. def checkForQuit():
348.     for event in pygame.event.get(QUIT): # obține toate evenimentele QUIT
349.         terminate() # termină dacă sunt prezente evenimente QUIT
350.     for event in pygame.event.get(KEYUP): # obține toate evenimentele KEYUP
351.         if event.key == K_ESCAPE:
352.             terminate() # termină dacă evenimentul KEYUP a fost pentru tasta Esc
353.         pygame.event.post(event) # pune celelalte obiecte de evenimente KEYUP înapoi
354.
355.
356. def calculateLevelAndFallFreq(score):
357.     # Pe baza scorului, returnează nivelul pe care se află jucătorul și
358.     # câte secunde trec până când o piesă care cade coboară un spațiu.
359.     level = int(score / 10) + 1
360.     fallFreq = 0.27 - (level * 0.02)
361.     return level, fallFreq
362.
363. def getNewPiece():
364.     # returnează o piesă nouă aleatorie într-o rotație și culoare aleatorie
365.     shape = random.choice(list(SHAPES.keys()))
366.     newPiece = {'shape': shape,
367.                 'rotation': random.randint(0, len(SHAPES[shape]) - 1),
368.                 'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
369.                 'y': -2, # începe deasupra tablei (adică mai puțin decât 0)
370.                 'color': random.randint(0, len(COLORS)-1)}
371.     return newPiece
372.
373.
374. def addToBoard(board, piece):
375.     # umple tabla pe baza locației, formei și rotației piesei
376.     for x in range(TEMPLATEWIDTH):
377.         for y in range(TEMPLATEHEIGHT):
378.             if SHAPES[piece['shape']][piece['rotation']][y][x] != BLANK:
379.                 board[x + piece['x']][y + piece['y']] = piece['color']
380.
381.
382. def getBlankBoard():
383.     # creează și returnează o structură de date de tablă goală nouă
384.     board = []
385.     for i in range(BOARDWIDTH):
386.         board.append([BLANK] * BOARDHEIGHT)
387.     return board
388.
389.
390. def isOnBoard(x, y):
391.     return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT
392.
393.
394. def isValidPosition(board, piece, adjX=0, adjY=0):
395.     # Returnează True dacă piesa este în tabla și nu se ciocnește
396.     for x in range(TEMPLATEWIDTH):
397.         for y in range(TEMPLATEHEIGHT):
398.             isAboveBoard = y + piece['y'] + adjY < 0
399.             if isAboveBoard or SHAPES[piece['shape']][piece['rotation']][y][x] == BLANK:
400.                 continue
401.             if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
402.                 return False
403.             if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
404.                 return False
405.     return True
406.
407. def isCompleteLine(board, y):
408.     # Returnează True dacă linia este umplută cu cutii fără goluri.
409.     for x in range(BOARDWIDTH):
410.         if board[x][y] == BLANK:
411.             return False
412.     return True
413.
414.
415. def removeCompleteLines(board):
416.     # Elimină orice linii complete de pe tablă, mută tot ce este deasupra lor în jos și returnează numărul de linii complete.
417.     numLinesRemoved = 0
418.     y = BOARDHEIGHT - 1 # începe y la partea de jos a tablei
419.     while y >= 0:
420.         if isCompleteLine(board, y):
421.             # Elimină linia și trage cutiile în jos cu o linie.
422.             for pullDownY in range(y, 0, -1):
423.                 for x in range(BOARDWIDTH):
424.                     board[x][pullDownY] = board[x][pullDownY-1]
425.             # Setează linia de foarte sus la gol.
426.             for x in range(BOARDWIDTH):
427.                 board[x][0] = BLANK
428.             numLinesRemoved += 1
429.             # Notă: la următoarea iterație a buclei, y este același.
430.             # Aceasta este pentru că dacă linia care a fost trasă în jos este, de asemenea,
431.             # completă, va fi eliminată.
432.         else:
433.             y -= 1 # treci să verifici următorul rând de sus
434.     return numLinesRemoved
435.
436.
437. def convertToPixelCoords(boxx, boxy):
438.     # Convertește coordonatele xy date ale tablei la coordonatele xy
439.     # ale locației de pe ecran.
440.     return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))
441.
442.
443. def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
444.     # desenează o singură cutie (fiecare piesă tetromino are patru cutii)
445.     # la coordonatele xy de pe tablă. Sau, dacă pixelx și pixely
446.     # sunt specificate, desenează la coordonatele pixel stocate în
447.     # pixelx și pixely (aceasta este folosită pentru piesa "Next").
448.     if color == BLANK:
449.         return
450.     if pixelx == None and pixely == None:
451.         pixelx, pixely = convertToPixelCoords(boxx, boxy)
452.     pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
453.     pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))
454.
455.
456. def drawBoard(board):
457.     # desenează bordura în jurul tablei
458.     pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
459.
460.     # umple fundalul tablei
461.     pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
462.     # desenează cutiile individuale de pe tablă
463.     for x in range(BOARDWIDTH):
464.         for y in range(BOARDHEIGHT):
465.             drawBox(x, y, board[x][y])
466.
467.
468. def drawStatus(score, level):
469.     # desenează textul scorului
470.     scoreSurf = BASICFONT.render('Scor: %s' % score, True, TEXTCOLOR)
471.     scoreRect = scoreSurf.get_rect()
472.     scoreRect.topleft = (WINDOWWIDTH - 150, 20)
473.     DISPLAYSURF.blit(scoreSurf, scoreRect)
474.
475.     # desenează textul nivelului
476.     levelSurf = BASICFONT.render('Nivel: %s' % level, True, TEXTCOLOR)
477.     levelRect = levelSurf.get_rect()
478.     levelRect.topleft = (WINDOWWIDTH - 150, 50)
479.     DISPLAYSURF.blit(levelSurf, levelRect)
480.
481.
482. def drawPiece(piece, pixelx=None, pixely=None):
483.     shapeToDraw = SHAPES[piece['shape']][piece['rotation']]
484.     if pixelx == None and pixely == None:
485.         # dacă pixelx și pixely nu au fost specificate, folosește locația stocată în structura de date a piesei
486.         pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])
487.
488.     # desenează fiecare dintre blocurile care alcătuiesc piesa
489.     for x in range(TEMPLATEWIDTH):
490.         for y in range(TEMPLATEHEIGHT):
491.             if shapeToDraw[y][x] != BLANK:
492.                 drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))
493.
494.
495. def drawNextPiece(piece):
496.     # desenează textul "next"
497.     nextSurf = BASICFONT.render('Următoarea:', True, TEXTCOLOR)
498.     nextRect = nextSurf.get_rect()
499.     nextRect.topleft = (WINDOWWIDTH - 120, 80)
500.     DISPLAYSURF.blit(nextSurf, nextRect)
501.     # desenează piesa "next"
502.     drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)
503.
504.
505. if __name__ == '__main__':
506.     main()
```

## Explicația Codului

### Constantele de Bază

```python
9. FPS = 25
10. WINDOWWIDTH = 640
11. WINDOWHEIGHT = 480
12. BOXSIZE = 20
13. BOARDWIDTH = 10
14. BOARDHEIGHT = 20
15. BLANK = '.'
```

Acestea sunt constantele folosite de jocul nostru Tetromino:
- Fiecare cutie este un pătrat cu lățimea și înălțimea de 20 de pixeli
- Tabla în sine este lată de 10 cutii și înaltă de 20 de cutii
- Constanta `BLANK` va fi folosită ca valoare pentru a reprezenta spațiile goale în structura de date a tablei

### Frecvența de Mișcare

```python
17. MOVESIDEWAYSFREQ = 0.15
18. MOVEDOWNFREQ = 0.1
```

De fiecare dată când jucătorul apasă tasta săgeată stânga sau dreapta, piesa care cade ar trebui să se miște cu o cutie spre stânga sau dreapta. Cu toate acestea, jucătorul poate, de asemenea, să țină apăsată tasta săgeată stânga sau dreapta pentru a continua să miște piesa care cade.

- **`MOVESIDEWAYSFREQ`**: Setează ca la fiecare 0.15 secunde care trec cu tasta săgeată stânga sau dreapta ținută apăsată, piesa se va mișca cu încă un spațiu lateral
- **`MOVEDOWNFREQ`**: Același lucru, dar spune cât de frecvent piesa coboară cu o cutie în timp ce jucătorul are tasta săgeată jos ținută apăsată

### Calculul Marginilor

```python
20. XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
21. TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5
```

Programul trebuie să calculeze câți pixeli sunt în partea stângă și dreaptă a tablei pentru a-i folosi mai târziu în program. Tabla va fi desenată cu 5 pixeli deasupra părții de jos a ferestrei.

### Culorile și Efectele de Lumină

```python
40. COLORS = ( BLUE, GREEN, RED, YELLOW)
41. LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
42. assert len(COLORS) == len(LIGHTCOLORS) # fiecare culoare trebuie să aibă culoare deschisă
```

Piesele vor veni în patru culori: albastru, verde, roșu și galben. Când desenăm cutiile, va exista o evidențiere subțire pe cutie într-o culoare mai deschisă. Fiecare dintre aceste patru culori va fi stocată în tuple numite `COLORS` (pentru culorile normale) și `LIGHTCOLORS` (pentru culorile mai deschise).

### Șabloanele de Forme

```python
44. TEMPLATEWIDTH = 5
45. TEMPLATEHEIGHT = 5
```

Programul jocului nostru trebuie să știe cum arată fiecare dintre forme, inclusiv pentru toate rotațiile lor posibile. Pentru a face acest lucru, vom crea liste de liste de șiruri. Lista interioară de șiruri va reprezenta o singură rotație a unei forme:

```python
47. S_SHAPE_TEMPLATE = [['.....',
48.                      '.....',
49.                      '..OO.',
50.                      '.OO..',
51.                      '.....'],
52.                     ['.....',
53.                      '..O..',
54.                      '..OO.',
55.                      '...O.',
56.                      '.....']]
```

Vom scrie restul codului nostru astfel încât să interpreteze o listă de șiruri pentru a reprezenta o formă unde punctele sunt spații goale și O-urile sunt cutii.

**Observație despre formatarea codului**: Aceasta este perfect validă în Python, pentru că interpretorul Python realizează că până când vede paranteza pătrată de închidere `]`, lista nu este terminată. Indentarea nu contează pentru că Python știe că nu veți avea o indentare diferită pentru un bloc nou în mijlocul unei liste.

#### Toate Șabloanele de Forme

Liniile 47-147 vor crea structuri de date "șablon" pentru fiecare dintre forme:

- **S_SHAPE_TEMPLATE**: Forma S cu 2 rotații posibile
- **Z_SHAPE_TEMPLATE**: Forma Z cu 2 rotații posibile  
- **I_SHAPE_TEMPLATE**: Forma I (linie dreaptă) cu 2 rotații posibile
- **O_SHAPE_TEMPLATE**: Forma O (pătrat) cu doar 1 rotație (nu se schimbă când se rotește)
- **J_SHAPE_TEMPLATE**: Forma J cu 4 rotații posibile
- **L_SHAPE_TEMPLATE**: Forma L cu 4 rotații posibile
- **T_SHAPE_TEMPLATE**: Forma T cu 4 rotații posibile

#### Dicționarul SHAPES

```python
149. SHAPES = {'S': S_SHAPE_TEMPLATE,
150.          'Z': Z_SHAPE_TEMPLATE,
151.          'J': J_SHAPE_TEMPLATE,
152.          'L': L_SHAPE_TEMPLATE,
153.          'I': I_SHAPE_TEMPLATE,
154.          'O': O_SHAPE_TEMPLATE,
155.          'T': T_SHAPE_TEMPLATE}
```

Variabila `SHAPES` va fi un dicționar care stochează toate șabloanele diferite. Aceasta va fi structura de date care conține toate datele de formă din jocul nostru.

### Funcția main()

```python
158. def main():
159.     global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
160.     pygame.init()
161.     FPSCLOCK = pygame.time.Clock()
162.     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
163.     BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
164.     BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
165.     pygame.display.set_caption('Tetromino')
166.
167.     showTextScreen('Tetromino')
```

Funcția `main()` gestionează crearea unor constante globale suplimentare și afișarea ecranului de start care apare când programul este rulat.

#### Bucla Principală și Muzica de Fundal

```python
168.     while True: # bucla de joc
169.         if random.randint(0, 1) == 0:
170.             pygame.mixer.music.load('tetrisb.mid')
171.         else:
172.             pygame.mixer.music.load('tetrisc.mid')
173.         pygame.mixer.music.play(-1, 0.0)
174.         runGame()
175.         pygame.mixer.music.stop()
176.         showTextScreen('Game Over')
```

Codul pentru jocul propriu-zis este totul în `runGame()`. Funcția `main()` decide aleatoriu ce muzică de fundal să înceapă redarea, apoi apelează `runGame()` pentru a începe jocul. Când jucătorul pierde, `runGame()` va reveni la `main()`, care apoi oprește muzica de fundal și afișează ecranul de game over.

### Funcția runGame()

#### Inițializarea Variabilelor

```python
179. def runGame():
180.     # configurează variabilele pentru începutul jocului
181.     board = getBlankBoard()
182.     lastMoveDownTime = time.time()
183.     lastMoveSidewaysTime = time.time()
184.     lastFallTime = time.time()
185.     movingDown = False # notă: nu există variabilă movingUp
186.     movingLeft = False
187.     movingRight = False
188.     score = 0
189.     level, fallFreq = calculateLevelAndFallFreq(score)
190.
191.     fallingPiece = getNewPiece()
192.     nextPiece = getNewPiece()
```

Înainte ca jocul să înceapă și piesele să înceapă să cadă, trebuie să inițializăm câteva variabile:
- **`fallingPiece`**: Piesa care cade în prezent și care poate fi rotită de jucător
- **`nextPiece`**: Piesa care apare în partea "Next" a ecranului
- Variabilele de timp pentru a urmări când s-au făcut ultimele mișcări
- Variabilele boolean pentru a urmări dacă jucătorul ține apăsate tastele

#### Bucla Principală de Joc

```python
194.     while True: # bucla principală de joc
195.         if fallingPiece == None:
196.             # Nicio piesă care cade în joc, așa că începe o piesă nouă în vârf
197.             fallingPiece = nextPiece
198.             nextPiece = getNewPiece()
199.             lastFallTime = time.time() # resetează lastFallTime
200.
201.             if not isValidPosition(board, fallingPiece):
202.                 return # nu poate încăpea o piesă nouă pe tablă, sfârșitul jocului
```

Variabila `fallingPiece` este setată la `None` după ce piesa care cade a aterizat. Aceasta înseamnă că piesa din `nextPiece` ar trebui copiată în variabila `fallingPiece`, iar o piesă nouă aleatorie ar trebui pusă în variabila `nextPiece`.

### Gestionarea Evenimentelor

#### Pauza Jocului

```python
207.                 if (event.key == K_p):
208.                     # Pune jocul în pauză
209.                     DISPLAYSURF.fill(BGCOLOR)
210.                     pygame.mixer.music.stop()
211.                     showTextScreen('Pauză') # pauză până la apăsarea unei taste
212.                     pygame.mixer.music.play(-1, 0.0)
213.                     lastFallTime = time.time()
214.                     lastMoveDownTime = time.time()
215.                     lastMoveSidewaysTime = time.time()
```

Dacă jucătorul a apăsat tasta P, atunci jocul ar trebui să se pună în pauză. Trebuie să ascundem tabla de la jucător (altfel jucătorul ar putea trișa punând jocul în pauză și luându-și timp să decidă unde să miște piesa).

#### Mișcarea Laterală

```python
225.                 if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
226.                     fallingPiece['x'] -= 1
227.                     movingLeft = True
228.                     movingRight = False
229.                     lastMoveSidewaysTime = time.time()
```

Funcția `isValidPosition()` are parametri opționali numiți `adjX` și `adjY`. În mod normal, funcția `isValidPosition()` verifică poziția datelor furnizate de obiectul piesă care este transmis pentru al doilea parametru. Cu toate acestea, uneori nu vrem să verificăm unde se află piesa în prezent, ci mai degrabă câteva spații peste acea poziție.

#### Rotirea Pieselor

```python
238.                 elif (event.key == K_UP or event.key == K_w):
239.                     fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(SHAPES[fallingPiece['shape']])
240.                     if not isValidPosition(board, fallingPiece):
241.                         fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(SHAPES[fallingPiece['shape']])
```

Tasta săgeată sus (sau tasta W) va rota piesa care cade la următoarea sa rotație. Codul trebuie doar să incrementeze valoarea cheii 'rotation' din dicționarul `fallingPiece` cu 1. Cu toate acestea, dacă incrementarea valorii cheii 'rotation' o face mai mare decât numărul total de rotații, atunci "mod-ând" cu numărul total de rotații posibile pentru acea formă va face ca aceasta să "se întoarcă" la 0.

**Exemplu cu forma J** (care are 4 rotații posibile):
```python
>>> 0 % 4
0
>>> 3 % 4
3
>>> 4 % 4
0
>>> 5 % 4
1
```

Dacă noua poziție rotită nu este validă pentru că se suprapune cu niște cutii deja pe tablă, atunci vrem să o comutăm înapoi la rotația originală scăzând 1 din `fallingPiece['rotation']`.

#### Căderea Rapidă cu Spațiu

```python
255.                 elif event.key == K_SPACE:
256.                     movingDown = False
257.                     movingLeft = False
258.                     movingRight = False
259.                     for i in range(1, BOARDHEIGHT):
260.                         if not isValidPosition(board, fallingPiece, adjY=i):
261.                             break
262.                     fallingPiece['y'] += i - 1
```

Când jucătorul apasă tasta spațiu, piesa care cade va coborî imediat cât de jos poate merge pe tablă și va ateriza. Pentru a găsi cât de departe poate cădea piesa, ar trebui să apelăm mai întâi `isValidPosition()` și să transmitem întreg-ul 1 pentru parametrul `adjY`. Dacă `isValidPosition()` returnează `False`, știm că piesa nu poate cădea mai mult.

### Sistemul de Timp și Mișcarea Continuă

```python
265.         if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
266.             if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
267.                 fallingPiece['x'] -= 1
268.             elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
269.                 fallingPiece['x'] += 1
270.             lastMoveSidewaysTime = time.time()
```

Variabilele de mișcare (`movingLeft`, `movingRight`, `movingDown`) sunt setate la `True` când jucătorul apasă o tastă și la `False` când o eliberează. Dacă utilizatorul a ținut apăsată tasta mai mult de 0.15 secunde (valoarea stocată în `MOVESIDEWAYSFREQ`), atunci piesa care cade ar trebui să se miște lateral din nou.

**De ce funcționează această abordare**:
- `time.time()` returnează timpul curent în secunde de la 1 ianuarie 1970 (timpul epoch Unix)
- `time.time() - lastMoveSidewaysTime` calculează câte secunde au trecut de la ultima mișcare
- Dacă această valoare este mai mare decât `MOVESIDEWAYSFREQ`, este timpul pentru o nouă mișcare

### Căderea Naturală a Pieselor

```python
277.         if time.time() - lastFallTime > fallFreq:
278.             # vezi dacă piesa a aterizat
279.             if not isValidPosition(board, fallingPiece, adjY=1):
280.                 # piesa care cade a aterizat, pune-o pe tablă
281.                 addToBoard(board, fallingPiece)
282.                 score += removeCompleteLines(board)
283.                 level, fallFreq = calculateLevelAndFallFreq(score)
284.                 fallingPiece = None
285.             else:
286.                 # piesa nu a aterizat, doar mută blocul în jos
287.                 fallingPiece['y'] += 1
288.                 lastFallTime = time.time()
```

Rata cu care piesa se mișcă în jos natural (adică cade) este urmărită de variabila `lastFallTime`. Când piesa aterizează:
1. Se apelează `addToBoard()` pentru a face piesa parte din structura de date a tablei
2. Se apelează `removeCompleteLines()` pentru a șterge orice linii complete și a trage cutiile în jos
3. Se recalculează nivelul și frecvența de cădere pe baza noului scor
4. Se setează `fallingPiece` la `None` pentru a indica că următoarea piesă ar trebui să devină noua piesă care cade

### Funcții Auxiliare Importante

#### calculateLevelAndFallFreq()

```python
356. def calculateLevelAndFallFreq(score):
357.     # Pe baza scorului, returnează nivelul pe care se află jucătorul și
358.     # câte secunde trec până când o piesă care cade coboară un spațiu.
359.     level = int(score / 10) + 1
360.     fallFreq = 0.27 - (level * 0.02)
361.     return level, fallFreq
```

De fiecare dată când jucătorul completează o linie, scorul lor va crește cu un punct. La fiecare zece puncte, jocul urcă un nivel și piesele încep să cadă mai repede.

**Calculul nivelului**:
- Nivelul = `int(scor / 10) + 1`
- Scor 0-9 → Nivel 1
- Scor 10-19 → Nivel 2
- Etc.

**Calculul frecvenței de cădere**:
- Începe cu timpul de bază de 0.27 secunde
- Scade 0.02 secunde pentru fiecare nivel
- La nivelul 14, frecvența va fi negativă, ceea ce înseamnă că piesele vor cădea cât de repede poate

#### getNewPiece()

```python
363. def getNewPiece():
364.     # returnează o piesă nouă aleatorie într-o rotație și culoare aleatorie
365.     shape = random.choice(list(SHAPES.keys()))
366.     newPiece = {'shape': shape,
367.                 'rotation': random.randint(0, len(SHAPES[shape]) - 1),
368.                 'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
369.                 'y': -2, # începe deasupra tablei (adică mai puțin decât 0)
370.                 'color': random.randint(0, len(COLORS)-1)}
371.     return newPiece
```

Structurile de date ale pieselor sunt pur și simplu o valoare dicționar cu cheile:
- **'shape'**: Tipul de formă ('S', 'Z', 'J', etc.)
- **'rotation'**: Indexul rotației curente pentru acea formă
- **'x', 'y'**: Poziția pe tablă
- **'color'**: Indexul culorii din lista `COLORS`

#### isValidPosition()

```python
394. def isValidPosition(board, piece, adjX=0, adjY=0):
395.     # Returnează True dacă piesa este în tabla și nu se ciocnește
396.     for x in range(TEMPLATEWIDTH):
397.         for y in range(TEMPLATEHEIGHT):
398.             isAboveBoard = y + piece['y'] + adjY < 0
399.             if isAboveBoard or SHAPES[piece['shape']][piece['rotation']][y][x] == BLANK:
400.                 continue
401.             if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
402.                 return False
403.             if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
404.                 return False
405.     return True
```

Această funcție verifică dacă o piesă poate fi plasată într-o anumită poziție pe tablă. Se iau coordonatele XY ale piesei și se adaugă coordonata din interiorul structurii de date a piesei pentru a găsi coordonatele "tablei" ale cutiilor piesei.

#### removeCompleteLines()

```python
415. def removeCompleteLines(board):
416.     # Elimină orice linii complete de pe tablă, mută tot ce este deasupra lor în jos și returnează numărul de linii complete.
417.     numLinesRemoved = 0
418.     y = BOARDHEIGHT - 1 # începe y la partea de jos a tablei
419.     while y >= 0:
420.         if isCompleteLine(board, y):
421.             # Elimină linia și trage cutiile în jos cu o linie.
422.             for pullDownY in range(y, 0, -1):
423.                 for x in range(BOARDWIDTH):
424.                     board[x][pullDownY] = board[x][pullDownY-1]
425.             # Setează linia de foarte sus la gol.
426.             for x in range(BOARDWIDTH):
427.                 board[x][0] = BLANK
428.             numLinesRemoved += 1
432.         else:
433.             y -= 1 # treci să verifici următorul rând de sus
434.     return numLinesRemoved
```

Această funcție găsește orice linii complete în structura de date a tablei transmise, elimină liniile și apoi schimbă toate cutiile de pe tablă de deasupra acelei linii în jos cu un rând. Funcția va returna numărul de linii care au fost eliminate.

**Cum funcționează eliminarea**:
1. Începe de la rândul de jos și merge în sus
2. Dacă găsește o linie completă, copiază fiecare rând de deasupra liniei eliminate la rândul de jos
3. Setează rândul de sus la gol
4. Nu incrementează `y` pentru a verifica din nou același rând (în cazul în care linia trasă în jos este, de asemenea, completă)

### Funcțiile de Desenare

#### drawBox()

```python
443. def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
444.     # desenează o singură cutie (fiecare piesă tetromino are patru cutii)
452.     pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
453.     pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))
```

Funcția `drawBox()` desenează o singură cutie pe ecran. Pentru a avea un contur negru între cutiile unei piese, mai întâi se desenează cutia cu culoarea mai întunecată, apoi se desenează o cutie puțin mai mică deasupra cutiei mai întunecate cu culoarea mai deschisă.

#### drawPiece()

```python
482. def drawPiece(piece, pixelx=None, pixely=None):
483.     shapeToDraw = SHAPES[piece['shape']][piece['rotation']]
484.     if pixelx == None and pixely == None:
485.         # dacă pixelx și pixely nu au fost specificate, folosește locația stocată în structura de date a piesei
486.         pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])
487.
488.     # desenează fiecare dintre blocurile care alcătuiesc piesa
489.     for x in range(TEMPLATEWIDTH):
490.         for y in range(TEMPLATEHEIGHT):
491.             if shapeToDraw[y][x] != BLANK:
492.                 drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))
```

Funcția `drawPiece()` va desena cutiile unei piese conform structurii de date a piesei care îi este transmisă. Această funcție va fi folosită pentru a desena piesa care cade și piesa "Next".

## Concluzie

Jocul Tetromino (care este o clonă a jocului mai popular "Tetris") este destul de ușor de explicat cuiva în română: "Blocuri cad din partea de sus a unei table, iar jucătorul le mișcă și le rotește astfel încât să formeze linii complete. Liniile complete dispar (oferind jucătorului puncte) și liniile de deasupra lor se mișcă în jos. Jocul continuă până când blocurile umplu întreaga tablă și jucătorul pierde."

Explicarea în română simplă este un lucru, dar când trebuie să spunem unui calculator exact ce să facă, există multe detalii pe care trebuie să le completăm. Jocul original Tetris a fost conceput și programat de o singură persoană, Alex Pajitnov, în Uniunea Sovietică în 1984. Jocul este simplu, distractiv și captivant. Este unul dintre cele mai populare jocuri video vreodată create și s-au vândut 100 de milioane de exemplare, cu mulți oameni care își creează propriile clone și variații ale acestuia.

Și totul a fost creat de o singură persoană care știa să programeze.

Cu ideea potrivită și câteva cunoștințe de programare, puteți crea jocuri incredibil de distractive. Și cu puțină practică, veți putea să vă transformați ideile de jocuri în programe reale care ar putea deveni la fel de populare ca Tetris!

### Practică Suplimentară

Pentru practică suplimentară de programare, puteți descărca versiuni cu bug-uri ale jocului Tetromino de la [http://invpy.com/buggy/tetromino](http://invpy.com/buggy/tetromino) și să încercați să descoperiți cum să reparați bug-urile.

Există, de asemenea, variații ale jocului Tetromino pe site-ul cărții:

#### Variații ale Jocului:
- **"Pentomino"**: O versiune a acestui joc cu piese alcătuite din cinci cutii - [http://invpy.com/pentomino.py](http://invpy.com/pentomino.py)
- **"Tetromino for Idiots"**: Toate piesele sunt alcătuite din doar o cutie - [http://invpy.com/tetrominoforidiots.py](http://invpy.com/tetrominoforidiots.py)