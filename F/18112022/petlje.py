# pozicija_automobila = 0
# pozicija_cilja = 10

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# for ime in ["marija", "sofija", "milena", "andjela", "aleksandra"]:
#     print("Cao", ime)

# print("Prva sledeca linija....")


# for broj in [1,2,3,4,5]:
#     print("Ovo je broj: ", broj)


# for broj in range(1, 21, 5):
#     print("Ovo je broj: ", broj)

# for broj in range(100, 0, -5):
#     print("Odbrojavanje: ", broj)


# pozicija_automobila = 0
# pozicija_cilja = 10


# for kretanje in range(pozicija_cilja +1):
#     pozicija_automobila = kretanje
#     print(pozicija_automobila == pozicija_cilja)


# startDate = 2010
# endDate = 2015

# for godine in range(endDate, startDate):
#     print(godine)


# for zvezda in range(100):
#     print("*", end="")

#t je tab
#n je novi red


# print()

# zeljeni_broj = int(input("Unesite broj: "))

# print("1\t2\t3\t")
# print("********************")

# for brojac in range(1, zeljeni_broj + 1):
#     print(brojac * 1, end="\t")
#     print(brojac * 2, end="\t")
#     print(brojac * 3)


for x in range(6):
        for y in range(6):
            if x == 0 or x == 5:
                print("#", end=" ")
            elif y == 0 or y == 5:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print() 

