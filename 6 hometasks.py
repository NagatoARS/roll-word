#Задание 1. Пишем функцию roll_word(). Пользователь вводит какое-то слово, например питон.
#Т.е. надо напечатать каждую букву отдельно, причем в обратном порядке (скорее всего нам потребуется анализировать длину введенной строки и обращаться по индексу к элементу строки)

def roll_word():
    a=input("Введите слово:")
    b=list(a)
    b.reverse()
    len_b=len(b)
    i=0
    while i < len_b:
        print(b[i])
        i+=1
    return(b)
roll_word()
    

#Задание 2.Пишем функцию поиска find(). У функции будет 2 аргумента: слово (word) и символ (letter)
#Задача функции вернуть индекс символа в строке. Если символа в строке нет, должно вернуться -1.
def find():
    word=input("Введите слово:")
    letter=input("Индекс буквы:")
    if word.find(letter) == True:
        return (print(word.find(letter)))
    else:
        return(print('-1'))
find()

#Задание 3. Делаем функцию count_letter(word, letter)
#Задача функции определить сколько раз буква встречается в строке.
def count_letter():
    word=input("Введите слово:")
    word=word.lower()
    a=input("Введите букву(-ы):")
    a=a.lower()
    return(print(word.count(a)))
count_letter()
