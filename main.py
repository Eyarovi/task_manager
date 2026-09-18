import os
import sys
import json
import time

running = True


start_menu = [
    "1. Показать все задачи",\
    "0. Выйти"
]

all_tasks_menu = [
    "1. Вернуться назад",
    "2. Выбрать задачу",
    "3. Добавить задачу",
    "4. Найти задачу",
    "5. Отсортировать задачи",
    "6. Отфильровать по параметру задачи",
    "0. Выйти"
]

task_menu = [
    "1. Редактирование",
    "2. Завершение", 
    "3. Удаление",
    "0. Выйти"
]

def show_start_menu():
    os.system("cls")

    print("\n=== МЕНЕДЖЕР ЗАДАЧ ===")
    print(*start_menu, sep="\n")


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
    os.system("cls")

    print("\n=== ВСЕ ЗАДАЧИ ===")

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

    print()
    print(*all_tasks_menu, sep="\n")


def choise_func(output_text : list):
    while True:
        try:
            print()
            choise = int(input("Выберите номер команды: "))

            if 0 <= choise <= len(output_text)-1:
                return choise
            else:
                print(
                    f"Ошибка: выберите число от 0 "
                    f"до {len(output_text) - 1}."
                )

        except:
            print("Ошибка: введите целое число.")


def choise_task_func(data_tasks):
    while True:
        try:
            print()
            choise = int(input("Выберите номер задачи: "))

            if 0 <= choise <= len(data_tasks)-1:
                return choise
            else:
                print(f"Ошибка: выберите номер задачи от 0 до {len(data_tasks)-1}.")

        except:
            print("Ошибка: введите целое число.")


def get_task(tasks, search_value):
    for task in tasks:
        if task["id"] == search_value:
            return task

    return print("Такая задача не существует")


def show_task():
    task_text = f"""
Название: {task["title"]}
Описание: {task["deacription"]}
Статус: {task["status"]}
Приоритет: {task["priority"]}
Создана: {task["created_at"]}
Дедлайн: {task["deadline"]}
    """

    print(task_text)


def show_task_menu():
    os.system("cls")

    print("\n===ПОДРОБНОЕ ОПИСАНИЕ ЗАДАЧИ===")

    show_task()

    print(*task_menu, sep="\n")


data = load_tasks()

def main():
    global running, data, task

    while running:
        show_start_menu()

        choise = choise_func(start_menu)

        if choise == 1:
            show_all_tasks()

            task_choice =  choise_func(all_tasks_menu)

            if task_choice == 1:
                continue

            if task_choice == 2:
                print()

                task_number = choise_task_func(data)
                task = get_task(data, task_number) 

                show_task_menu()

                input()

            if task_choice == 3:
                print("\n=== ДОБАВЛЕНИЕ ЗАДАЧИ ===")
                print("В разработке")

            if task_choice == 4:
                print("\n=== ПОИСК ЗАДАЧ ===")
                print("В разработке")

            if choise == 5:
                print("\n=== СОРТИРОВКА ЗАДАЧ ===")
                print("В разработке")

            if choise == 6:
                print("\n=== ФИЛЬТРАЦИЯ ЗАДАЧ ===")
                print("В разработке")

            if task_choice == 0:
                running = False



        if choise == 0:
            running = False

if __name__ == "__main__":
    main()