# Задние 1
numbers = []


def add_number():
    num = int(input("Введите число для добавления в список: "))
    if num in numbers:
        print("Это число уже существует в списке.")
    else:
        numbers.append(num)
        print(f"Число {num} добавлено в список.")


def remove_number():
    num = int(input("Введите число для удаления из списка: "))
    if num in numbers:
        numbers.remove(num)
        print(f"Все вхождения числа {num} были удалены из списка.")
    else:
        print(f"Числа {num} нет в списке.")


def show_list():
    choice = input("Введите 'начало' или 'конец' для отображения списка: ")
    if choice == "начало":
        print(numbers)
    elif choice == "конец":
        print(numbers[::-1])
    else:
        print("Некорректный ввод.")


def check_value():
    num = int(input("Введите число для проверки: "))
    if num in numbers:
        print(f"Число {num} есть в списке.")
    else:
        print(f"Числа {num} нет в списке.")


def replace_value():
    num = int(input("Введите число для замены: "))
    if num in numbers:
        replace_all = input("Заменить все вхождения? (да/нет): ")
        if replace_all == "да":
            new_num = int(input("Введите новое число: "))
            numbers = [new_num if x == num else x for x in numbers]
            print(f"Все вхождения числа {num} были заменены на {new_num}.")
        else:
            index = numbers.index(num)
            new_num = int(input("Введите новое число: "))
            numbers[index] = new_num
            print(f"Первое вхождение числа {num} было заменено на {new_num}.")
    else:
        print(f"Числа {num} нет в списке.")


while True:
    print("Меню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")

    choice = input("Выберите пункт меню (1-5) или введите 'выход' для завершения: ")

    if choice == "1":
        add_number()
    elif choice == "2":
        remove_number()
    elif choice == "3":
        show_list()
    elif choice == "4":
        check_value()
    elif choice == "5":
        replace_value()
    elif choice == "выход":
        break
    else:
        print("Некорректный выбор.")


# Задание 2
class FixedSizeStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
            print(f"Строка '{item}' добавлена в стек.")
        else:
            print("Стек полон, невозможно добавить новую строку.")

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            print(f"Строка '{item}' удалена из стека.")
        else:
            print("Стек пуст, невозможно удалить строку.")

    def count(self):
        print(f"В стеке {len(self.stack)} строк.")

    def is_empty(self):
        if not self.stack:
            print("Стек пуст.")
        else:
            print("Стек не пуст.")

    def is_full(self):
        if len(self.stack) == self.size:
            print("Стек полон.")
        else:
            print("Стек не полон.")

    def clear(self):
        self.stack.clear()
        print("Стек очищен.")

    def peek(self):
        if self.stack:
            print(f"Верхняя строка в стеке: {self.stack[-1]}")
        else:
            print("Стек пуст.")

stack_size = 5
stack = FixedSizeStack(stack_size)

while True:
    print("Меню:")
    print("1. Добавить строку в стек")
    print("2. Удалить строку из стека")
    print("3. Подсчитать количество строк в стеке")
    print("4. Проверить, пуст ли стек")
    print("5. Проверить, полон ли стек")
    print("6. Очистить стек")
    print("7. Получить верхнюю строку без удаления")
    print("8. Выйти")

    choice = input("Выберите пункт меню (1-8): ")

    if choice == "1":
        item = input("Введите строку для добавления в стек: ")
        stack.push(item)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        stack.count()
    elif choice == "4":
        stack.is_empty()
    elif choice == "5":
        stack.is_full()
    elif choice == "6":
        stack.clear()
    elif choice == "7":
        stack.peek()
    elif choice == "8":
        break
    else:
        print("Некорректный выбор.")

# Задание 3
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Строка '{item}' добавлена в стек.")

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            print(f"Строка '{item}' удалена из стека.")
        else:
            print("Стек пуст, невозможно удалить строку.")

    def count(self):
        print(f"В стеке {len(self.stack)} строк.")

    def is_empty(self):
        if not self.stack:
            print("Стек пуст.")
        else:
            print("Стек не пуст.")

    def clear(self):
        self.stack.clear()
        print("Стек очищен.")

    def peek(self):
        if self.stack:
            print(f"Верхняя строка в стеке: {self.stack[-1]}")
        else:
            print("Стек пуст.")

stack = Stack()

while True:
    print("Меню:")
    print("1. Добавить строку в стек")
    print("2. Удалить строку из стека")
    print("3. Подсчитать количество строк в стеке")
    print("4. Проверить, пуст ли стек")
    print("5. Очистить стек")
    print("6. Получить верхнюю строку без удаления")
    print("7. Выйти")

    choice = input("Выберите пункт меню (1-7): ")

    if choice == "1":
        item = input("Введите строку для добавления в стек: ")
        stack.push(item)
    elif choice == "2":
        stack.pop()
    elif choice == "3":
        stack.count()
    elif choice == "4":
        stack.is_empty()
    elif choice == "5":
        stack.clear()
    elif choice == "6":
        stack.peek()
    elif choice == "7":
        break
    else:
        print("Некорректный выбор.")
