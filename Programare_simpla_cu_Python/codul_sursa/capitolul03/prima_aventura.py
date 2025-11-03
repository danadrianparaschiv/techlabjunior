# Starea inițială
viata = 10
aur = 0
inventar = ["sabie"]

print("Bun venit în aventură!")
print("Ai", viata, "viață și", aur, "aur.")
print("În inventarul tău se află:", inventar)

# Alegerea locației
loc = input("Unde mergi? (padure/pestera) ")

if loc == "padure":
    print("Ai găsit 5 monede de aur!")
    aur += 5
elif loc == "pestera":
    print("Peștera este întunecoasă… pierzi 2 viață.")
    viata -= 2
else:
    print("Stai în sat și te odihnești.")

# Cumperi o poțiune dacă ai aur
if aur >= 5:
    cumpara = input("Vrei să cumperi o poțiune pentru 5 aur? (da/nu) ")
    if cumpara == "da":
        inventar.append("poțiune")
        aur -= 5
        print("Ai cumpărat o poțiune!")

# Finalul misiunii
print("Inventarul final:", inventar)
print("Viață:", viata, "| Aur:", aur)
