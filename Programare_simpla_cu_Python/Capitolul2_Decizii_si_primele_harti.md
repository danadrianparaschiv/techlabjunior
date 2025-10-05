# Capitolul 2 – Decizii și primele hărți ale aventurii

## De ce avem nevoie de decizii în jocuri?

În capitolul anterior, am creat un mic program care saluta jucătorul. Dar jocurile bune sunt pline de **alegeri**. Fiecare alegere schimbă povestea:

> „Vrei să intri în peșteră sau să urmezi drumul spre munte?"

Aceasta se numește **ramificare** (eng. *branching*). Vom folosi **instrucțiuni condiționale** (eng. *conditional statements*) pentru a face jocul nostru mai interesant.

## Ce vei învăța în acest capitol

- Cum să folosești instrucțiuni **if / else** pentru a lua decizii.
- Cum să verifici mai multe condiții cu **elif**.
- Cum să lucrezi cu **numere** și să faci mici calcule.
- Cum să creezi prima **hartă** (simplă) a aventurii tale.

## Instrucțiuni condiționale

### Cum funcționează if?

```python
raspuns = input("Vrei să intri în peșteră? (da/nu) ")

if raspuns == "da":
    print("Intri încet în peștera întunecoasă...")
else:
    print("Te întorci pe cărare, în siguranță.")
```

- Dacă condiția este adevărată (jucătorul scrie „da"), se execută prima ramură.
- Dacă nu, se execută ramura `else`.

### Verificarea mai multor condiții cu elif

Ce faci dacă sunt mai multe alegeri?

```python
arma = input("Ce armă alegi? (sabie/arc/băț) ")

if arma == "sabie":
    print("Ai ales sabia strălucitoare!")
elif arma == "arc":
    print("Ai ales arcul magic cu săgeți nesfârșite!")
else:
    print("Ai ales un simplu băț... noroc mult!")
```

## Lucrăm cu numere

Uneori vrei să adaugi puțină „matematică" în joc: viață, puncte, aur.

```python
aur = 10
print("Ai", aur, "monede de aur.")

cumparare = int(input("Cât aur vrei să cheltui pe o poțiune? "))
aur = aur - cumparare

print("Ți-au rămas", aur, "monede.")
```

**Observă:**

- Am folosit **`int()`** pentru a transforma textul introdus de jucător în număr (număr întreg – eng. *integer*).
- Apoi am făcut scăderea și am afișat rezultatul.

## Prima hartă a aventurii

Să facem o mini-hartă cu 3 locuri: **satul**, **pădurea** și **peștera**.

### Cod complet (prima_harta.py)

```python
print("Te afli în sat. Poți merge la pădure sau la peșteră.")

loc = input("Unde vrei să mergi? (padure/pestera) ")

if loc == "padure":
    print("În pădure auzi păsările cântând și găsești un drum ascuns.")
elif loc == "pestera":
    print("Peștera e întunecoasă și rece. Simți un curent de aer misterios.")
else:
    print("Te întorci acasă și bei o cană de ceai.")
```

## Exerciții pentru tine

1. Adaugă un al patrulea loc pe hartă: **râul**.
2. Fă ca jucătorul să primească 5 monede dacă alege pădurea.
3. Adaugă o alegere în peșteră: „Aprinzi o torță sau mergi pe întuneric?".

## Ce urmează în capitolul 3

- Cum să **salvăm datele jucătorului** (inventar, viață, aur).
- Cum să facem **hărți mai mari** și să ne mișcăm între locații.
- Cum să începem să creăm **o poveste reală** cu misiuni și obiective.