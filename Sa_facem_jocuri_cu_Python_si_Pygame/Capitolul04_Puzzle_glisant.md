# Capitolul 4 – Puzzle Glisant

Tabla este o grilă 4x4 cu cincisprezece piese (numerotate de la 1 la 15 de la stânga la dreapta) și un spațiu gol. Piesele încep în poziții aleatorii, iar jucătorul trebuie să gliseze piesele până când acestea revin în ordinea lor originală.

Acest cod sursă poate fi descărcat de la [http://invpy.com/slidepuzzle.py](http://invpy.com/slidepuzzle.py).

Dacă primiți orice mesaje de eroare, uitați-vă la numărul liniei menționat în mesajul de eroare și verificați codul pentru eventuale greșeli de tastare. Puteți, de asemenea, să copiați și să lipiți codul în formularul web de la [http://invpy.com/diff/slidepuzzle](http://invpy.com/diff/slidepuzzle) pentru a vedea diferențele dintre codul vostru și codul din carte.

```python
1. # Slide Puzzle
2. # By Al Sweigart al@inventwithpython.com
3. # http://inventwithpython.com/pygame
4. # Creative Commons BY-NC-SA 3.0 US
5.
6. import pygame, sys, random
7. from pygame.locals import *
8.
9. # Creează constantele (experimentați cu valori diferite)
10. BOARDWIDTH = 4 # numărul de coloane în tablă
11. BOARDHEIGHT = 4 # numărul de rânduri în tablă
12. TILESIZE = 80
13. WINDOWWIDTH = 640
14. WINDOWHEIGHT = 480
15. FPS = 30
16. BLANK = None
17.
18. # R G B
19. BLACK = ( 0, 0, 0)
20. WHITE = (255, 255, 255)
21. BRIGHTBLUE = ( 0, 50, 255)
22. DARKTURQUOISE = ( 3, 54, 73)
23. GREEN = ( 0, 204, 0)
24.
25. BGCOLOR = DARKTURQUOISE
26. TILECOLOR = GREEN
27. TEXTCOLOR = WHITE
28. BORDERCOLOR = BRIGHTBLUE
29. BASICFONTSIZE = 20
30.
31. BUTTONCOLOR = WHITE
32. BUTTONTEXTCOLOR = BLACK
33. MESSAGECOLOR = WHITE
34.
35. XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
36. YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
37.
38. UP = 'up'
39. DOWN = 'down'
40. LEFT = 'left'
41. RIGHT = 'right'
42.
43. def main():
44. global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
45.
46. pygame.init()
47. FPSCLOCK = pygame.time.Clock()
48. DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
49. pygame.display.set_caption('Slide Puzzle')
50. BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
51.
52. # Stochează butoanele opționale și dreptunghiurile lor în OPTIONS.
53. RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
54. NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
55. SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)
56.
57. mainBoard, solutionSeq = generateNewPuzzle(80)
58. SOLVEDBOARD = getStartingBoard() # o tablă rezolvată este aceeași ca tabla în starea inițială.
59. allMoves = [] # lista mișcărilor făcute din configurația rezolvată
60.
61. while True: # bucla principală de joc
62. slideTo = None # direcția, dacă există, în care o piesă ar trebui să gliseze
63. msg = '' # conține mesajul de afișat în colțul din stânga sus.
64. if mainBoard == SOLVEDBOARD:
65. msg = 'Rezolvat!'
66.
67. drawBoard(mainBoard, msg)
68.
69. checkForQuit()
70. for event in pygame.event.get(): # bucla de gestionare a evenimentelor
71. if event.type == MOUSEBUTTONUP:
72. spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])
73.
74. if (spotx, spoty) == (None, None):
75. # verifică dacă utilizatorul a făcut clic pe un buton opțional
76. if RESET_RECT.collidepoint(event.pos):
77. resetAnimation(mainBoard, allMoves) # s-a făcut clic pe butonul Reset
78. allMoves = []
79. elif NEW_RECT.collidepoint(event.pos):
80. mainBoard, solutionSeq = generateNewPuzzle(80) # s-a făcut clic pe butonul New Game
81. allMoves = []
82. elif SOLVE_RECT.collidepoint(event.pos):
83. resetAnimation(mainBoard, solutionSeq + allMoves) # s-a făcut clic pe butonul Solve
84. allMoves = []
85. else:
86. # verifică dacă piesa pe care s-a făcut clic era lângă spațiul gol
87.
88. blankx, blanky = getBlankPosition(mainBoard)
89. if spotx == blankx + 1 and spoty == blanky:
90. slideTo = LEFT
91. elif spotx == blankx - 1 and spoty == blanky:
92. slideTo = RIGHT
93. elif spotx == blankx and spoty == blanky + 1:
94. slideTo = UP
95. elif spotx == blankx and spoty == blanky - 1:
96. slideTo = DOWN
97.
98. elif event.type == KEYUP:
99. # verifică dacă utilizatorul a apăsat o tastă pentru a glisa o piesă
100. if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
101. slideTo = LEFT
102. elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
103. slideTo = RIGHT
104. elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
105. slideTo = UP
106. elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
107. slideTo = DOWN
108.
109. if slideTo:
110. slideAnimation(mainBoard, slideTo, 'Apasă pe piesă sau tastele săgeată pentru a glisa.', 8) # afișează glisarea pe ecran
111. makeMove(mainBoard, slideTo)
112. allMoves.append(slideTo) # înregistrează glisarea
113. pygame.display.update()
114. FPSCLOCK.tick(FPS)
115.
116.
117. def terminate():
118. pygame.quit()
119. sys.exit()
120.
121.
122. def checkForQuit():
123. for event in pygame.event.get(QUIT): # obține toate evenimentele QUIT
124. terminate() # termină dacă sunt prezente evenimente QUIT
125. for event in pygame.event.get(KEYUP): # obține toate evenimentele KEYUP
126. if event.key == K_ESCAPE:
127. terminate() # termină dacă evenimentul KEYUP a fost pentru tasta Esc
128. pygame.event.post(event) # pune celelalte obiecte de evenimente KEYUP înapoi
129.
130.
131. def getStartingBoard():
132. # Returnează o structură de date pentru tablă cu piesele în starea rezolvată.
133. # De exemplu, dacă BOARDWIDTH și BOARDHEIGHT sunt amândouă 3, această funcție
134. # returnează [[1, 4, 7], [2, 5, 8], [3, 6, None]]
135. counter = 1
136. board = []
137. for x in range(BOARDWIDTH):
138. column = []
139. for y in range(BOARDHEIGHT):
140. column.append(counter)
141. counter += BOARDWIDTH
142. board.append(column)
143. counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1
144.
145. board[BOARDWIDTH-1][BOARDHEIGHT-1] = None
146. return board
147.
148.
149. def getBlankPosition(board):
150. # Returnează x și y coordonatele tablei pentru spațiul gol.
151. for x in range(BOARDWIDTH):
152. for y in range(BOARDHEIGHT):
153. if board[x][y] == None:
154. return (x, y)
155.
156.
157. def makeMove(board, move):
158. # Această funcție nu verifică dacă mișcarea este validă.
159. blankx, blanky = getBlankPosition(board)
160.
161. if move == UP:
162. board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
163. elif move == DOWN:
164. board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
165. elif move == LEFT:
166. board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
167. elif move == RIGHT:
168. board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
169.
170.
171. def isValidMove(board, move):
172. blankx, blanky = getBlankPosition(board)
173. return (move == UP and blanky != len(board[0]) - 1) or \
174. (move == DOWN and blanky != 0) or \
175. (move == LEFT and blankx != len(board) - 1) or \
176. (move == RIGHT and blankx != 0)
177.
178.
179. def getRandomMove(board, lastMove=None):
180. # începe cu o listă completă cu toate cele patru mișcări
181. validMoves = [UP, DOWN, LEFT, RIGHT]
182.
183. # elimină mișcările din listă pe măsură ce sunt descalificate
184. if lastMove == UP or not isValidMove(board, DOWN):
185. validMoves.remove(DOWN)
186. if lastMove == DOWN or not isValidMove(board, UP):
187. validMoves.remove(UP)
188. if lastMove == LEFT or not isValidMove(board, RIGHT):
189. validMoves.remove(RIGHT)
190. if lastMove == RIGHT or not isValidMove(board, LEFT):
191. validMoves.remove(LEFT)
192.
193. # returnează o mișcare aleatorie din lista mișcărilor rămase
194. return random.choice(validMoves)
195.
196.
197. def getLeftTopOfTile(tileX, tileY):
198. left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
199. top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
200. return (left, top)
201.
202.
203. def getSpotClicked(board, x, y):
204. # din coordonatele pixel x și y, obține coordonatele x și y ale tablei
205. for tileX in range(len(board)):
206. for tileY in range(len(board[0])):
207. left, top = getLeftTopOfTile(tileX, tileY)
208. tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
209. if tileRect.collidepoint(x, y):
210. return (tileX, tileY)
211. return (None, None)
212.
213.
214. def drawTile(tilex, tiley, number, adjx=0, adjy=0):
215. # desenează o piesă la coordonatele tablei tilex și tiley, opțional cu câțiva
216. # pixeli peste (determinat de adjx și adjy)
217. left, top = getLeftTopOfTile(tilex, tiley)
218. pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
219. textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
220. textRect = textSurf.get_rect()
221. textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
222. DISPLAYSURF.blit(textSurf, textRect)
223.
224.
225. def makeText(text, color, bgcolor, top, left):
226. # creează obiectele Surface și Rect pentru niște text.
227. textSurf = BASICFONT.render(text, True, color, bgcolor)
228. textRect = textSurf.get_rect()
229. textRect.topleft = (top, left)
230. return (textSurf, textRect)
231.
232.
233. def drawBoard(board, message):
234. DISPLAYSURF.fill(BGCOLOR)
235. if message:
236. textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
237. DISPLAYSURF.blit(textSurf, textRect)
238.
239. for tilex in range(len(board)):
240. for tiley in range(len(board[0])):
241. if board[tilex][tiley]:
242. drawTile(tilex, tiley, board[tilex][tiley])
243.
244. left, top = getLeftTopOfTile(0, 0)
245. width = BOARDWIDTH * TILESIZE
246. height = BOARDHEIGHT * TILESIZE
247. pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)
248.
249. DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
250. DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
251. DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)
252.
253.
254. def slideAnimation(board, direction, message, animationSpeed):
255. # Notă: Această funcție nu verifică dacă mișcarea este validă.
256.
257. blankx, blanky = getBlankPosition(board)
258. if direction == UP:
259. movex = blankx
260. movey = blanky + 1
261. elif direction == DOWN:
262. movex = blankx
263. movey = blanky - 1
264. elif direction == LEFT:
265. movex = blankx + 1
266. movey = blanky
267. elif direction == RIGHT:
268. movex = blankx - 1
269. movey = blanky
270.
271. # pregătește suprafața de bază
272. drawBoard(board, message)
273. baseSurf = DISPLAYSURF.copy()
274. # desenează un spațiu gol peste piesa care se mișcă pe suprafața baseSurf.
275. moveLeft, moveTop = getLeftTopOfTile(movex, movey)
276. pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))
277.
278. for i in range(0, TILESIZE, animationSpeed):
279. # animează piesa care glisează
280. checkForQuit()
281. DISPLAYSURF.blit(baseSurf, (0, 0))
282. if direction == UP:
283. drawTile(movex, movey, board[movex][movey], 0, -i)
284. if direction == DOWN:
285. drawTile(movex, movey, board[movex][movey], 0, i)
286. if direction == LEFT:
287. drawTile(movex, movey, board[movex][movey], -i, 0)
288. if direction == RIGHT:
289. drawTile(movex, movey, board[movex][movey], i, 0)
290.
291. pygame.display.update()
292. FPSCLOCK.tick(FPS)
293.
294.
295. def generateNewPuzzle(numSlides):
296. # Din configurația de pornire, fă numSlides numărul de mișcări (și
297. # animează aceste mișcări).
298. sequence = []
299. board = getStartingBoard()
300. drawBoard(board, '')
301. pygame.display.update()
302. pygame.time.wait(500) # pauză de 500 milisecunde pentru efect
303. lastMove = None
304. for i in range(numSlides):
305. move = getRandomMove(board, lastMove)
306. slideAnimation(board, move, 'Generez puzzle nou...', int(TILESIZE / 3))
307. makeMove(board, move)
308. sequence.append(move)
309. lastMove = move
310. return (board, sequence)
311.
312.
313. def resetAnimation(board, allMoves):
314. # fă toate mișcările din allMoves în ordine inversă.
315. revAllMoves = allMoves[:] # obține o copie a listei
316. revAllMoves.reverse()
317.
318. for move in revAllMoves:
319. if move == UP:
320. oppositeMove = DOWN
321. elif move == DOWN:
322. oppositeMove = UP
323. elif move == RIGHT:
324. oppositeMove = LEFT
325. elif move == LEFT:
326. oppositeMove = RIGHT
327. slideAnimation(board, oppositeMove, '', int(TILESIZE / 2))
328. makeMove(board, oppositeMove)
329.
330.
331. if __name__ == '__main__':
332. main()
```

## Explicația Codului

Cea mai mare parte a codului din jocul Slide Puzzle este similară cu jocurile anterioare pe care le-am studiat, în special constantele care sunt stabilite la începutul codului.

### Funcția main()

Așa cum în capitolul anterior, funcțiile apelate din funcția `main()` vor fi explicate mai târziu în capitol. Pentru moment, trebuie să știți doar ce fac și ce valori returnează. Nu trebuie să știți cum funcționează.

Prima parte a funcției `main()` se ocupă de crearea ferestrei, obiectului Clock și obiectului Font. Funcția `makeText()` este definită mai târziu în program, dar pentru moment trebuie să știți doar că returnează un obiect `pygame.Surface` și un obiect `pygame.Rect` care pot fi folosite pentru a crea butoane clickabile.

Jocul Slide Puzzle va avea trei butoane:
- Un buton "Reset" care va anula orice mișcări făcute de jucător
- Un buton "New" care va crea un nou puzzle glisant
- Un buton "Solve" care va rezolva puzzle-ul pentru jucător

### Structurile de Date ale Tablei

Vom avea nevoie de două structuri de date pentru tablă în acest program:
1. O tablă va reprezenta starea curentă a jocului
2. Cealaltă tablă va avea piesele în starea "rezolvată", ceea ce înseamnă că toate piesele sunt aliniate în ordine

Când tabla stării curente a jocului este exact aceeași cu tabla rezolvată, atunci știm că jucătorul a câștigat.

### Generarea unui Puzzle Nou

Funcția `generateNewPuzzle()` va crea o structură de date pentru tablă care a început în starea ordonată, rezolvată și apoi a avut 80 de mișcări aleatorii executate pe ea. Aceasta va face tabla într-o stare amestecată aleatoriu pe care jucătorul va trebui să o rezolve.

### Algoritmul de Rezolvare

Rezolvarea unui puzzle glisant poate fi foarte dificilă. În loc să programăm calculatorul să facă acest lucru (ceea ce ar fi foarte dificil), avem o modalitate mai ușoară. Calculatorul poate memoriza toate glisările aleatorii pe care le-a făcut când a creat structura de date a tablei, iar apoi tabla poate fi rezolvată doar prin efectuarea glisării opuse.

De exemplu, dacă efectuăm o glisare "dreapta" pe tablă, pentru a reveni la starea originală după glisare, trebuie doar să facem glisarea opusă (o glisare stânga). Pentru a reveni la starea originală după mai multe glisări, trebuie doar să facem glisările opuse în ordine inversă.

### Bucla Principală de Joc

În bucla principală de joc, variabila `slideTo` va urmări în ce direcție dorește jucătorul să gliseze o piesă, iar variabila `msg` urmărește ce șir să afișeze în partea de sus a ferestrei.

### Gestionarea Evenimentelor

Programul gestionează două tipuri principale de evenimente:
1. **Evenimente de mouse**: Când jucătorul face clic pe o piesă sau pe un buton
2. **Evenimente de tastatură**: Când jucătorul apasă tastele săgeată sau tastele WASD

#### Tastele WASD

Tastele W, A, S și D (numite tastele WASD, pronunțate "waz-dee") sunt utilizate în mod obișnuit în jocurile pe calculator pentru a face același lucru ca tastele săgeată:
- **W** este pentru sus
- **A** este pentru stânga  
- **S** este pentru jos
- **D** este pentru dreapta

### Funcții Importante

#### `checkForQuit()`
Această funcție verifică evenimentele QUIT (sau dacă utilizatorul a apăsat tasta Esc) și apoi apelează funcția `terminate()`. Utilizează coada de evenimente Pygame pentru a gestiona evenimentele în mod eficient.

#### `getStartingBoard()`
Creează și returnează o structură de date care reprezintă o tablă "rezolvată", unde toate piesele numerotate sunt în ordine și piesa goală este în colțul din dreapta jos.

#### `makeMove()`
Actualizează structura de date a tablei. Valoarea pentru piesă este schimbată cu valoarea pentru spațiul gol. Funcția nu trebuie să returneze valori, deoarece parametrul `board` are o referință de listă transmisă ca argument.

#### `slideAnimation()`
Gestionează animația glisării pieselor. Pentru a desena cadrele animației de glisare, trebuie să deseneze suprafața de bază pe suprafața de afișare, apoi pe fiecare cadru al animației să deseneze piesa care glisează din ce în ce mai aproape de poziția sa finală.

### Optimizarea și Lizibilitatea Codului

Există multe modalități diferite de a scrie jocul Slide Puzzle astfel încât să arate și să acționeze exact la fel, chiar dacă codul este diferit. Cele mai comune diferențe sunt compromisurile între timpul de execuție și utilizarea memoriei.

#### Exemple de Optimizare:

1. **Funcția `getBlankPosition()`**: În loc să căutăm prin toată tabla de fiecare dată, am putea avea variabile `blankspacex` și `blankspacey` care să stocheze aceste coordonate XY.

2. **Variabila `SOLVEDBOARD`**: În loc să păstrăm o tablă în starea rezolvată în memorie, am putea apela `getStartingBoard()` de fiecare dată când vrem să facem comparația.

#### Importanța Lizibilității

**Scrisul de cod lizibil este o abilitate foarte importantă.** Codul "lizibil" este codul care este ușor de înțeles, în special de către programatorii care nu au scris codul. Lizibilitatea este importantă pentru că atunci când vrei să repari erori sau să adaugi funcții noi programului tău, având un program lizibil face aceste sarcini mult mai ușoare.

#### Sfaturi pentru Cod Lizibil:

- Folosește nume de variabile descriptive (de exemplu, `blankx` în loc de `x`)
- Evită trucurile "inteligente" care reduc lizibilitatea
- Nu te preocupa de economisirea a câtorva bytes de memorie dacă face codul mai confuz
- Calculatoarele moderne au miliarde de bytes de memorie - economisirea câtorva bytes nu merită să faci codul mai confuz

### Practică

Pentru practică, poți descărca versiuni cu erori ale programului Sliding Puzzle de la [http://invpy.com/buggy/slidepuzzle](http://invpy.com/buggy/slidepuzzle).

Acest capitol nu a introdus concepte noi de programare Pygame pe care jocul Memory Puzzle nu le-a folosit, în afară de utilizarea metodei `copy()` a obiectelor Surface. Doar cunoașterea câtorva concepte diferite îți va permite să creezi jocuri complet diferite.