import sqlite3

conn = sqlite3.connect("task_manager.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT NOT NULL,
status TEXT NOT NULL,
priority TEXT NOT NULL,
created_at TEXT NOT NULL,
deadline TEXT NOT NULL
)
""")

conn.commit()

# conn.executemany("""
# INSERT INTO tasks (title, description, status, priority, created_at, deadline)
# VALUES (?, ?, ?, ?, ?, ?)
# """, [
#     ("Пример имени", "АХУЕТЬ КАКОЕ БОЛЬШОЕ ОПИСАНИЕ ДЛЯ ПРОВЕРКИ ЭТОГО ЕБУЧЕГО ГОВНА, А ТО ВДРУГ ОНО НЕ РАБОТЕТ, БУДЕТ ЕВРЕЙ ПЛАКАТЬ ЕСЛИ ОНО НЕ РАБОТАЕТ, ИБО ЭТО ПИЗДЕЦ ОБИДНО", "активна", "высокая", "2026-09-14", "2026-09-18"),
#     ("Написать CLI менеджер", "Реализовать функции очистки, вывода и сохранения", "активная", "высокая", "2026-09-14", "2026-09-18"),
#     ("Повторить работу с JSON", "Закрепить load/dump", "выполнена", "средняя", "2026-09-13", "2026-09-14")
# ]
# )

# conn.commit()