import random

Caracters= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

Long = int(input("Indique la longitud de su contraseña"))

Contra= ""
for i in range(Long):
    Contra += random.choice(Caracters)
print("SU CONTRASEÑA ES:", Contra)


