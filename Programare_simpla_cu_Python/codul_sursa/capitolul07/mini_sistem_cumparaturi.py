def afiseaza_inventar(inventar):
    print("\nInventarul tău:")
    for obiect, cantitate in inventar.items():
        print(f"- {obiect}: {cantitate}")

# Inventarul și aurul
inventar = {"sabie": 1}
aur = 10

# Magazinul
magazin = {
    "potiune": 3,
    "scut": 5
}

print("Bun venit la magazinul magic!")
afiseaza_inventar(inventar)
print("Ai", aur, "aur.")

while True:
    print("\nArticole disponibile:")
    for obiect, pret in magazin.items():
        print(f"- {obiect}: {pret} aur")
    alegere = input("Ce vrei să cumperi? (scrie 'exit' pentru a ieși) ")

    if alegere == "exit":
        break
    elif alegere in magazin:
        if aur >= magazin[alegere]:
            aur -= magazin[alegere]
            if alegere in inventar:
                inventar[alegere] += 1
            else:
                inventar[alegere] = 1
            print(f"Ai cumpărat {alegere}!")
        else:
            print("Nu ai suficient aur!")
    else:
        print("Articol necunoscut.")

afiseaza_inventar(inventar)
print("Aur rămas:", aur)