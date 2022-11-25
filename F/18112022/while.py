
import random

# sekunde = 10

# while sekunde >0:
#     print(sekunde)
#     sekunde -= 1



# baterija = 100

while baterija > 0:
    print("Mozes koristi telefon", baterija, "%")
    baterija -= random.randint(5, 20)
    if baterija <15:
        print("Ukljuci punjac")


print("Prazna baterija")

for broj in range(11):
    if broj == 2:
        continue
    print(broj)
