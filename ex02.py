def get_cats_info(path):
   
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('Файл не знайдено!')
        return []

    cats_info = []

    for line in lines:
        try:
            cat_id, name, age = line.split(',')
            cat_info = {
                'id': cat_id,
                'name': name,
                'age': int(age)
            }
            cats_info.append(cat_info)
        except ValueError:
            print('Неправильний формат даних у рядку:', line)
            continue

    return cats_info


# Приклад використання функції
path = 'cats.txt'
cats_info = get_cats_info(path)

for cat in cats_info:
    print(cat)