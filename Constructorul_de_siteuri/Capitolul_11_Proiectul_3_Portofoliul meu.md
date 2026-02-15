# Capitolul 11: Proiectul 3 — Portofoliul meu 🌐

> *„Cel mai bun mod de a-ți demonstra abilitățile este prin ceea ce ai creat."*
> — adaptat

---

## Ce vei construi în acest capitol

Un **site web personal complet** — portofoliul tău de programator! Acesta este proiectul final al cărții, și va combina absolut tot ce ai învățat.

```
  ┌─────────────────────────────────────────────────────┐
  │  🚀 Prenume Nume          Acasă  Proiecte  Contact  │
  ├─────────────────────────────────────────────────────┤
  │                                                     │
  │            Salut! Sunt [Numele tău].                │
  │        Construiesc lucruri pe web. 🌐              │
  │                                                     │
  │              [ Vezi proiectele ]                     │
  │                                                     │
  ├─────────────────────────────────────────────────────┤
  │                                                     │
  │              DESPRE MINE                            │
  │                                                     │
  │    Am [x] ani și sunt pasionat de...               │
  │    ┌──────┐  HTML  CSS  JavaScript  Canvas          │
  │    │ foto │                                        │
  │    └──────┘                                        │
  │                                                     │
  ├─────────────────────────────────────────────────────┤
  │                                                     │
  │              PROIECTELE MELE                        │
  │                                                     │
  │    ┌──────────┐  ┌──────────┐  ┌──────────┐       │
  │    │ 🧠 Quiz │  │ 🌟 Catch │  │ 📝 ToDo │       │
  │    │  Game   │  │the Stars │  │  List    │       │
  │    └──────────┘  └──────────┘  └──────────┘       │
  │                                                     │
  ├─────────────────────────────────────────────────────┤
  │                                                     │
  │              CONTACTEAZĂ-MĂ                        │
  │                                                     │
  │    [ Nume ]  [ Email ]  [ Mesaj ]  [ Trimite ]     │
  │                                                     │
  ├─────────────────────────────────────────────────────┤
  │         Creat cu ❤️ — 2025                          │
  └─────────────────────────────────────────────────────┘
```

### Ce vei practica:

```
  TOTUL! Acesta e proiectul care leagă întreaga carte:
  
  Cap. 2:  HTML semantic      →  Structura completă a site-ului
  Cap. 3:  CSS fundamente     →  Culori, fonturi, spațiere
  Cap. 4:  Flexbox + Responsive → Layout, grid, media queries
  Cap. 5:  Variabile JS       →  Date dinamice
  Cap. 6:  Funcții, if/else   →  Validarea formularului
  Cap. 7:  DOM + Evenimente   →  Interactivitate completă
  Cap. 8:  Proiect Quiz       →  Afișat în galerie
  Cap. 9:  Animații           →  Reveal la scroll, tranziții
  Cap. 10: Proiect Canvas     →  Afișat în galerie
```

---

## 11.1 Planificarea portofoliului

### Secțiunile site-ului

Un portofoliu bun are o structură clară. Al nostru va avea **5 secțiuni**:

```
  1. NAVBAR      — Navigare fixă în partea de sus
  2. HERO        — Prima impresie: numele tău + slogan
  3. DESPRE MINE — Cine ești, ce abilități ai
  4. PROIECTE    — Galeria cu proiectele tale
  5. CONTACT     — Formular de contact
  6. FOOTER      — Informații finale
```

### Structura fișierelor

```
  📁 portofoliu/
  ├── index.html
  ├── stil.css
  └── script.js
```

---

## 11.2 HTML — Structura completă

### `index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portofoliul Meu | Web Developer Junior</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Nunito:wght@400;600;700&family=Space+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="stil.css">
</head>
<body>

    <!-- ══════════ NAVBAR ══════════ -->
    <nav id="navbar" class="navbar">
        <div class="container nav-interior">
            <a href="#hero" class="logo">
                <span class="logo-icon">🚀</span>
                <span class="logo-text">Prenume<span class="logo-accent">Dev</span></span>
            </a>
            <ul class="nav-linkuri">
                <li><a href="#despre">Despre</a></li>
                <li><a href="#proiecte">Proiecte</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <button id="btn-meniu" class="btn-meniu" aria-label="Deschide meniul">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>

    <!-- ══════════ HERO ══════════ -->
    <header id="hero" class="hero">
        <div class="container hero-interior">
            <p class="hero-salut">👋 Salut! Mă numesc</p>
            <h1 class="hero-nume">Prenume Nume</h1>
            <h2 class="hero-subtitlu">Construiesc lucruri pe web <span class="emoji-rotate">🌐</span></h2>
            <p class="hero-desc">Am <strong>13 ani</strong> și sunt pasionat de programare web. 
            Creez site-uri, jocuri și aplicații interactive cu HTML, CSS și JavaScript.</p>
            <div class="hero-butoane">
                <a href="#proiecte" class="btn btn-primar">Vezi proiectele mele</a>
                <a href="#contact" class="btn btn-ghost">Contactează-mă</a>
            </div>
        </div>
        <div class="hero-decoratii">
            <span class="dec dec-1">&lt;/&gt;</span>
            <span class="dec dec-2">{ }</span>
            <span class="dec dec-3">#</span>
            <span class="dec dec-4">( )</span>
        </div>
    </header>

    <!-- ══════════ DESPRE MINE ══════════ -->
    <section id="despre" class="despre">
        <div class="container">
            <h2 class="sectiune-titlu reveal">
                <span class="titlu-numar">01.</span> Despre mine
            </h2>
            
            <div class="despre-continut">
                <div class="despre-text reveal">
                    <p>Salut! Sunt un tânăr programator de <strong>13 ani</strong> din 
                    <strong>România</strong>. Am descoperit programarea web acum câteva luni
                    și de atunci nu m-am mai oprit!</p>
                    
                    <p>Am început cu <strong>HTML</strong> — construind scheletul paginilor, 
                    apoi am adăugat <strong>CSS</strong> pentru design și culori, iar cu
                    <strong>JavaScript</strong> am dat viață proiectelor mele.</p>
                    
                    <p>Visul meu este să creez aplicații web care ajută oamenii și să devin
                    un programator profesionist. Când nu programez, îmi place să 
                    citesc, să joc jocuri video și să explorez lucruri noi.</p>
                </div>
                
                <div class="despre-skills reveal">
                    <h3>Tehnologii pe care le știu:</h3>
                    <div class="skills-grid">
                        <div class="skill-item">
                            <div class="skill-icon">📄</div>
                            <span class="skill-nume">HTML5</span>
                            <div class="skill-bara">
                                <div class="skill-progres" data-nivel="90"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-icon">🎨</div>
                            <span class="skill-nume">CSS3</span>
                            <div class="skill-bara">
                                <div class="skill-progres" data-nivel="85"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-icon">⚡</div>
                            <span class="skill-nume">JavaScript</span>
                            <div class="skill-bara">
                                <div class="skill-progres" data-nivel="75"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-icon">🎮</div>
                            <span class="skill-nume">Canvas</span>
                            <div class="skill-bara">
                                <div class="skill-progres" data-nivel="65"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-icon">📱</div>
                            <span class="skill-nume">Responsive</span>
                            <div class="skill-bara">
                                <div class="skill-progres" data-nivel="80"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-icon">💻</div>
                            <span class="skill-nume">VS Code</span>
                            <div class="skill-bara">
                                <div class="skill-progres" data-nivel="85"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════ PROIECTE ══════════ -->
    <section id="proiecte" class="proiecte">
        <div class="container">
            <h2 class="sectiune-titlu reveal">
                <span class="titlu-numar">02.</span> Proiectele mele
            </h2>
            <p class="sectiune-sub reveal">Fiecare proiect a fost o aventură de învățare.
            Click pe un card pentru mai multe detalii!</p>

            <div class="proiecte-grid">
                
                <!-- Proiect 1: Quiz Game -->
                <div class="proiect-card reveal">
                    <div class="proiect-header" style="background: linear-gradient(135deg, #667eea, #764ba2);">
                        <span class="proiect-emoji">🧠</span>
                    </div>
                    <div class="proiect-body">
                        <h3>Quiz Game</h3>
                        <p>Joc de cultură generală cu 8 întrebări, scor în timp real, 
                        feedback vizual și ecran de rezultat personalizat.</p>
                        <div class="proiect-tags">
                            <span class="tag">HTML</span>
                            <span class="tag">CSS</span>
                            <span class="tag">JavaScript</span>
                            <span class="tag">DOM</span>
                        </div>
                        <div class="proiect-linkuri">
                            <a href="#" class="proiect-link">Demo live →</a>
                            <a href="#" class="proiect-link secundar">Cod sursă</a>
                        </div>
                    </div>
                </div>

                <!-- Proiect 2: Catch the Stars -->
                <div class="proiect-card reveal">
                    <div class="proiect-header" style="background: linear-gradient(135deg, #0f0c29, #302b63);">
                        <span class="proiect-emoji">🌟</span>
                    </div>
                    <div class="proiect-body">
                        <h3>Catch the Stars</h3>
                        <p>Joc 2D pe Canvas — prinde stelele care cad, evită bombele! 
                        Cu niveluri progresive, power-up-uri și scor.</p>
                        <div class="proiect-tags">
                            <span class="tag">Canvas</span>
                            <span class="tag">JavaScript</span>
                            <span class="tag">Game Loop</span>
                            <span class="tag">Coliziuni</span>
                        </div>
                        <div class="proiect-linkuri">
                            <a href="#" class="proiect-link">Demo live →</a>
                            <a href="#" class="proiect-link secundar">Cod sursă</a>
                        </div>
                    </div>
                </div>

                <!-- Proiect 3: To-Do List -->
                <div class="proiect-card reveal">
                    <div class="proiect-header" style="background: linear-gradient(135deg, #48BB78, #38A169);">
                        <span class="proiect-emoji">📝</span>
                    </div>
                    <div class="proiect-body">
                        <h3>Lista de sarcini</h3>
                        <p>Aplicație interactivă de to-do list cu adăugare, 
                        bifare, ștergere și statistici în timp real.</p>
                        <div class="proiect-tags">
                            <span class="tag">HTML</span>
                            <span class="tag">CSS</span>
                            <span class="tag">JavaScript</span>
                            <span class="tag">classList</span>
                        </div>
                        <div class="proiect-linkuri">
                            <a href="#" class="proiect-link">Demo live →</a>
                            <a href="#" class="proiect-link secundar">Cod sursă</a>
                        </div>
                    </div>
                </div>

                <!-- Proiect 4: Landing Page Animată -->
                <div class="proiect-card reveal">
                    <div class="proiect-header" style="background: linear-gradient(135deg, #1a1a2e, #16213e);">
                        <span class="proiect-emoji">✨</span>
                    </div>
                    <div class="proiect-body">
                        <h3>Landing Page Animată</h3>
                        <p>Pagină de prezentare cu animații la scroll, numere animate, 
                        particule decorative și design responsive.</p>
                        <div class="proiect-tags">
                            <span class="tag">CSS Animations</span>
                            <span class="tag">IntersectionObserver</span>
                            <span class="tag">Responsive</span>
                        </div>
                        <div class="proiect-linkuri">
                            <a href="#" class="proiect-link">Demo live →</a>
                            <a href="#" class="proiect-link secundar">Cod sursă</a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- ══════════ CONTACT ══════════ -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="sectiune-titlu reveal">
                <span class="titlu-numar">03.</span> Contactează-mă
            </h2>
            <p class="sectiune-sub reveal">Ai o întrebare sau vrei să lucrăm împreună la un proiect?
            Trimite-mi un mesaj!</p>

            <div class="contact-form-container reveal">
                <div id="form-succes" class="form-succes ascuns">
                    <div class="succes-icon">🎉</div>
                    <h3>Mesaj trimis!</h3>
                    <p>Mulțumesc pentru mesaj! Voi răspunde cât de curând posibil.</p>
                </div>

                <div id="form-container">
                    <div class="form-rand">
                        <div class="form-grup">
                            <label for="input-nume">Numele tău</label>
                            <input type="text" id="input-nume" placeholder="Ex: Maria Popescu">
                            <span class="form-eroare" id="eroare-nume"></span>
                        </div>
                        <div class="form-grup">
                            <label for="input-email">Email</label>
                            <input type="email" id="input-email" placeholder="Ex: maria@email.com">
                            <span class="form-eroare" id="eroare-email"></span>
                        </div>
                    </div>
                    <div class="form-grup">
                        <label for="input-mesaj">Mesajul tău</label>
                        <textarea id="input-mesaj" rows="5" placeholder="Scrie mesajul tău aici..."></textarea>
                        <span class="form-eroare" id="eroare-mesaj"></span>
                    </div>
                    <button id="btn-trimite" class="btn btn-primar btn-trimite">
                        Trimite mesajul ✉️
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- ══════════ FOOTER ══════════ -->
    <footer class="footer">
        <div class="container footer-interior">
            <p class="footer-text">Creat cu ❤️ de <strong>Prenume Nume</strong></p>
            <p class="footer-sub">Constructorul de Site-uri — Programare web pentru copii curioși</p>
            <div class="footer-linkuri">
                <a href="#hero">Sus ↑</a>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

---

## 11.3 CSS — Designul complet

### `stil.css`:

```css
/* ══════════════════════════════
   RESET ȘI VARIABILE
   ══════════════════════════════ */
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
    --primar: #5A67D8;
    --primar-inchis: #434190;
    --accent: #F6E05E;
    --text: #2D3748;
    --text-slab: #718096;
    --fundal: #F7FAFC;
    --fundal-card: #FFFFFF;
    --border: #E2E8F0;
    --raza: 14px;
}

body {
    font-family: "Nunito", sans-serif;
    color: var(--text);
    background-color: var(--fundal);
    line-height: 1.7;
    overflow-x: hidden;
}

.container {
    max-width: 1040px;
    margin: 0 auto;
    padding: 0 24px;
}

.ascuns { display: none !important; }

/* ══════════════════════════════
   NAVBAR
   ══════════════════════════════ */
.navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 100;
    background-color: rgba(247, 250, 252, 0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    padding: 10px 0;
    transition: box-shadow 0.3s;
}

.navbar.scrolled {
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}

.nav-interior {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
}

.logo-icon { font-size: 22px; }

.logo-text {
    font-family: "Fredoka", sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--text);
}

.logo-accent { color: var(--primar); }

.nav-linkuri {
    display: flex;
    gap: 4px;
    list-style: none;
}

.nav-linkuri a {
    text-decoration: none;
    color: var(--text-slab);
    font-weight: 600;
    font-size: 15px;
    padding: 8px 16px;
    border-radius: 8px;
    transition: color 0.2s, background-color 0.2s;
}

.nav-linkuri a:hover {
    color: var(--primar);
    background-color: #EBF4FF;
}

/* Buton meniu mobil (hamburger) */
.btn-meniu {
    display: none;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 5px;
}

.btn-meniu span {
    display: block;
    width: 24px;
    height: 2px;
    background-color: var(--text);
    border-radius: 2px;
    transition: transform 0.3s, opacity 0.3s;
}

/* ══════════════════════════════
   BUTOANE
   ══════════════════════════════ */
.btn {
    display: inline-block;
    font-family: "Fredoka", sans-serif;
    font-weight: 600;
    font-size: 16px;
    padding: 14px 32px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
}

.btn:hover { transform: translateY(-2px); }
.btn:active { transform: translateY(0); }

.btn-primar {
    background-color: var(--primar);
    color: white;
    box-shadow: 0 4px 12px rgba(90, 103, 216, 0.3);
}

.btn-primar:hover {
    background-color: var(--primar-inchis);
    box-shadow: 0 6px 20px rgba(90, 103, 216, 0.4);
}

.btn-ghost {
    background-color: transparent;
    color: var(--primar);
    border: 2px solid var(--primar);
}

.btn-ghost:hover {
    background-color: var(--primar);
    color: white;
}

/* ══════════════════════════════
   HERO
   ══════════════════════════════ */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 120px 0 80px;
    position: relative;
    overflow: hidden;
}

.hero-interior { max-width: 620px; }

.hero-salut {
    font-size: 18px;
    color: var(--primar);
    font-weight: 600;
    margin-bottom: 8px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.1s forwards;
}

.hero-nume {
    font-family: "Fredoka", sans-serif;
    font-size: 52px;
    font-weight: 700;
    color: var(--text);
    line-height: 1.1;
    margin-bottom: 8px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.2s forwards;
}

.hero-subtitlu {
    font-family: "Fredoka", sans-serif;
    font-size: 28px;
    font-weight: 600;
    color: var(--text-slab);
    margin-bottom: 20px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.3s forwards;
}

.hero-desc {
    font-size: 17px;
    color: var(--text-slab);
    margin-bottom: 30px;
    line-height: 1.8;
    max-width: 520px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.4s forwards;
}

.hero-butoane {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.5s forwards;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(25px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Emoji rotativ */
.emoji-rotate {
    display: inline-block;
    animation: rotireLenta 8s linear infinite;
}

@keyframes rotireLenta {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

/* Decorații flotante */
.hero-decoratii {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
}

.dec {
    position: absolute;
    font-family: "Space Mono", monospace;
    color: rgba(90, 103, 216, 0.08);
    font-size: 48px;
    font-weight: 700;
    animation: float 7s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50%      { transform: translateY(-20px); }
}

.dec-1 { top: 15%; right: 8%; animation-delay: 0s; }
.dec-2 { top: 55%; right: 15%; font-size: 36px; animation-delay: 1.5s; }
.dec-3 { bottom: 20%; right: 25%; font-size: 56px; animation-delay: 3s; }
.dec-4 { top: 35%; right: 35%; font-size: 30px; animation-delay: 4.5s; }

/* ══════════════════════════════
   TITLURI DE SECȚIUNE
   ══════════════════════════════ */
.sectiune-titlu {
    font-family: "Fredoka", sans-serif;
    font-size: 30px;
    color: var(--text);
    margin-bottom: 10px;
}

.titlu-numar {
    font-family: "Space Mono", monospace;
    color: var(--primar);
    font-size: 18px;
    margin-right: 6px;
}

.sectiune-sub {
    color: var(--text-slab);
    font-size: 16px;
    margin-bottom: 35px;
    max-width: 500px;
}

/* ══════════════════════════════
   DESPRE MINE
   ══════════════════════════════ */
.despre {
    padding: 90px 0;
}

.despre-continut {
    display: flex;
    gap: 50px;
    align-items: flex-start;
    flex-wrap: wrap;
}

.despre-text {
    flex: 1;
    min-width: 280px;
}

.despre-text p {
    color: var(--text-slab);
    margin-bottom: 14px;
    font-size: 16px;
}

.despre-text strong { color: var(--text); }

.despre-skills {
    flex: 1;
    min-width: 280px;
}

.despre-skills h3 {
    font-family: "Fredoka", sans-serif;
    font-size: 18px;
    color: var(--text);
    margin-bottom: 18px;
}

.skills-grid {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.skill-item {
    display: flex;
    align-items: center;
    gap: 12px;
}

.skill-icon { font-size: 22px; flex-shrink: 0; }

.skill-nume {
    font-weight: 600;
    font-size: 14px;
    color: var(--text);
    min-width: 90px;
}

.skill-bara {
    flex: 1;
    height: 8px;
    background-color: #EDF2F7;
    border-radius: 4px;
    overflow: hidden;
}

.skill-progres {
    height: 100%;
    width: 0;
    background: linear-gradient(90deg, var(--primar), #667eea);
    border-radius: 4px;
    transition: width 1s ease;
}

/* ══════════════════════════════
   PROIECTE
   ══════════════════════════════ */
.proiecte {
    padding: 90px 0;
    background-color: white;
}

.proiecte-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
}

.proiect-card {
    background-color: var(--fundal);
    border-radius: var(--raza);
    overflow: hidden;
    border: 1px solid var(--border);
    transition: transform 0.3s, box-shadow 0.3s;
}

.proiect-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.08);
}

.proiect-header {
    height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.proiect-emoji { font-size: 52px; }

.proiect-body { padding: 22px; }

.proiect-body h3 {
    font-family: "Fredoka", sans-serif;
    font-size: 20px;
    color: var(--text);
    margin-bottom: 8px;
}

.proiect-body p {
    font-size: 14px;
    color: var(--text-slab);
    margin-bottom: 14px;
    line-height: 1.6;
}

.proiect-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 16px;
}

.tag {
    font-family: "Space Mono", monospace;
    font-size: 11px;
    padding: 4px 10px;
    background-color: #EBF4FF;
    color: var(--primar);
    border-radius: 20px;
    font-weight: 600;
}

.proiect-linkuri {
    display: flex;
    gap: 16px;
}

.proiect-link {
    font-size: 14px;
    font-weight: 700;
    text-decoration: none;
    color: var(--primar);
    transition: color 0.2s;
}

.proiect-link:hover { color: var(--primar-inchis); }

.proiect-link.secundar {
    color: var(--text-slab);
}

.proiect-link.secundar:hover { color: var(--text); }

/* ══════════════════════════════
   CONTACT
   ══════════════════════════════ */
.contact {
    padding: 90px 0;
}

.contact-form-container {
    max-width: 600px;
    background-color: white;
    border-radius: var(--raza);
    padding: 35px;
    border: 1px solid var(--border);
}

.form-rand {
    display: flex;
    gap: 16px;
}

.form-grup {
    flex: 1;
    margin-bottom: 18px;
}

.form-grup label {
    display: block;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 6px;
    color: var(--text);
}

.form-grup input,
.form-grup textarea {
    width: 100%;
    padding: 12px 16px;
    font-family: "Nunito", sans-serif;
    font-size: 15px;
    border: 2px solid var(--border);
    border-radius: 10px;
    outline: none;
    transition: border-color 0.2s;
    resize: vertical;
}

.form-grup input:focus,
.form-grup textarea:focus {
    border-color: var(--primar);
}

.form-grup input.invalid,
.form-grup textarea.invalid {
    border-color: #E53E3E;
}

.form-eroare {
    display: block;
    font-size: 12px;
    color: #E53E3E;
    margin-top: 4px;
    min-height: 18px;
}

.btn-trimite {
    width: 100%;
    padding: 16px;
    font-size: 17px;
    margin-top: 4px;
}

/* Mesaj de succes */
.form-succes {
    text-align: center;
    padding: 30px;
}

.succes-icon { font-size: 52px; margin-bottom: 12px; }

.form-succes h3 {
    font-family: "Fredoka", sans-serif;
    font-size: 24px;
    color: #48BB78;
    margin-bottom: 8px;
}

.form-succes p { color: var(--text-slab); }

/* ══════════════════════════════
   FOOTER
   ══════════════════════════════ */
.footer {
    background-color: var(--text);
    color: rgba(255,255,255,0.5);
    padding: 30px 0;
    text-align: center;
}

.footer-text {
    font-size: 14px;
    margin-bottom: 4px;
}

.footer-text strong { color: rgba(255,255,255,0.8); }

.footer-sub { font-size: 12px; margin-bottom: 12px; }

.footer-linkuri a {
    color: rgba(255,255,255,0.4);
    text-decoration: none;
    font-size: 13px;
    transition: color 0.2s;
}

.footer-linkuri a:hover { color: white; }

/* ══════════════════════════════
   ANIMAȚII REVEAL (scroll)
   ══════════════════════════════ */
.reveal {
    opacity: 0;
    transform: translateY(25px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.vizibil {
    opacity: 1;
    transform: translateY(0);
}

/* ══════════════════════════════
   RESPONSIVE
   ══════════════════════════════ */
@media (max-width: 768px) {
    .hero-nume { font-size: 36px; }
    .hero-subtitlu { font-size: 22px; }
    .hero-desc { font-size: 15px; }

    .proiecte-grid { grid-template-columns: 1fr; }

    .form-rand { flex-direction: column; gap: 0; }

    .nav-linkuri { display: none; }
    .btn-meniu { display: flex; }

    .nav-linkuri.activ {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: rgba(247, 250, 252, 0.98);
        backdrop-filter: blur(12px);
        padding: 10px 20px 20px;
        border-bottom: 1px solid var(--border);
    }

    .dec { display: none; }
}

@media (max-width: 480px) {
    .hero { padding: 100px 0 60px; }
    .hero-nume { font-size: 30px; }
    .hero-subtitlu { font-size: 18px; }
    .sectiune-titlu { font-size: 24px; }

    .contact-form-container { padding: 22px; }
}
```

### Concept nou: Variabile CSS (`--primar`, `--text`, etc.)

Ai observat `:root { --primar: #5A67D8; }` la începutul CSS-ului? Acestea sunt **variabile CSS** (numite și custom properties):

```css
:root {
    --primar: #5A67D8;
    --text: #2D3748;
}

/* Le folosești cu var() */
.buton {
    background-color: var(--primar);
    color: var(--text);
}
```

Avantajul uriaș: dacă vrei să schimbi culoarea principală a întregului site, modifici **o singură linie** (valoarea variabilei), nu zeci de proprietăți individuale.

### Concept nou: CSS Grid

Pe lângă Flexbox, CSS oferă **Grid** — perfect pentru layout-uri 2D (rânduri ȘI coloane):

```css
.proiecte-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);   /* 2 coloane egale */
    gap: 24px;
}
```

```
  Flexbox = o singură direcție (rând SAU coloană)
  Grid    = două direcții simultan (rânduri ȘI coloane)
  
  grid-template-columns: repeat(2, 1fr)
  
  ┌──────────────┬──────────────┐
  │   1fr        │    1fr       │   rândul 1
  │   Card 1     │    Card 2   │
  ├──────────────┼──────────────┤
  │   Card 3     │    Card 4   │   rândul 2
  │              │              │
  └──────────────┴──────────────┘
  
  1fr = o fracțiune din spațiul disponibil
  repeat(2, 1fr) = 2 coloane egale
```

---

## 11.4 JavaScript — Interactivitate

### `script.js`:

```javascript
// ══════════════════════════════════════════════
// 🌐 PORTOFOLIUL MEU — SCRIPT PRINCIPAL
// ══════════════════════════════════════════════


// ── 1. REVEAL LA SCROLL ──

const elemReveal = document.querySelectorAll(".reveal");

const observer = new IntersectionObserver(function(entries) {
    for (let i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
            entries[i].target.classList.add("vizibil");
        }
    }
}, { threshold: 0.15 });

for (let i = 0; i < elemReveal.length; i++) {
    observer.observe(elemReveal[i]);
}


// ── 2. SKILL BARS ANIMATE ──

const despreSection = document.querySelector("#despre");
let skillsAnimated = false;

const observerSkills = new IntersectionObserver(function(entries) {
    if (entries[0].isIntersecting && !skillsAnimated) {
        skillsAnimated = true;
        let baruri = document.querySelectorAll(".skill-progres");
        for (let i = 0; i < baruri.length; i++) {
            let nivel = baruri[i].dataset.nivel;
            baruri[i].style.width = `${nivel}%`;
        }
    }
}, { threshold: 0.3 });

observerSkills.observe(despreSection);


// ── 3. NAVBAR SCROLL EFFECT ──

const navbar = document.querySelector("#navbar");

window.addEventListener("scroll", function() {
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});


// ── 4. SMOOTH SCROLL ──

const linkuriNav = document.querySelectorAll('a[href^="#"]');

for (let i = 0; i < linkuriNav.length; i++) {
    linkuriNav[i].addEventListener("click", function(e) {
        e.preventDefault();
        let targetId = this.getAttribute("href");
        let target = document.querySelector(targetId);
        
        if (target) {
            let offset = navbar.offsetHeight + 10;
            let pozitie = target.getBoundingClientRect().top + window.scrollY - offset;
            
            window.scrollTo({
                top: pozitie,
                behavior: "smooth"
            });
        }

        // Închide meniul mobil dacă e deschis
        navLinkuri.classList.remove("activ");
    });
}


// ── 5. MENIU MOBIL (HAMBURGER) ──

const btnMeniu = document.querySelector("#btn-meniu");
const navLinkuri = document.querySelector(".nav-linkuri");

btnMeniu.addEventListener("click", function() {
    navLinkuri.classList.toggle("activ");
});


// ── 6. VALIDARE FORMULAR ──

const btnTrimite = document.querySelector("#btn-trimite");
const inputNume = document.querySelector("#input-nume");
const inputEmail = document.querySelector("#input-email");
const inputMesaj = document.querySelector("#input-mesaj");
const eroareNume = document.querySelector("#eroare-nume");
const eroareEmail = document.querySelector("#eroare-email");
const eroareMesaj = document.querySelector("#eroare-mesaj");
const formContainer = document.querySelector("#form-container");
const formSucces = document.querySelector("#form-succes");


function valideazaEmail(email) {
    // Verificare simplă: conține @ și cel puțin un punct după @
    let areAt = email.includes("@");
    let parteDupaAt = email.split("@")[1];
    let arePunct = parteDupaAt && parteDupaAt.includes(".");
    return areAt && arePunct;
}


function reseteazaErori() {
    inputNume.classList.remove("invalid");
    inputEmail.classList.remove("invalid");
    inputMesaj.classList.remove("invalid");
    eroareNume.textContent = "";
    eroareEmail.textContent = "";
    eroareMesaj.textContent = "";
}


function valideazaFormular() {
    reseteazaErori();
    let valid = true;
    
    // Validare nume
    let nume = inputNume.value.trim();
    if (nume === "") {
        inputNume.classList.add("invalid");
        eroareNume.textContent = "Te rugăm să completezi numele.";
        valid = false;
    } else if (nume.length < 2) {
        inputNume.classList.add("invalid");
        eroareNume.textContent = "Numele trebuie să aibă cel puțin 2 caractere.";
        valid = false;
    }
    
    // Validare email
    let email = inputEmail.value.trim();
    if (email === "") {
        inputEmail.classList.add("invalid");
        eroareEmail.textContent = "Te rugăm să completezi emailul.";
        valid = false;
    } else if (!valideazaEmail(email)) {
        inputEmail.classList.add("invalid");
        eroareEmail.textContent = "Te rugăm să introduci un email valid.";
        valid = false;
    }
    
    // Validare mesaj
    let mesaj = inputMesaj.value.trim();
    if (mesaj === "") {
        inputMesaj.classList.add("invalid");
        eroareMesaj.textContent = "Te rugăm să scrii un mesaj.";
        valid = false;
    } else if (mesaj.length < 10) {
        inputMesaj.classList.add("invalid");
        eroareMesaj.textContent = "Mesajul trebuie să aibă cel puțin 10 caractere.";
        valid = false;
    }
    
    return valid;
}


btnTrimite.addEventListener("click", function() {
    if (valideazaFormular()) {
        // Formularul e valid! Arată mesajul de succes.
        formContainer.classList.add("ascuns");
        formSucces.classList.remove("ascuns");
        
        // Afișează în consolă datele (într-o aplicație reală, le-ai trimite la server)
        console.log("📬 Formular trimis!");
        console.log(`   Nume:  ${inputNume.value.trim()}`);
        console.log(`   Email: ${inputEmail.value.trim()}`);
        console.log(`   Mesaj: ${inputMesaj.value.trim()}`);
    }
});

// Elimină stilul de eroare când utilizatorul începe să scrie
inputNume.addEventListener("input", function() {
    inputNume.classList.remove("invalid");
    eroareNume.textContent = "";
});

inputEmail.addEventListener("input", function() {
    inputEmail.classList.remove("invalid");
    eroareEmail.textContent = "";
});

inputMesaj.addEventListener("input", function() {
    inputMesaj.classList.remove("invalid");
    eroareMesaj.textContent = "";
});
```

---

## 11.5 Ce concepte ai pus în practică

### Recapitulare tehnici folosite

```
  ┌──────────────────────────────────────────────────────────────┐
  │  CAPITOL     CONCEPT                  UNDE ÎN PORTOFOLIU    │
  ├──────────────────────────────────────────────────────────────┤
  │  Cap. 2      HTML semantic            header, nav, section,  │
  │                                       footer, article        │
  │  Cap. 3      CSS: culori, fonturi     Variabile CSS, Google  │
  │              box model                Fonts, spacing          │
  │  Cap. 4      Flexbox                  Navbar, hero, skills,  │
  │              Responsive               form, media queries    │
  │  Cap. 4      CSS Grid (NOU!)         Grila de proiecte      │
  │  Cap. 5      Variabile JS            Starea formularului    │
  │  Cap. 6      if/else, funcții        Validare formular      │
  │  Cap. 7      DOM, querySelector      Toată interactivitatea │
  │              classList, addEventListener                      │
  │  Cap. 7      Input, .value, .trim()  Formularul de contact  │
  │  Cap. 9      @keyframes              Hero fade-up, float    │
  │  Cap. 9      IntersectionObserver    Reveal la scroll       │
  │  Cap. 9      transition              Hover pe carduri, nav  │
  │  NOU         Variabile CSS (:root)   Culorile întregului site│
  │  NOU         CSS Grid                Layout-ul proiectelor   │
  │  NOU         Meniu hamburger         Navigare mobilă         │
  │  NOU         Validare formular       Secțiunea de contact    │
  │  NOU         aria-label              Accesibilitate          │
  └──────────────────────────────────────────────────────────────┘
```

### Concepte noi detaliate

#### Variabile CSS

```css
:root {
    --culoare: #5A67D8;
}

/* Avantaj: schimbi o singură linie → se schimbă peste tot */
.buton { background-color: var(--culoare); }
.link  { color: var(--culoare); }
.tag   { border-color: var(--culoare); }
```

#### CSS Grid vs Flexbox

```
  Când folosești FLEXBOX:
  • Navigarea (elemente pe o linie)
  • Alinierea pe un singur ax
  • Layout-uri simple
  
  Când folosești GRID:
  • Galerii de carduri (rânduri + coloane)
  • Layout-uri complexe cu plasare precisă
  • Când ai nevoie de control pe AMBELE axe
```

#### Validarea formularului

```
  Input utilizator
       │
       ▼
  ┌─────────────┐
  │ E gol?      │── DA ──► Eroare: "Completează câmpul"
  └──────┬──────┘
      NU │
  ┌──────▼──────┐
  │ E prea      │── DA ──► Eroare: "Minim X caractere"
  │ scurt?      │
  └──────┬──────┘
      NU │
  ┌──────▼──────┐
  │ Email valid?│── NU ──► Eroare: "Email invalid"
  │ (conține @  │
  │  și punct)  │
  └──────┬──────┘
      DA │
       ▼
  ✅ Trimite!
```

#### Meniul hamburger

Pe mobil, meniul de navigare se ascunde sub un buton cu 3 linii (☰):

```javascript
btnMeniu.addEventListener("click", function() {
    navLinkuri.classList.toggle("activ");
});
```

Clasa `activ` face meniul vizibil pe mobil cu `display: flex`.

---

## 11.6 Personalizarea — Fă-l al tău!

Acesta este **site-ul tău**. Iată ce ar trebui să personalizezi:

### Informații de bază

```
  ✏️ "Prenume Nume"    → Numele tău real
  ✏️ "13 ani"          → Vârsta ta
  ✏️ "România"         → Orașul/țara ta  
  ✏️ "PrenumeDev"      → Numele tău de brand
  ✏️ Textul "Despre"   → Povestea ta reală
```

### Culori

Schimbă variabilele CSS din `:root` pentru a personaliza întregul site:

```css
/* Tema albastră (implicit) */
:root { --primar: #5A67D8; --primar-inchis: #434190; }

/* Tema verde */
:root { --primar: #38A169; --primar-inchis: #2F855A; }

/* Tema portocalie */
:root { --primar: #DD6B20; --primar-inchis: #C05621; }

/* Tema roșie */
:root { --primar: #E53E3E; --primar-inchis: #C53030; }
```

### Proiecte

Înlocuiește link-urile `href="#"` cu link-urile reale către proiectele tale, dacă le publici online (de exemplu pe GitHub Pages).

### Nivelurile de skill

Ajustează valorile `data-nivel` pentru a reflecta încrederea ta reală:

```html
<div class="skill-progres" data-nivel="75"></div>
<!-- 75 = 75% — te simți destul de confortabil -->
```

---

## 11.7 Cum publici site-ul online (gratuit!)

Vrei ca site-ul tău să fie vizibil pe internet? Iată cum:

### Opțiunea 1: GitHub Pages (recomandat)

```
  1. Creează un cont pe github.com (gratuit, cu emailul părinților)
  2. Creează un repository nou cu numele: prenume.github.io
  3. Încarcă fișierele: index.html, stil.css, script.js
  4. Activează GitHub Pages din Settings → Pages
  5. Site-ul tău e acum live la: https://prenume.github.io 🎉
```

### Opțiunea 2: Netlify

```
  1. Creează un cont pe netlify.com (gratuit)
  2. Trage folderul proiectului în zona de upload
  3. Netlify generează automat un link
  4. Poți seta un subdomeniu personalizat gratuit
```

### Opțiunea 3: Vercel

```
  1. Creează un cont pe vercel.com (gratuit)
  2. Conectează cu GitHub sau încarcă manual
  3. Site-ul e live în câteva secunde
```

> 💡 **Sfat!**
> GitHub Pages este cea mai populară opțiune pentru portofolii de programatori. Este gratuit, simplu, și folosit de milioane de dezvoltatori din toată lumea. Plus, arată bine pe CV să ai un profil GitHub!

---

## 11.8 Greșeli frecvente (și cum le repari) 🔧

### ❌ Greșeala 1: Uiți responsive-ul pe mobil

```css
/* ❌ Cardurile se suprapun pe ecran mic */
.proiecte-grid {
    grid-template-columns: repeat(2, 1fr);
}

/* ✅ Pe mobil, treci la o singură coloană */
@media (max-width: 768px) {
    .proiecte-grid {
        grid-template-columns: 1fr;
    }
}
```

### ❌ Greșeala 2: Smooth scroll nu compensează navbar-ul fix

```javascript
// ❌ Scroll-ul duce EXACT la element — ascuns sub navbar!
target.scrollIntoView({ behavior: "smooth" });

// ✅ Calculează offset-ul pentru navbar
let offset = navbar.offsetHeight + 10;
let pozitie = target.getBoundingClientRect().top + window.scrollY - offset;
window.scrollTo({ top: pozitie, behavior: "smooth" });
```

### ❌ Greșeala 3: Validarea doar vizuală, nu logică

```javascript
// ❌ Verifică doar dacă câmpul nu e gol
if (email !== "") {
    // trimite... dar "asdfgh" nu e un email valid!
}

// ✅ Verifică și formatul
if (email !== "" && email.includes("@") && email.split("@")[1].includes(".")) {
    // acum e un email mai plauzibil
}
```

### ❌ Greșeala 4: Link-uri `#` care sar la top

```html
<!-- ❌ href="#" face pagina să sară la top -->
<a href="#">Click</a>

<!-- ✅ Folosește preventDefault() în JS -->
```

```javascript
link.addEventListener("click", function(e) {
    e.preventDefault();
    // ... acțiunea ta
});
```

---

## 11.9 Mini-quiz — Verifică ce ai învățat! ✅

**1.** Ce sunt variabilele CSS și de ce sunt utile?

**2.** Care e diferența principală dintre Flexbox și CSS Grid?

**3.** Cum faci un meniu de navigare responsive care se transformă în „hamburger" pe mobil?

**4.** Ce verificări ar trebui să facă un formular de contact înainte de „trimitere"?

**5.** Ce este `aria-label` și de ce contează?

**6.** Numește 3 platforme gratuite unde poți publica un site web.

**7.** De ce calculezi un `offset` la smooth scroll când ai navbar fix?

---

<details>
<summary>🔑 Click aici pentru răspunsuri</summary>

1. **Variabilele CSS** (custom properties) sunt valori definite cu `--nume: valoare` în `:root` și folosite cu `var(--nume)`. Sunt utile pentru că poți schimba o culoare/dimensiune **într-un singur loc** și schimbarea se propagă în tot CSS-ul.

2. **Flexbox** aranjează elementele pe **o singură axă** (rând sau coloană). **CSS Grid** controlează **ambele axe** simultan (rânduri ȘI coloane), perfect pentru galerii și layout-uri 2D.

3. Pe desktop, navbar-ul arată linkurile normal. Pe mobil (cu `@media`), ascunzi linkurile (`display: none`) și arăți un buton hamburger. La click pe hamburger, JavaScript adaugă clasa `activ` pe lista de linkuri care le face vizibile din nou.

4. Verifică dacă câmpurile nu sunt **goale**, dacă au o **lungime minimă**, și dacă emailul are un **format valid** (conține `@` și un punct după `@`). Arată mesaje de eroare clare lângă fiecare câmp problematic.

5. **`aria-label`** oferă o descriere text pentru elementele care nu au text vizibil (cum ar fi butonul hamburger ☰). E esențial pentru **accesibilitate** — citoarele de ecran folosite de persoanele cu deficiențe de vedere citesc aria-label pentru a descrie elementul.

6. **GitHub Pages**, **Netlify**, și **Vercel** — toate oferă hosting gratuit pentru site-uri statice (HTML/CSS/JS).

7. Navbar-ul fix stă **deasupra** conținutului. Fără offset, scroll-ul duce exact la secțiune, dar primele 50-60px sunt ascunse sub navbar. Scăzând `navbar.offsetHeight`, secțiunea apare corect sub navbar.

</details>

---

## 11.10 Știai că? — Curiozități din lumea tech 🤓

💼 **Portofoliul web** este cel mai important instrument pentru un programator care caută un job sau un internship. Conform studiilor, recrutorii petrec în medie doar **6 secunde** uitându-se la un CV, dar pot petrece minute explorând un portofoliu interactiv. Ai acum un avantaj uriaș!

🐙 **GitHub** a fost creat în 2008 și cumpărat de Microsoft în 2018 cu **7.5 miliarde de dolari**. Astăzi, peste 100 de milioane de programatori din toată lumea îl folosesc. Când îți publici portofoliul pe GitHub Pages, intri într-o comunitate globală de creatori.

📱 **Responsive design** a devenit esențial în 2015 când Google a anunțat „Mobilegeddon" — o actualizare a algoritmului de căutare care penaliza site-urile neadaptate pentru mobil. Astăzi, peste 60% din traficul web vine de pe telefoane mobile.

🏗️ **CSS Grid** a fost propus pentru prima dată de Microsoft în 2011 și standardizat abia în 2017. Timp de 6 ani, programatorii au folosit „hack-uri" cu `float` și `inline-block` pentru a face grid-uri. Azi ai la dispoziție un instrument nativ, elegant, și ai învățat să-l folosești!

---

## Recapitulare — Ce ai învățat în Capitolul 11

```
  CONCEPTE NOI:
  ✅ Variabile CSS (:root, var())
  ✅ CSS Grid (grid-template-columns, repeat, fr)
  ✅ Meniu hamburger responsive
  ✅ Validare formular (câmpuri goale, lungime, format email)
  ✅ aria-label pentru accesibilitate
  ✅ Publicare online (GitHub Pages, Netlify, Vercel)
  
  TEHNICI CONSOLIDATE:
  ✅ HTML semantic complet (nav, header, section, footer)
  ✅ Flexbox pentru layout-uri
  ✅ Media queries pentru responsive
  ✅ Google Fonts cu font-stacks
  ✅ IntersectionObserver pentru reveal la scroll
  ✅ Skill bars animate cu dataset
  ✅ Navbar cu efect la scroll (classList + window.scroll)
  ✅ Smooth scroll cu offset pentru navbar fix
  ✅ @keyframes (fadeUp, float, rotireLenta)
  ✅ Tranziții pe hover (carduri, butoane, linkuri)
  ✅ Delegare de evenimente și input handling
  
  PROIECT COMPLET:
  ✅ Site web personal cu 5 secțiuni! 🌐
```

---

## Ce urmează?

Ai ajuns la **ultimul capitol**! În **Capitolul 12: Ce urmează? — Drumul tău ca programator 🗺️**, vei descoperi cum să continui să înveți, ce tehnologii să explorezi mai departe, resurse gratuite incredibile, și cum să-ți transformi pasiunea în viitorul tău.

Ești aproape de final — și abia ai început! 🚀

---

> *„Web-ul este mai mult o creație socială decât una tehnică. L-am proiectat pentru un efect social — să ajute oamenii să lucreze împreună."*
> — Tim Berners-Lee, creatorul World Wide Web
