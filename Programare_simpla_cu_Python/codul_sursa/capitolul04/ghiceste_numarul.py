import random

print("Bine ai venit la jocul BONUS: Ghicește numărul!")
print("Am ales un număr între 1 și 20. Ai 5 încercări să-l ghicești.")

# Alegem un număr aleator
numar_secret = random.randint(1, 20)

# Jucătorul are 5 încercări
incercari = 5

while incercari > 0:
    ghicire = int(input("Introdu numărul tău: "))

    if ghicire == numar_secret:
        print("Felicitări! Ai ghicit numărul!")
        break
    elif ghicire < numar_secret:
        print("Numărul este MAI MARE decât atât.")
    else:
        print("Numărul este MAI MIC decât atât.")

    incercari -= 1
    print("Îți mai rămân", incercari, "încercări.")

if incercari == 0:
    print("Ai pierdut! Numărul era", numar_secret)
