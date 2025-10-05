print("Te afli în sat. Poți merge la pădure sau la peșteră.")

loc = input("Unde vrei să mergi? (padure/pestera) ")

if loc == "padure":
    print("În pădure auzi păsările cântând și găsești un drum ascuns.")
elif loc == "pestera":
    print("Peștera e întunecoasă și rece. Simți un curent de aer misterios.")
else:
    print("Te întorci acasă și bei o cană de ceai.")
