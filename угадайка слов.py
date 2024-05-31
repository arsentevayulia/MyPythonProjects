from random import *

word_list = ['собака', 'кошка','ребенок','питон','муж','жена','импровизация','программирование','задротство','привет']

def get_word():
    word = choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
    print ("Давайте играть в угадайку слов!")
    word = get_word()
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print(display_hangman(tries))
    print (word_completion)

    while not guessed and tries > 0:
        print("Введите слово целиком или букву:")
        slovo = input().upper()
        if len(slovo)  == 1 and slovo.isalpha():
            if slovo in guessed_letters:
                print("Уже называли {}".format(slovo))
            elif slovo not in word:
                print ("Вы ошиблись, буквы {} нет в слове".format(slovo))
                tries -= 1
                guessed_letters.append(slovo)
            else:
                print("Буква {} есть в слове!".format(slovo))
                guessed_letters.append(slovo)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == slovo]
                for i in indices:
                    word_as_list[i] = slovo
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    print('Победа')
                    break
        elif len(slovo) == len(word) and slovo.isalpha():
            if slovo in guessed_words:
                print('Вы уже называли слово {}'.format(slovo))
            elif slovo != word:
                print('Слово {} не является верным.'.format(slovo))
                tries -= 1
                guessed_words.append(slovo)
            else:
                word_completion = word
                print('Победа')
                break
        else:
            print('Введите букву или слово.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было {}. Может быть в следующий раз!'.format(word))


ag = 'д'

while ag.lower() == 'д':
    word = get_word()
    play(word)
    ag = input('Играем еще раз? (д = да, н = нет):')

