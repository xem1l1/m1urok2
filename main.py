import random
import time
import string

simbol = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

print("ГЕНЕРАТОР ПАРОЛЕЙ")
print("здесь вы сможете сгенерировать пароль")
zapros = int(input("Введите длину пароля: "))

password = ""



for i in range(zapros):
    password += random.choice(string.printable)
    
time.sleep(2)
print("Сгенерированный пароль:", password)
