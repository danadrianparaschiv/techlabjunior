
# Capitolul 12 – Jocul final: Aventura completă

## Ce vom face în acest capitol

Vom combina toate mecanicile din capitolele anterioare:
- Harta mare și navigarea liberă.
- Inventar și aur.
- Monștri și lupte.
- Misiuni și obiective.
- Salvare și încărcare progres (JSON).
Vom avea o poveste completă: Eliza trebuie să găsească „Cheia Magică” și să înfrângă Dragonul Final.

## Structura jocului

- Pornirea jocului – întreabă dacă vrei joc nou sau să încarci progresul.
- Jucător și hartă – obiecte cu proprietăți și metode.
- Luptă cu monștri – evenimente aleatorii în anumite locații.
- Misiune finală – găsești Cheia Magică și înfrunți Dragonul.
- Sfârșitul jocului – câștigi sau pierzi în funcție de viață și obiective.

## Cod complet al jocului final

```python
import json
import random

# ======== Clase ========
class Aventurier:
    def __init__(self, nume):
        self.nume = nume
        self.viata = 15
        self.aur = 0
        self.inventar = []

    def afiseaza_status(self):
        print(f"\n{self.nume} – Viață: {self.viata}, Aur: {self.aur}, Inventar: {self.inventar}")

    def colecteaza(self, obiect):
        self.inventar.append(obiect)
        print(f"Ai colectat {obiect}!")

    def vindeca(self):
        if "poțiune" in self.inventar:
            self.viata += 5
            self.inventar.remove("poțiune")
            print("Ai folosit o poțiune și te-ai vindecat cu 5 viață!")
        else:
            print("Nu ai nicio poțiune de folosit.")

class Monstru:
    def __init__(self, nume, viata, atac):
        self.nume = nume
        self.viata = viata
        self.atac = atac

    def ataca(self, tinta):
        print(f"{self.nume} atacă pe {tinta.nume} și îi scade {self.atac} viață!")
        tinta.viata -= self.atac

# ======== Funcții pentru salvare/încărcare ========
def salveaza_joc(jucator, locatie):
    date_joc = {
        "nume": jucator.nume,
        "viata": jucator.viata,
        "aur": jucator.aur,
        "inventar": jucator.inventar,
        "locatie": locatie
    }
    with open("save.json", "w") as f:
        json.dump(date_joc, f)
    print("Progres salvat!")

def incarca_joc():
    try:
        with open("save.json", "r") as f:
            date_joc = json.load(f)
        print("Progres încărcat!")
        return date_joc
    except FileNotFoundError:
        print("Nu există un fișier de salvare.")
        return None

# ======== Harta și descrieri ========
harta = {
    "sat": {"nord": "pădure", "est": "pajiște"},
    "pădure": {"sud": "sat", "est": "peșteră"},
    "peșteră": {"vest": "pădure", "est": "vizuina dragonului"},
    "pajiște": {"vest": "sat"},
    "vizuina dragonului": {"vest": "peșteră"}
}

descrieri = {
    "sat": "Ești în sat. Casele sunt mici și primitoare.",
    "pădure": "Pădurea e deasă și misterioasă. Poți găsi comori sau monștri.",
    "peșteră": "Peștera e întunecoasă. Se spune că ascunde o cheie magică.",
    "pajiște": "Pajiștea e liniștită, plină de flori.",
    "vizuina dragonului": "În fața ta se află Dragonul Final. Lupta decisivă începe!"
}

# ======== Evenimente speciale ========
def intalnire_monstru(jucator):
    monstru = Monstru("Lup sălbatic", random.randint(4, 8), random.randint(1, 3))
    print(f"\nUn {monstru.nume} apare!")
    while monstru.viata > 0 and jucator.viata > 0:
        actiune = input("Ataci sau fugi? ").lower()
        if actiune == "ataci":
            daune = random.randint(1, 4)
            monstru.viata -= daune
            print(f"Ai lovit monstrul cu {daune} daune!")
            if monstru.viata <= 0:
                print("Ai învins monstrul și primești 3 aur.")
                jucator.aur += 3
                break
            monstru.ataca(jucator)
        elif actiune == "fugi":
            print("Ai fugit din luptă!")
            break
        else:
            print("Comandă necunoscută.")

def eveniment_padure(jucator):
    if random.randint(1, 2) == 1:
        intalnire_monstru(jucator)
    else:
        print("Ai găsit o poțiune în pădure!")
        jucator.colecteaza("poțiune")

def eveniment_pestera(jucator):
    if "cheie magică" not in jucator.inventar:
        print("Ai găsit Cheia Magică!")
        jucator.colecteaza("cheie magică")
    else:
        print("Peștera e goală acum.")

def lupta_finala(jucator):
    dragon = Monstru("Dragonul Final", 15, 4)
    print("\nDragonul Final își aruncă flăcările asupra ta!")
    while dragon.viata > 0 and jucator.viata > 0:
        actiune = input("Ataci sau folosești poțiune? ").lower()
        if actiune == "ataci":
            daune = random.randint(2, 5)
            dragon.viata -= daune
            print(f"Ai lovit dragonul cu {daune} daune!")
            if dragon.viata <= 0:
                print("Ai învins Dragonul Final! Lumea e salvată!")
                return True
            dragon.ataca(jucator)
        elif actiune == "poțiune":
            jucator.vindeca()
        else:
            print("Comandă necunoscută.")
    return False

# ======== Joc principal ========
def joc():
    # Pornire: încarcă sau joc nou
    opt = input("Vrei să încarci jocul salvat? (da/nu) ").lower()
    if opt == "da":
        date = incarca_joc()
        if date:
            jucator = Aventurier(date["nume"])
            jucator.viata = date["viata"]
            jucator.aur = date["aur"]
            jucator.inventar = date["inventar"]
            locatie = date["locatie"]
        else:
            jucator = Aventurier("Eliza")
            locatie = "sat"
    else:
        jucator = Aventurier("Eliza")
        locatie = "sat"

    # Bucla jocului
    while True:
        print("\n" + descrieri[locatie])
        jucator.afiseaza_status()
        print("Direcții disponibile:", ", ".join(harta[locatie].keys()))

        comanda = input("Ce faci? (nord/sud/est/vest/salveaza/exit) ").lower()

        if comanda == "salveaza":
            salveaza_joc(jucator, locatie)
        elif comanda == "exit":
            print("Ai încheiat jocul.")
            break
        elif comanda in harta[locatie]:
            locatie = harta[locatie][comanda]

            # Evenimente în funcție de locație
            if locatie == "pădure":
                eveniment_padure(jucator)
            elif locatie == "peșteră":
                eveniment_pestera(jucator)
            elif locatie == "vizuina dragonului":
                if "cheie magică" in jucator.inventar:
                    rezultat = lupta_finala(jucator)
                    if rezultat:
                        break
                else:
                    print("Ușa magică e încuiată. Îți trebuie Cheia Magică!")
                    locatie = "peșteră"
        else:
            print("Nu poți merge în acea direcție.")

        # Condiție de pierdere
        if jucator.viata <= 0:
            print("Ai murit în aventură. Joc terminat.")
            break

# Pornire joc
joc()
```

## Cum să extinzi jocul după capitolul 12

- Adaugă niveluri și experiență (XP).
- Creează mai mulți monștri cu comportamente diferite.
- Adaugă magazin pentru cumpărarea armelor și armurilor.
- Creează un final alternativ dacă jucătorul adună toate comorile ascunse.

Iată o versiune extinsă și detaliată a secțiunii „Structura jocului” din Capitolul 12, astfel încât să fie clar cum se leagă toate elementele în jocul final:

## Structura jocului – cum funcționează aventura completă

Pentru jocul nostru final, vom combina toate mecanicile învățate în capitolele anterioare. Iată cum este organizat jocul pas cu pas:

### 1. Pornirea jocului

- Întrebarea inițială: „Vrei să încarci progresul salvat?”
- Dacă jucătorul alege DA:
Se citește fișierul JSON (save.json).
Se reconstruiește starea jucătorului (viață, aur, inventar, locație).
- Dacă jucătorul alege NU sau nu există salvare:
Se creează un jucător nou (Eliza) și se pornește în sat.
- Ce înveți aici: Citirea fișierelor, folosirea JSON și reconstruirea obiectelor din date salvate.

### 2. Harta și locațiile

- Structură: Harta este un dicționar cu locații conectate prin direcții (nord, sud, est, vest).
- Descrieri: Fiecare locație are o descriere text pentru atmosferă.
- Navigare: La fiecare pas, jucătorul vede direcțiile posibile și alege unde să meargă.
- Ce înveți aici: Dicționare imbricate, afișarea opțiunilor dinamice și buclă principală de joc.

### 3. Starea jucătorului

- Proprietăți urmărite:
viata – scade la atacuri, crește cu poțiuni sau odihnă.
aur – câștigat din lupte și evenimente.
inventar – listă cu obiectele colectate (poțiuni, Cheia Magică).
locatie – unde se află pe hartă.
- Metode principale:
afiseaza_status() – arată viața, aurul și inventarul curent.
colecteaza() – adaugă un obiect în inventar.
vindeca() – folosește poțiuni pentru viață.
- Ce înveți aici: Cum clasele grupează date și comportamente, și cum să manipulezi obiectele.

### 4. Evenimente aleatorii

- Pădure:
Poți găsi o poțiune sau poți întâlni un lup care atacă.
- Peșteră:
Aici găsești Cheia Magică dacă nu o ai deja.
- Pajiște:
Obții aur din culesul florilor.
- Vizuină:
Locul luptei finale cu Dragonul, disponibilă doar dacă ai Cheia Magică.
- Ce înveți aici: Folosirea random pentru a crea varietate și rejucabilitate.

### 5. Sistemul de luptă

- Lupte normale: Întâlniri cu lupi sălbatici în pădure.
- Lupta finală: Confruntarea cu Dragonul Final:
Jucătorul poate ataca sau folosi poțiuni.
Dragonul atacă după fiecare tură a jucătorului.
Jocul se termină cu victorie dacă dragonul ajunge la 0 viață.
- Ce înveți aici: Buclă de luptă, verificarea condițiilor de victorie/pierdere.

### 6. Salvarea progresului

Oricând, jucătorul poate scrie salveaza pentru a salva starea curentă:
Nume, viață, aur, inventar, locație.
Salvarea se face în fișier JSON (save.json).
La pornirea jocului, jucătorul poate încărca fișierul pentru a continua.
- Ce înveți aici: Persistența datelor și manipularea fișierelor JSON.

### 7. Condiții de final

Victorie:
Jucătorul obține Cheia Magică și învinge Dragonul Final.
Înfrângere:
Jucătorul moare (viață ≤ 0).
Ieșire:
Jucătorul tastează exit și termină jocul oricând.
- Ce înveți aici: Condiții finale clare și feedback pentru jucător.

### 8. Extensii posibile

Adăugarea de misiuni secundare (colectează flori, salvează un sat).
Magazin în sat pentru cumpărat arme și armuri.
Mai multe tipuri de monștri cu abilități diferite.
Niveluri de dificultate (mod ușor, normal, greu).

Vrei să fac și o schemă vizuală pentru această structură (un fel de hartă logică cu pași și săgeți)?
Să fie în stil simplu pentru copii sau stil mai serios pentru învățare tehnică?

Iată o secțiune suplimentară pentru Capitolul 12, unde prezentăm pe scurt alte funcționalități ale limbajului Python și modul în care pot fi folosite pentru a extinde jocul după ce copilul stăpânește conceptele de bază:

## Ce alte funcționalități oferă Python și cum le putem folosi pentru a extinde jocul?

Acum că ai învățat elementele de bază ale Python și ai creat un joc complet de aventură, ești pregătit să explorezi caracteristici mai avansate ale limbajului. Acestea te vor ajuta să faci jocul tău mai mare, mai amuzant și mai interactiv.

### 1. Module și pachete externe

Python are mii de biblioteci create de comunitate: pentru grafică, sunet, baze de date și multe altele.
Exemple utile pentru jocuri:
pygame – pentru a transforma jocul text într-un joc cu grafică 2D.
playsound sau pygame.mixer – pentru efecte sonore (sunet de sabie, zgomotul dragonului).
colorama – pentru a colora textul în terminal (verde pentru viață, roșu pentru atac).

### 2. Programare Orientată pe Obiecte avansată (OOP)

```python
Poți crea clase derivate (moștenire) pentru diferite tipuri de monștri:
```

Monstru → Goblin, Dragon, Vampir.
Poți folosi proprietăți private sau metode speciale pentru comportamente unice.
Astfel, jocul devine mai modular și mai ușor de extins.

### 3. Salvarea avansată a datelor

În loc de un singur fișier JSON, poți salva mai multe sloturi de joc (save1.json, save2.json).
Poți folosi formate mai complexe precum SQLite (o bază de date mică) pentru progres și scoruri.
Poți adăuga autosave când jucătorul termină o misiune.

### 4. Manipularea timpului și efecte dinamice

Modulul time îți permite să creezi pauze dramatice sau cronometre.
Modulul datetime poate face evenimente speciale (zi/noapte, bonusuri zilnice).

### 5. Generatoare și evenimente infinite

Cu generatoare (yield) poți crea evenimente care apar treptat, fără să încarci toată memoria.
Exemple: apariția aleatorie a monștrilor, recompense diferite la fiecare explorare.

### 6. Decoratori și funcții avansate

Decoratorii pot adăuga comportamente suplimentare funcțiilor tale (ex. log de acțiuni, contorizarea timpului de joc).
Funcțiile lambda pot fi folosite pentru acțiuni scurte și rapide (ex. calcule simple de scor).

### 7. Extinderea hărții și a poveștii

Folosește fișiere externe (ex. JSON) pentru a defini locațiile și misiunile, astfel încât să poți schimba povestea fără să rescrii codul.
Creează capitole suplimentare: după ce învingi Dragonul, poți descoperi o nouă insulă magică!

### 8. Interfață grafică (GUI)

Cu biblioteci precum tkinter sau pygame, poți crea o fereastră grafică cu butoane și imagini.
Astfel, jocul text poate deveni un joc vizual cu hărți și personaje desenate.

### 9. Sunete și muzică

Poți adăuga muzică de fundal și efecte sonore pentru acțiuni:
sunet când găsești o comoară;
efect de „foc” când dragonul atacă.

### 10. Conectarea la internet

Poți salva scorurile într-o bază de date online și să faci un clasament al jucătorilor.
Poți chiar adăuga mod multiplayer simplu, unde doi jucători se conectează prin internet.

## De ce e important să explorezi aceste funcționalități?

Îți vei dezvolta creativitatea – poți transforma un joc text simplu într-o aventură completă.
Vei învăța programare modernă – biblioteci, obiecte, baze de date.
Vei putea crea proiecte mai mari și poate chiar primul tău joc publicat!

Vrei să fac și o casetă colorată cu „Idei pentru extinderea jocului” (cu 3-4 exemple scurte și amuzante)?
Să fie în același stil prietenos pentru copii ca restul cărții?
Înțeleg! Hai să fac lista și mai bogată, adăugând încă 5 exemple creative de jocuri text pe care copiii le pot face cu cunoștințele din carte (ajungem la 15 exemple în total):

### 11. Căutarea Comorii (Treasure Hunt)

Ce este: Explorezi o hartă pentru a găsi comori ascunse, dar ai un număr limitat de mișcări.
Ce folosești: Dicționare pentru hartă, random pentru plasarea comorilor, bucle și condiții.
Extensie: Adaugă indicii („Mai cald”, „Mai rece”) când te apropii de comoară.

### 12. Ferma Virtuală (Farm Game)

Ce este: Ai o fermă unde plantezi semințe, le uzi și le culegi pentru profit.
Ce folosești: Dicționare pentru inventar, funcții pentru creștere plante, bucle pentru trecerea zilelor.
Extensie: Adaugă animale (găini, vaci) și evenimente (furtuni care afectează recolta).

### 13. Detectivul (Mystery Solver)

Ce este: Rezolvi un mister investigând locații și interogând personaje.
Ce folosești: Liste și dicționare pentru indicii, condiții pentru progres, clase pentru NPC-uri.
Extensie: Adaugă mai multe finaluri în funcție de deciziile tale.

### 14. Cursa de Obstacole (Text Obstacle Race)

Ce este: Trebuie să alegi rapid cum să treci obstacole (sari, te ferești, te târăști).
Ce folosești: Input rapid, condiții, random pentru apariția obstacolelor.
Extensie: Adaugă un sistem de scor și cronometru pentru viteză.

### 15. Planeta Necunoscută (Space Survival)

Ce este: Aterizezi pe o planetă străină și trebuie să supraviețuiești colectând resurse și reparând nava.
Ce folosești: Hărți, clase pentru resurse și inamici, evenimente aleatorii, inventar avansat.
Extensie: Adaugă mai multe planete și posibilitatea de a construi baze.

## Rezumat – 15 jocuri pe care le poți crea

X și Zero (Tic-Tac-Toe)
Spânzurătoarea (Hangman)
Joc de Ghicitori (Quiz Magic)
Simon Says – Joc de Memorie
Aventură în Labirint
Joc cu Zaruri Magice
Joc de Comerț (Magazinul Aventurierului)
Mini-RPG cu Niveluri
Joc de Cuvinte Amestecate (Word Jumble)
Joc de Supraviețuire (Survival Text Game)
Căutarea Comorii (Treasure Hunt)
Ferma Virtuală (Farm Game)
Detectivul (Mystery Solver)
Cursa de Obstacole (Text Obstacle Race)
Planeta Necunoscută (Space Survival)

Vrei să fac acum o pagină specială în carte cu aceste 15 idei prezentate ca mini-postere ilustrate (iconițe mici pentru fiecare joc)?
Sau preferi o singură ilustrație cu toate ideile reprezentate într-un colaj jucăuș (o tablă de idei pentru copii)?

Iată o listă cu jocuri simple care pot fi implementate în Python doar cu text (fără grafica avansată), perfecte pentru învățarea treptată a programării și potrivite pentru capitolele următoare ale cărții:

## 1. X și Zero (Tic-Tac-Toe)

Concept: Două persoane (sau jucător vs. calculator) pun X și O pe o tablă 3×3 până când cineva aliniază trei simboluri.
- Ce înveți: Lucrul cu liste bidimensionale, verificarea condițiilor de câștig, alternarea jucătorilor.

## 2. Spânzurătoarea (Hangman)

Concept: Calculatorul alege un cuvânt secret, iar jucătorul ghicește literele. La fiecare greșeală se „desenează” spânzurătoarea în text.
- Ce înveți: Buclă while, verificarea literelor, afișarea progresului cu _.

## 3. Ghicirea Numărului (Guess the Number)

Concept: Calculatorul alege un număr aleator, iar jucătorul încearcă să-l ghicească, primind indicii „mai mare” sau „mai mic”.
- Ce înveți: Numere aleatorii (random.randint), condiții if/elif/else.

## 4. Aventura în Labirint

Concept: Jucătorul navighează printr-un labirint descris în text (alegeri: nord, sud, est, vest) până găsește ieșirea.
- Ce înveți: Structurarea locațiilor cu dicționare, buclă principală de joc.

## 5. Joc de Luptă Simplă

Concept: Jucătorul întâlnește monștri aleatori și alege acțiuni (atac, apărare, fugă). Rezultatul e bazat pe zaruri sau aleatoriu.
- Ce înveți: Funcții, variabile pentru viață și aur, evenimente aleatorii.

## 6. Joc de Magazin / Comerț

Concept: Jucătorul are aur și cumpără obiecte de la un magazin virtual. Poate vinde sau folosi obiecte.
- Ce înveți: Dicționare pentru inventar, funcții pentru tranzacții.

## 7. Joc de Cuvinte (Word Jumble)

Concept: Calculatorul amestecă literele unui cuvânt, iar jucătorul trebuie să-l ghicească.
- Ce înveți: Manipularea șirurilor de caractere și liste, amestecarea cu random.shuffle.

## 8. Quiz cu Întrebări

Concept: Jucătorul răspunde la o serie de întrebări cu variante multiple sau răspuns liber.
- Ce înveți: Structuri de date pentru întrebări, verificarea răspunsurilor, scor.

## 9. Joc de Aventură cu Inventar

Concept: Jucătorul explorează locații (sat, pădure, peșteră), adună obiecte și le folosește pentru a rezolva puzzle-uri.
- Ce înveți: Liste și dicționare combinate, funcții, condiții multiple.

## 10. Zaruri Magice (Dice Game)

Concept: Jucătorul aruncă zaruri și trebuie să obțină o anumită combinație pentru a câștiga (ex. scor peste 15).
- Ce înveți: Funcții, generarea numerelor aleatorii, bucle.

## 11. Blackjack Simplificat

Concept: Jucătorul primește cărți și încearcă să obțină 21 puncte fără să-l depășească.
- Ce înveți: Liste, alegeri aleatorii, condiții complexe.

## 12. Joc de „Simon Says” Textual

Concept: Calculatorul generează o secvență de cuvinte (sau direcții), iar jucătorul trebuie să o repete corect.
- Ce înveți: Liste, memorare și verificarea inputului pas cu pas.

