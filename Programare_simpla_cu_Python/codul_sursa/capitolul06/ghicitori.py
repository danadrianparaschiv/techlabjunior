# Funcția care pune o ghicitoare și verifică răspunsul
def pune_ghicitoare(intrebare, raspuns_corect):
    raspuns = input(intrebare + "\nRăspunsul tău: ").lower()
    if raspuns == raspuns_corect:
        print("Corect! Ai câștigat 1 punct.")
        return 1  # punct câștigat
    else:
        print("Greșit! Răspunsul corect era:", raspuns_corect)
        return 0  # fără puncte

# Jocul principal
def joc_ghicitori():
    print("Bine ai venit la jocul BONUS: Ghicitori magice!")
    scor = 0

    # Lista de ghicitori (intrebare, raspuns_corect)
    ghicitori = [
        ("Ce are chei dar nu poate deschide uși?", "pian"),
        ("Ce are gât dar nu are cap?", "sticla"),
        ("Ce urcă dar nu coboară niciodată?", "varsta"),
    ]

    for intrebare, raspuns_corect in ghicitori:
        scor += pune_ghicitoare(intrebare, raspuns_corect)

    print("\nAi terminat jocul! Scorul tău este:", scor, "din", len(ghicitori))

# Pornim jocul
joc_ghicitori()