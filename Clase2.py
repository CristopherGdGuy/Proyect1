import random as r
longitud = int(input("¿Cuantos de longitud de contraseña quieres:"))
carac = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
for i in range(longitud):
    choise = r.randint(0,52)
    caracter = carac[choise]
    password += caracter
print(password)
