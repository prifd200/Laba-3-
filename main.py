import re
import time
max_buffer_len = 100                                                                                                          # максимальный размер рабочего буфера
try:
    with open("text.txt", "r", encoding="utf-8") as f:                                                                        # открываем файл
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
                numbers += len(re.findall(r'\b\d+[.,]?\d+\b', buffer))                                                                # подсчитывает количество чисел
                buffer = f.read(max_buffer_len)                                                                               # читаем очередной блок
            print(f"В тексте:\n{lines} строк(и); {chars} символов; {words} слов; {sentences} предложений; {puncts} знаков препинания; {digits} цифр; {numbers} чисел")
except FileNotFoundError:
    print("Файл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
print("Время работы программы:  ", time.process_time(), "секунд")