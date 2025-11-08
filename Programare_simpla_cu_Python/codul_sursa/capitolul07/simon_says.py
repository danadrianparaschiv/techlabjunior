import random
import time

def joc_simon():
    print("Bine ai venit la jocul BONUS: Simon Says!")
    print("Repetă secvența de cuvinte exact cum apare.")
    print("Scrie cuvintele separate prin spațiu.")

    directii = ["su", "jo", "st", "dr"] # sus, jos, stânga, dreapta
    secventa = []
    scor = 0

    while True:
        # Adaugă o nouă direcție aleatoare în secvență
        secventa.append(random.choice(directii))

        # Afișează secvența
        print("\nSecvența este:")
        for pas in secventa:
            print(pas)
            if secventa.index(pas) > 0:
                time.sleep(1)  # pauză scurtă pentru fiecare pas
            else:
                time.sleep(1.5)    # pauză mai lungă la început


        # Șterge ecranul cu linii noi (simulare)
        print("\n" * 20)

        # Cere jucătorului să introducă secvența
        raspuns = input("Repetă secvența: ").lower().split()

        # Verifică răspunsul
        if raspuns == secventa:
            scor += 1
            print("Corect! Scorul tău este:", scor)
        else:
            print("Greșit! Joc încheiat.")
            print("Secvența corectă era:", " ".join(secventa))
            print("Scor final:", scor)
            break

# Pornim jocul
joc_simon()