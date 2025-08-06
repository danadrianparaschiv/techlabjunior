# Capitolul 5 – Simulate

Simulate este o clonă a jocului Simon. Există patru butoane colorate pe ecran. Butoanele se aprind într-un anumit model aleatoriu, apoi jucătorul trebuie să repete acest model prin apăsarea butoanelor în ordinea corectă. De fiecare dată când jucătorul simulează cu succes modelul, modelul devine mai lung. Jucătorul încearcă să potrivească modelul cât mai mult timp posibil.

## Descărcarea Codului

Acest cod sursă poate fi descărcat de la [http://invpy.com/simulate.py](http://invpy.com/simulate.py).

Dacă primiți orice mesaje de eroare, uitați-vă la numărul liniei menționat în mesajul de eroare și verificați codul pentru eventuale greșeli de tastare. Puteți, de asemenea, să copiați și să lipiți codul în formularul web de la [http://invpy.com/diff/simulate](http://invpy.com/diff/simulate) pentru a vedea diferențele dintre codul vostru și codul din carte.

Puteți descărca cele patru fișiere audio pe care le folosește acest program de la linkurile de mai jos:
- [http://invpy.com/beep1.ogg](http://invpy.com/beep1.ogg)
- [http://invpy.com/beep2.ogg](http://invpy.com/beep2.ogg)  
- [http://invpy.com/beep3.ogg](http://invpy.com/beep3.ogg)
- [http://invpy.com/beep4.ogg](http://invpy.com/beep4.ogg)

## Codul Sursă Complet

```python
1. # Simulate (a Simon clone)
2. # By Al Sweigart al@inventwithpython.com
3. # http://inventwithpython.com/pygame
4. # Creative Commons BY-NC-SA 3.0 US
5.
6. import random, sys, time, pygame
7. from pygame.locals import *
8.
9. FPS = 30
10. WINDOWWIDTH = 640
11. WINDOWHEIGHT = 480
12. FLASHSPEED = 500 # în milisecunde
13. FLASHDELAY = 200 # în milisecunde
14. BUTTONSIZE = 200
15. BUTTONGAPSIZE = 20
16. TIMEOUT = 4 # secunde înainte de sfârșitul jocului dacă nu se apasă niciun buton.
17.
18. # R G B
19. WHITE = (255, 255, 255)
20. BLACK = ( 0, 0, 0)
21. BRIGHTRED = (255, 0, 0)
22. RED = (155, 0, 0)
23. BRIGHTGREEN = ( 0, 255, 0)
24. GREEN = ( 0, 155, 0)
25. BRIGHTBLUE = ( 0, 0, 255)
26. BLUE = ( 0, 0, 155)
27. BRIGHTYELLOW = (255, 255, 0)
28. YELLOW = (155, 155, 0)
29. DARKGRAY = ( 40, 40, 40)
30. bgColor = BLACK
31.
32. XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
33. YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
34.
35. # Obiecte Rect pentru fiecare dintre cele patru butoane
36. YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
37. BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
38. REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
39. GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
40.
41. def main():
42.     global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4
43.
44.     pygame.init()
45.     FPSCLOCK = pygame.time.Clock()
46.     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
47.     pygame.display.set_caption('Simulate')
48.
49.     BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
50.
51.     infoSurf = BASICFONT.render('Potrivește modelul făcând clic pe buton sau folosind tastele Q, W, A, S.', 1, DARKGRAY)
52.     infoRect = infoSurf.get_rect()
53.     infoRect.topleft = (10, WINDOWHEIGHT - 25)
54.     # încarcă fișierele audio
55.     BEEP1 = pygame.mixer.Sound('beep1.ogg')
56.     BEEP2 = pygame.mixer.Sound('beep2.ogg')
57.     BEEP3 = pygame.mixer.Sound('beep3.ogg')
58.     BEEP4 = pygame.mixer.Sound('beep4.ogg')
59.
60.     # Inițializează câteva variabile pentru un joc nou
61.     pattern = [] # stochează modelul de culori
62.     currentStep = 0 # culoarea pe care jucătorul trebuie să o apese următoarea
63.     lastClickTime = 0 # timpul ultimei apăsări de buton a jucătorului
64.     score = 0
65.     # când False, modelul se redă. când True, așteaptă ca jucătorul să facă clic pe un buton colorat:
66.     waitingForInput = False
67.
68.     while True: # bucla principală de joc
69.         clickedButton = None # butonul pe care s-a făcut clic (setat la YELLOW, RED, GREEN sau BLUE)
70.         DISPLAYSURF.fill(bgColor)
71.         drawButtons()
72.
73.         scoreSurf = BASICFONT.render('Scor: ' + str(score), 1, WHITE)
74.         scoreRect = scoreSurf.get_rect()
75.         scoreRect.topleft = (WINDOWWIDTH - 100, 10)
76.         DISPLAYSURF.blit(scoreSurf, scoreRect)
77.
78.         DISPLAYSURF.blit(infoSurf, infoRect)
79.
80.         checkForQuit()
81.         for event in pygame.event.get(): # bucla de gestionare a evenimentelor
82.             if event.type == MOUSEBUTTONUP:
83.                 mousex, mousey = event.pos
84.                 clickedButton = getButtonClicked(mousex, mousey)
85.             elif event.type == KEYDOWN:
86.                 if event.key == K_q:
87.                     clickedButton = YELLOW
88.                 elif event.key == K_w:
89.                     clickedButton = BLUE
90.                 elif event.key == K_a:
91.                     clickedButton = RED
92.                 elif event.key == K_s:
93.                     clickedButton = GREEN
94.
95.         if not waitingForInput:
96.             # redă modelul
97.             pygame.display.update()
98.             pygame.time.wait(1000)
99.             pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
100.            for button in pattern:
101.                flashButtonAnimation(button)
102.                pygame.time.wait(FLASHDELAY)
103.            waitingForInput = True
104.        else:
105.            # așteaptă ca jucătorul să introducă butoanele
106.            if clickedButton and clickedButton == pattern[currentStep]:
107.                # a apăsat butonul corect
108.                flashButtonAnimation(clickedButton)
109.                currentStep += 1
110.                lastClickTime = time.time()
111.
112.                if currentStep == len(pattern):
113.                    # a apăsat ultimul buton din model
114.                    changeBackgroundAnimation()
115.                    score += 1
116.                    waitingForInput = False
117.                    currentStep = 0 # resetează înapoi la primul pas
118.
119.            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
120.                # a apăsat butonul incorect, sau a expirat timpul
121.                gameOverAnimation()
122.                # resetează variabilele pentru un joc nou:
123.                pattern = []
124.                currentStep = 0
125.                waitingForInput = False
126.                score = 0
127.                pygame.time.wait(1000)
128.                changeBackgroundAnimation()
129.
130.        pygame.display.update()
131.        FPSCLOCK.tick(FPS)
132.
133.
134. def terminate():
135.     pygame.quit()
136.     sys.exit()
137.
138.
139. def checkForQuit():
140.     for event in pygame.event.get(QUIT): # obține toate evenimentele QUIT
141.         terminate() # termină dacă sunt prezente evenimente QUIT
142.     for event in pygame.event.get(KEYUP): # obține toate evenimentele KEYUP
143.         if event.key == K_ESCAPE:
144.             terminate() # termină dacă evenimentul KEYUP a fost pentru tasta Esc
145.         pygame.event.post(event) # pune celelalte obiecte de evenimente KEYUP înapoi
146.
147.
148. def flashButtonAnimation(color, animationSpeed=50):
149.     if color == YELLOW:
150.         sound = BEEP1
151.         flashColor = BRIGHTYELLOW
152.         rectangle = YELLOWRECT
153.     elif color == BLUE:
154.         sound = BEEP2
155.         flashColor = BRIGHTBLUE
156.         rectangle = BLUERECT
157.     elif color == RED:
158.         sound = BEEP3
159.         flashColor = BRIGHTRED
160.         rectangle = REDRECT
161.     elif color == GREEN:
162.         sound = BEEP4
163.         flashColor = BRIGHTGREEN
164.         rectangle = GREENRECT
165.
166.     origSurf = DISPLAYSURF.copy()
167.     flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
168.     flashSurf = flashSurf.convert_alpha()
169.     r, g, b = flashColor
170.     sound.play()
171.     for start, end, step in ((0, 255, 1), (255, 0, -1)): # bucla de animație
172.         for alpha in range(start, end, animationSpeed * step):
173.             checkForQuit()
174.             DISPLAYSURF.blit(origSurf, (0, 0))
175.             flashSurf.fill((r, g, b, alpha))
176.             DISPLAYSURF.blit(flashSurf, rectangle.topleft)
177.             pygame.display.update()
178.             FPSCLOCK.tick(FPS)
179.     DISPLAYSURF.blit(origSurf, (0, 0))
180.
181.
182. def drawButtons():
183.     pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
184.     pygame.draw.rect(DISPLAYSURF, BLUE, BLUERECT)
185.     pygame.draw.rect(DISPLAYSURF, RED, REDRECT)
186.     pygame.draw.rect(DISPLAYSURF, GREEN, GREENRECT)
187.
188.
189. def changeBackgroundAnimation(animationSpeed=40):
190.     global bgColor
191.     newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
192.
193.     newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
194.     newBgSurf = newBgSurf.convert_alpha()
195.     r, g, b = newBgColor
196.     for alpha in range(0, 255, animationSpeed): # bucla de animație
197.         checkForQuit()
198.         DISPLAYSURF.fill(bgColor)
199.
200.         newBgSurf.fill((r, g, b, alpha))
201.         DISPLAYSURF.blit(newBgSurf, (0, 0))
202.
203.         drawButtons() # redesenează butoanele deasupra nuanței
204.
205.         pygame.display.update()
206.         FPSCLOCK.tick(FPS)
207.     bgColor = newBgColor
208.
209.
210. def gameOverAnimation(color=WHITE, animationSpeed=50):
211.     # redă toate bipurile deodată, apoi face să clipească fundalul
212.     origSurf = DISPLAYSURF.copy()
213.     flashSurf = pygame.Surface(DISPLAYSURF.get_size())
214.     flashSurf = flashSurf.convert_alpha()
215.     BEEP1.play() # redă toate cele patru bipuri în același timp, aproximativ.
216.     BEEP2.play()
217.     BEEP3.play()
218.     BEEP4.play()
219.     r, g, b = color
220.     for i in range(3): # fă clipirea de 3 ori
221.         for start, end, step in ((0, 255, 1), (255, 0, -1)):
222.             # Prima iterație în această buclă setează următoarea buclă for
223.             # să meargă de la 0 la 255, a doua de la 255 la 0.
224.             for alpha in range(start, end, animationSpeed * step): # bucla de animație
225.                 # alpha înseamnă transparență. 255 este opac, 0 este invizibil
226.                 checkForQuit()
227.                 flashSurf.fill((r, g, b, alpha))
228.                 DISPLAYSURF.blit(origSurf, (0, 0))
229.                 DISPLAYSURF.blit(flashSurf, (0, 0))
230.                 drawButtons()
231.                 pygame.display.update()
232.                 FPSCLOCK.tick(FPS)
233.
234.
235. def getButtonClicked(x, y):
236.     if YELLOWRECT.collidepoint( (x, y) ):
237.         return YELLOW
238.     elif BLUERECT.collidepoint( (x, y) ):
239.         return BLUE
240.     elif REDRECT.collidepoint( (x, y) ):
241.         return RED
242.     elif GREENRECT.collidepoint( (x, y) ):
243.         return GREEN
244.     return None
245.
246.
247. if __name__ == '__main__':
248.     main()
```

## Explicația Codului

### Configurarea Constantelor

Aici stabilim constantele obișnuite pentru lucrurile pe care am putea dori să le modificăm mai târziu, cum ar fi dimensiunea celor patru butoane, nuanțele de culoare folosite pentru butoane (culorile strălucitoare sunt folosite când butoanele se aprind) și timpul pe care îl are jucătorul să apese următorul buton din secvență înainte ca jocul să expire.

```python
32. XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
33. YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
```

### Obiectele Rect pentru Butoane

```python
35. # Obiecte Rect pentru fiecare dintre cele patru butoane
36. YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
37. BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
38. REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
39. GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
```

La fel ca butoanele din jocurile Sliding Puzzle pentru "Reset", "Solve" și "New Game", jocul Simulate are patru zone dreptunghiulare și cod pentru a gestiona când jucătorul face clic în interiorul acelor zone. Programul va avea nevoie de obiecte Rect pentru zonele celor patru butoane astfel încât să poată apela metoda `collidepoint()` pe ele.

### Funcția main()

Funcția `main()` va implementa cea mai mare parte a programului și va apela celelalte funcții după cum sunt necesare. Funcțiile obișnuite de configurare Pygame sunt apelate pentru a inițializa biblioteca, pentru a crea un obiect Clock, pentru a crea o fereastră, pentru a seta titlul și pentru a crea un obiect Font care va fi folosit pentru a afișa scorul și instrucțiunile în fereastră.

#### Încărcarea Fișierelor Audio

```python
54. # încarcă fișierele audio
55. BEEP1 = pygame.mixer.Sound('beep1.ogg')
56. BEEP2 = pygame.mixer.Sound('beep2.ogg')
57. BEEP3 = pygame.mixer.Sound('beep3.ogg')
58. BEEP4 = pygame.mixer.Sound('beep4.ogg')
```

Liniile 55-58 vor încărca fișierele audio astfel încât Simulate să poată reda efecte sonore în timp ce jucătorul face clic pe fiecare buton. Funcția constructor `pygame.mixer.Sound()` va returna un obiect Sound, pe care îl stocăm în variabilele `BEEP1` până la `BEEP4`.

### Variabilele de Stare a Jocului

```python
60. # Inițializează câteva variabile pentru un joc nou
61. pattern = [] # stochează modelul de culori
62. currentStep = 0 # culoarea pe care jucătorul trebuie să o apese următoarea
63. lastClickTime = 0 # timpul ultimei apăsări de buton a jucătorului
64. score = 0
65. # când False, modelul se redă. când True, așteaptă ca jucătorul să facă clic pe un buton colorat:
66. waitingForInput = False
```

- **`pattern`**: o listă de valori de culoare pentru a ține evidența modelului pe care jucătorul trebuie să îl memoreze
- **`currentStep`**: ține evidența cărei culori din lista pattern trebuie să îi facă clic jucătorul următoarea
- **`lastClickTime`**: pentru a verifica dacă a trecut destul timp de la ultimul clic pe buton
- **`score`**: ține evidența scorului
- **`waitingForInput`**: are două moduri - fie programul redă modelul de butoane pentru jucător (False), fie programul a terminat redarea modelului și așteaptă ca utilizatorul să facă clic pe butoane în ordinea corectă (True)

### Bucla Principală de Joc

Bucla principală începe la linia 68. Variabila `clickedButton` va fi resetată la `None` la începutul fiecărei iterații. Dacă se face clic pe un buton în timpul acestei iterații, atunci `clickedButton` va fi setată la una dintre valorile de culoare pentru a se potrivi cu butonul.

### Gestionarea Evenimentelor

#### Evenimente de Mouse și Tastatură

```python
81. for event in pygame.event.get(): # bucla de gestionare a evenimentelor
82.     if event.type == MOUSEBUTTONUP:
83.         mousex, mousey = event.pos
84.         clickedButton = getButtonClicked(mousex, mousey)
85.     elif event.type == KEYDOWN:
86.         if event.key == K_q:
87.             clickedButton = YELLOW
88.         elif event.key == K_w:
89.             clickedButton = BLUE
90.         elif event.key == K_a:
91.             clickedButton = RED
92.         elif event.key == K_s:
93.             clickedButton = GREEN
```

Tastele Q, W, A și S corespund butoanelor pentru că sunt aranjate într-o formă pătrată pe tastatură:
- **Q**: corespunde butonului galben (stânga sus)
- **W**: corespunde butonului albastru (dreapta sus)  
- **A**: corespunde butonului roșu (stânga jos)
- **S**: corespunde butonului verde (dreapta jos)

### Modurile Programului

Există două "moduri" sau "stări" diferite în care poate fi programul:

#### Modul de Redare a Modelului (waitingForInput = False)

```python
95. if not waitingForInput:
96.     # redă modelul
97.     pygame.display.update()
98.     pygame.time.wait(1000)
99.     pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
100.    for button in pattern:
101.        flashButtonAnimation(button)
102.        pygame.time.wait(FLASHDELAY)
103.    waitingForInput = True
```

Când `waitingForInput` este `False`, programul va afișa animația pentru model. Linia 99 va adăuga o culoare aleatoare la lista pattern pentru a face modelul cu un pas mai lung.

#### Modul de Introducere a Jucătorului (waitingForInput = True)

```python
104. else:
105.     # așteaptă ca jucătorul să introducă butoanele
106.     if clickedButton and clickedButton == pattern[currentStep]:
107.         # a apăsat butonul corect
108.         flashButtonAnimation(clickedButton)
109.         currentStep += 1
110.         lastClickTime = time.time()
```

Când jucătorul face clic pe butonul corect, programul face butonul să clipească, crește `currentStep` la următorul pas și actualizează `lastClickTime` la timpul curent.

### Timpul și Timeout-ul

Programul folosește funcția `time.time()` care returnează numărul de secunde de la 1 ianuarie 1970 (numit timpul epoch Unix). Aceasta permite programului să verifice dacă jucătorul a așteptat prea mult pentru a face clic pe următorul buton.

```python
119. elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
```

Această condiție verifică două lucruri:
1. Dacă jucătorul a făcut clic pe butonul greșit
2. Dacă jucătorul a "expirat" (nu a făcut clic pe un buton în timp de 4 secunde)

### Funcțiile de Animație

#### Animația Flash a Butonului

```python
148. def flashButtonAnimation(color, animationSpeed=50):
```

Animația flash a butonului funcționează prin desenarea tablei normale și apoi desenarea versiunii de culoare strălucitoare a butonului pe deasupra. Valoarea alfa a culorii strălucitoare începe de la 0 și crește treptat până devine complet opacă, făcând să pară că butonul se luminează treptat.

#### Animația de Schimbare a Fundalului

```python
189. def changeBackgroundAnimation(animationSpeed=40):
```

Această animație se întâmplă când jucătorul termină cu succes introducerea întregului model. Pe fiecare iterație prin buclă, întreaga suprafață de afișare trebuie să fie redesenată cu o culoare de fundal din ce în ce mai puțin transparentă.

#### Animația Game Over

```python
210. def gameOverAnimation(color=WHITE, animationSpeed=50):
```

Când jucătorul face o greșeală sau expiră timpul, toate cele patru sunete sunt redate simultan și fundalul clipește de trei ori pentru a indica sfârșitul jocului.

### Zen-ul Python

La sfârșitul codului este menționat un "Easter egg" din Python. Dacă tastați `import this` în shell-ul interactiv Python, veți vedea "Zen-ul Python" - un set de principii pentru scrierea unui cod bun:

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
...
```

Aceste principii ne învață că este mai bine să scriem cod care este:
- **Explicit** în loc de implicit
- **Simplu** în loc de complex  
- **Lizibil** și clar în intenție

De aceea funcția `getButtonClicked()` se termină cu `return None` explicit, chiar dacă toate funcțiile returnează `None` implicit - pentru a face codul mai clar și mai ușor de înțeles.