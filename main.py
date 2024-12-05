# module_1_6.py

# Работа со словарями
my_dict = {
    "Антон": 1990,
    "Борис": 1985,
    "Иван": 1992
}

# 1. Выводим на экран словарь my_dict
print("Словарь my_dict:", my_dict)

# 2. Выводим одно значение по существующему ключу
print("Год рождения Иван:", my_dict.get("Иван"))

# 3. Выводим значение по отсутствующему ключу без ошибки
print("Год рождения по отсутствующему ключу (Данил):", my_dict.get("Данил", "Такого ключа нет"))

# 4. Добавляем ещё две пары
my_dict["Данил"] = 1988
my_dict["Ева"] = 1995

# 5. Удаляем одну из пар и выводим её значение
removed_value = my_dict.pop("Борис", "Такого ключа нет")
print("Удалено значение для Борис:", removed_value)

# 6. Выводим на экран обновленный словарь
print("Обновленный словарь my_dict:", my_dict)

# Работа с множествами
my_set = {1, 2, 333, "яблоко", "банан", 10, 2.5, "груша", 'ананас'}  # Включаем повторы, но в множестве они отобразятся уникально

# 1. Выводим на экран множество my_set
print("Множество my_set:", my_set)

# 2. Добавляем 2 новых элемента
my_set.add(4)
my_set.add("orange")

# 3. Удаляем один элемент
my_set.discard(2)  # Используем discard, чтобы избежать ошибки, если элемент не найден

# 4. Выводим на экран измененное множество
print("Измененное множество my_set:", my_set)
