import os
import sys
import json
import time

running = True

start_menu = [
    "1. Показать все задачи",
    "2. Отсортировать задачи",
    "3. Отфильтровать задачи",
    "0. Выйти"
]

all_tasks_menu = [
        "1. Вернуться назад",
        "0. Выйти"
]
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Файл tasks.json не найден.")
        return []

    except json.JSONDecodeError:
        print("Ошибка: файл tasks.json повреждён.")
        return []

def show_all_tasks():

    data = load_tasks()

    if not data:
        print("Список задач пуст.")
    else:
        for task in data:
            text = (
                f"{task['id']}. | "
                f"{task['title']} | "
                f"приоритет: {task['priority']} | "
                f"статус: {task['status']} | "
                f"создана: {task['created_at']} | "
            )

            if task.get("deadline"):
                text += f"(выполнить до: {task['deadline']})"

            print(text)
            print("-" * 80)

def choise_func(output_text : list) -> int:
    """
    output_text - выводимый список выбора
    возвращает выбранное пользователем значение от 0 до длины списка output_text-1
    """
    print(*output_text, sep="\n")
    print()

    while True:
        try:
            choise = int(input("Выберите задачу: "))

            if 0 <= choise <= len(output_text)-1:
                return choise

        except ValueError   :
            print(f"Еблан? выбери от 0 до {len(output_text)-1}")

    
def main():
    global running

    while running:
        os.system("cls")
        print("\n=== МЕНЕДЖЕР ЗАДАЧ ===")

        choise = choise_func(start_menu)

        if choise == 1:
            os.system("cls")
            
            print("\n=== ВСЕ ЗАДАЧИ ===")

            show_all_tasks()

            task_choice = choise_func(all_tasks_menu)

            if task_choice == 0:
                running = False

            if task_choice == 1:
                continue

            if task_choice == 2:
                print("\n=== ПОДРОБНЫЙ ПРОСМОТР ЗАДАЧИ ===")  # также 1.редактирование 2.завершение, 3.удаление
                print("В разработке")

            if task_choice == 3:
                print("\n=== ДОБАВЛЕНИЕ ЗАДАЧИ ===")
                print("В разработке")

            if task_choice == 4:
                print("\n=== ПОИСК ЗАДАЧ ===")
                print("В разработке")



        if choise == 2:
            os.system("cls")
            print("\n=== СОРТИРОВКА ЗАДАЧ ===")
            print("В разработке")
            input("\nНажмите Enter, чтобы вернуться в меню...")

        if choise == 3:
            os.system("cls")
            print("\n=== ФИЛЬТРАЦИЯ ЗАДАЧ ===")
            print("В разработке")
            input("\nНажмите Enter, чтобы вернуться в меню...")

        if choise == 0:
            running = False

if __name__ == "__main__":
    main()