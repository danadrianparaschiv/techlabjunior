import random

print("Bine ai venit la jocul BONUS: Spânzurătoarea!")
print("Ghicește cuvântul literă cu literă.")

# Lista de cuvinte
cuvinte = ["python", "aventura", "magie", "padure", "sabie"]

# Alegem un cuvânt aleator
cuvant_secret = random.choice(cuvinte)
ghicit = ["_"] * len(cuvant_secret)  # listă cu liniuțe pentru fiecare literă

incercari = 6  # numărul maxim de greșeli

while incercari > 0 and "_" in ghicit:
    print("\nCuvânt:", " ".join(ghicit))
    litera = input("Alege o literă: ").lower()

    if litera in cuvant_secret:
        print("Bravo! Litera este în cuvânt.")
        for i, l in enumerate(cuvant_secret):
            if l == litera:
                ghicit[i] = litera
    else:
        incercari -= 1
        print(f"Litera nu există. Mai ai {incercari} încercări.")

if "_" not in ghicit:
    print("\nFelicitări! Ai ghicit cuvântul:", cuvant_secret)
else:
    print("\nAi pierdut! Cuvântul era:", cuvant_secret)
