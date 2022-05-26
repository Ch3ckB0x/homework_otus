import json
from csv import reader


try:
    with open("users.json", "r") as f:
        users = json.loads(f.read())
        users_list = [{"name": i["name"], "gender": i["gender"], "address": i["address"], "age": i["age"], "books": []}
                      for i in users]

    with open("books.csv", newline='') as f:
        reader = reader(f)

        # Извлекаем заголовок
        header = next(reader)

        # Итерируемся по данным, делая из них словари
        books_info = [{"title": row[0], "author": row[1], "pages": row[3], "genre": row[2]} for row in reader]

except FileNotFoundError:
    print("Не найдены необходимые файлы")

else:
    # Распределяем книги по пользователям
    for user in users_list:
        if len(books_info) > 0:
            user['books'].append(books_info.pop())


        # Создаем файл
        with open('result.json', 'w') as r:
            result = json.dumps(users_list, indent=4)
            r.write(result)
