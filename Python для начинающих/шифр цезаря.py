def shifr (lang, text, k):
    if lang == 'ru':
        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
        alphabet += alphabet.upper()
        mod = 32
    elif lang == 'en':
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        alphabet += alphabet.upper()
        mod = 26
    else:
        print ("Ошибка, введите правильный язык")
    for c in text:
        if not c.isalpha():
            print(c,end='') 
        elif c.isupper():
           print (alphabet[(alphabet.find(c)-k) % mod], end = '')
        else:
            print (alphabet[(alphabet.find(c)-k) % mod+mod], end = '')
print("Укажите язык шифрования")
lang = input()
print ("Введите текст для шифра")
text = input()
print ("Введие шаг сдвига")
k = int(input())

shifr (lang, text, k)


