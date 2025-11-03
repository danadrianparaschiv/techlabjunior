viata = 10
aur = 0
inventar = ["sabie"]

print("Bun venit în aventura ta!")
print("Scrie 'exit' dacă vrei să închei jocul.")

while viata > 0:
    print("\nAi", viata, "viață și", aur, "aur.")
    print("Locuri disponibile: sat / pădure / peșteră")
    loc = input("Unde vrei să mergi? ")

    if loc == "exit":
        print("Ai ales să părăsești aventura.")
        break

    if loc == "sat":
        print("Te odihnești și recuperezi 2 viață.")
        viata += 2
    elif loc == "pădure":
        print("Ai găsit 3 aur, dar te-a zgâriat un lup (pierzi 1 viață).")
        aur += 3
        viata -= 1
    elif loc == "peșteră":
        if aur >= 5:
            print("Plătești 5 aur și găsești o poțiune magică.")
            inventar.append("poțiune magică")
            aur -= 5
        else:
            print("Peștera e periculoasă și pierzi 3 viață!")
            viata -= 3
    else:
        print("Nu știu locul acesta. Alege sat, pădure sau peșteră.")

print("\nJoc încheiat!")
print("Inventar final:", inventar)
print("Aur:", aur, "| Viață:", viata)
