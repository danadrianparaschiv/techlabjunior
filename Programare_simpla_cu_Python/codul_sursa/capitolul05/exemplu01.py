import random

viata_jucator = 10
viata_monstru = random.randint(5, 12)

print("Un monstru a apărut cu", viata_monstru, "viață!")

while viata_monstru > 0 and viata_jucator > 0:
    atac = random.randint(1, 4)
    print("Ataci monstrul și îi scazi", atac, "viață.")
    viata_monstru -= atac

    if viata_monstru <= 0:
        print("Ai învins monstrul!")
        break

    # Monstrul atacă
    atac_monstru = random.randint(1, 3)
    print("Monstrul te lovește și pierzi", atac_monstru, "viață.")
    viata_jucator -= atac_monstru

if viata_jucator <= 0:
    print("Ai pierdut lupta!")
