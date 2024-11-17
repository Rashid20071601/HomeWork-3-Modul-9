# Списки строк на английском и русском языках
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генератор, который вычисляет разницу в длине строк для тех, которые не совпадают по длине
first_result = (len(word_1) - len(word_2) for word_1, word_2 in zip(first, second) if len(word_1) != len(word_2))

# Генератор, который проверяет, что длина строки из first меньше или равна длине строки из second
second_result = (len(first[i]) <= len(second[i]) for i in range(min(len(first), len(second))))

# Выводим результаты генераторов в виде списков
print(list(first_result))
print(list(second_result))
