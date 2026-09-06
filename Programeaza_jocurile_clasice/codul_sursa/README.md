# Codul sursă al jocurilor

Acest folder conține cele cinci jocuri din carte, exact așa cum au fost publicate de editură în depozitul [github.com/Wireframe-Magazine/Code-the-Classics](https://github.com/Wireframe-Magazine/Code-the-Classics), cu toate comentariile autorilor (în limba engleză), imaginile, sunetele și muzica.

| Folder | Joc | Capitol | Inspirat din |
|---|---|---|---|
| [boing](boing/) | Boing! | Capitolul 1 | Pong |
| [cavern](cavern/) | Cavern | Capitolul 2 | Bubble Bobble |
| [bunner](bunner/) | Infinite Bunner | Capitolul 3 | Frogger |
| [myriapod](myriapod/) | Myriapod | Capitolul 4 | Centipede |
| [soccer](soccer/) | Substitute Soccer | Capitolul 5 | Sensible Soccer |

Fiecare folder are un singur fișier Python (de exemplu `boing.py`) și trei subfoldere: `images`, `sounds` și `music`. Pygame Zero le găsește singur, atâta timp cât pornești jocul din folderul lui.

## Instalare

Ai nevoie de Python 3.6 sau mai nou (recomandăm versiunea curentă de pe [python.org](https://www.python.org)) și de biblioteca Pygame Zero, versiunea 1.2 sau mai nouă. Într-un terminal (Command Prompt pe Windows):

```bash
pip3 install pgzero
```

Pe Raspberry Pi OS, Pygame Zero este de obicei deja instalat. Pe Windows, dacă `pip3` nu este recunoscut, încearcă `py -m pip install pgzero`.

## Rularea unui joc

Intră în folderul jocului și pornește fișierul Python:

```bash
cd boing
python3 boing.py
```

Poți deschide fișierul și într-un editor precum Thonny, IDLE sau Mu și să apeși Run. Jocurile își verifică singure versiunile de Python și Pygame Zero și afișează un mesaj dacă ceva lipsește.

## Comenzi

- **Boing!**: jucătorul 1 folosește A/Z sau săgețile sus/jos; jucătorul 2 folosește K/M. SPAȚIU pornește jocul.
- Celelalte jocuri își afișează comenzile pe ecranul de titlu; ele sunt explicate și în capitolele respective.
