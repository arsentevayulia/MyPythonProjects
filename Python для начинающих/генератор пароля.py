import random
from string import *
def generate_password (l_pass, chars):
    password = ''
    for i in range (l_pass):
        password += random.choice(chars)
    return password

d = '0123456789'
ll = 'abcdefghijklmnopqrstuvwxyz'
ul = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
p = '!#$%&*+-=?@^_'
s = ''
chars = 'il1Lo0O'
print("Укажите количество паролей для генерации")
q_pass = int(input())
print("Укажите длину 1 пароля")
l_pass = int(input())
print("Включаем ли цифры? д/н")
answer1 = input()
print("Включаем ли прописные буквы? д/н")
answer2 = input()
print("Включаем ли строчные буквы? д/н")
answer3 = input()
print("Включаем символы? д/н")
answer4 = input()
print("Исключаем неоднозначные символы? д/н")
answer5 = input()
if answer1 == 'д':
    chars = chars + d
if answer2 == 'д':
    chars = chars + ll
if answer3 == 'д':
    chars = chars + ul
if answer4 == 'д':
    chars = chars + p
for c in chars:
    chars.replace(c, '')    
for _ in range(q_pass):
    print(generate_password (l_pass, chars))

