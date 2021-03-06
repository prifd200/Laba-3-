import re
import time
max_buffer_len = 100                                                                                                          # максимальный размер рабочего буфера
def laba2(text_name):
    try:
        with open(f"{text_name}.txt", "r", encoding="utf-8") as f:                                                                        # открываем файл
            lines, chars, words, sentences, puncts, digits, numbers = 1, 0, 0, 0, 0, 0, 0                                         # вводим переменные для подсчёта количество строк, количество символов, количество слов, количество предложений, количество знаков препинания, количество цифр, количество чисел
            buffer = f.read(max_buffer_len)                                                                                       # читаем первый блок
            if not buffer:                                                                                                        # если файл пустой
                print("Файл пустой.\nОтредактируйте файл или добавьте не пустой файл text.txt.\n")
            else:
                while buffer:
                    lines += len(re.findall(r'\n', buffer))                                                                       # подсчитывает переносы строк
                    chars += len(re.findall(r'.', buffer))                                                                        # подсчитывает количество символов
                    words += len(re.findall(r'\b[a-zA-Zа-яА-Я]+\b', buffer))                                                      # подсчитывает количество слов
                    sentences += len(re.findall(r'[.!?]+', buffer))                                                               # подсчитывает количество предложений
                    puncts += len(re.findall(r'[.!?:;",)\'(\-]', buffer))                                                         # подсчитывает количество знаков препинания
                    digits += len(re.findall(r'\d', buffer))                                                                      # подсчитывает количество цифр
                    numbers += len(re.findall(r'\d+[.,]?\d+\b', buffer))                                                                # подсчитывает количество чисел
                    buffer = f.read(max_buffer_len)                                                                               # читаем очередной блок
                print(f"В тексте:\n{lines} строк(и); {chars} символов; {words} слов; {sentences} предложений; {puncts} знаков препинания; {digits} цифр; {numbers} чисел")
    except FileNotFoundError:
        print("Файл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    #print("Время работы программы:  ", time.process_time(), "секунд")


tests = {"Тест 1": "\nФайл, текст длиной 1200 символов, содержащий 202 слов; 18 предложений; 81 знаков препинания; 0 цифр; 0 чисел, присутствует кириллица",
         "Тест 2": "\nФайл, текст длиной 1438 символов, содержащий 179 слов; 71 предложений; 179 знаков препинания; 46 цифр; 11 чисел, присутствует латиницу и цифры ",
         "Тест 3": "\nФайл, текст длиной 9991 символов, 1158 слов; 61 предложений; 185 знаков препинания; 0 цифр; 0 чисел, присутствует кирилица",
         "Тест 4": "\nФайл, текст длиной 2861 символов, содержащий 467 слов; 44 предложений; 198 знаков препинания; 6 цифр; 1 чисел, присутствует латиницу,кириллицу,цифры ",
         "Тест 5": "\nПустой файл",
         "Тест 6": "\nФайла нет в директории проекта",
         "Тест 7": "\nФайл, текст длиной 2861 символов, содержащий 800 слов; 78 предложений; 351 знаков препинания; 0 цифр; 0 чисел, присутствует кирилица и знаки",
         "Тест 8": "\nФайл, текст длиной 2861 символов, содержащий 697 слов; 99 предложений; 197 знаков препинания; 8 цифр; 2 чисел, присутствует",
         "Тест 9": "\nФайл, текст длиной 88 символов, содержащий 12 слов; 0 предложений; 0 знаков препинания; 9 цифр; 3 чисел, присутствует"}
for i in range(1, 10):
    start = time.time()
    print(f"\nТест {i}", tests[f"Тест {i}"], '\n')
    laba2(f"test{i}")
    print(time.time()-start)
