import random

viata = 10
aur = 0
inventar = ["sabie"]

print("Începe aventura ta plină de surprize!")

while viata > 0:
    actiune = input("\nUnde vrei să mergi? (padure/pestera/exit) ")

    if actiune == "exit":
        print("Ai ales să închei aventura.")
        break

    if actiune == "padure":
        # Șansă să găsești aur sau să întâlnești un monstru
        if random.randint(1, 2) == 1:
            aur_gasit = random.randint(1, 5)
            aur += aur_gasit
            print(f"Ai găsit {aur_gasit} monede de aur!")
        else:
            print("Un monstru apare în pădure!")
            viata_monstru = random.randint(5, 10)
            while viata_monstru > 0 and viata > 0:
                atac = random.randint(1, 4)
                viata_monstru -= atac
                print(f"Lovești monstrul cu {atac} puncte!")

                if viata_monstru <= 0:
                    print("Ai învins monstrul și câștigi 2 aur!")
                    aur += 2
                    break

                atac_monstru = random.randint(1, 3)
                viata -= atac_monstru
                print(f"Monstrul te lovește cu {atac_monstru} puncte!")

    elif actiune == "pestera":
        if aur >= 5:
            print("Cumperi o poțiune magică și câștigi 3 viață!")
            inventar.append("poțiune magică")
            aur -= 5
            viata += 3
        else:
            print("Nu ai suficient aur. Peștera e pustie.")

    else:
        print("Loc necunoscut. Alege padure, pestera sau exit.")

print("\nAventura s-a încheiat!")
print("Inventarul tău:", inventar)
print("Aur:", aur, "| Viață:", viata)
