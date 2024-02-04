def total_salary(path):
   
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('Файл не знайдено!')
        return 0, 0

    total_salary = 0
    average_salary = 0

    for line in lines:
        try:
            developer, salary = line.split(',')
            salary = int(salary)
            total_salary += salary
        except ValueError:
            print('Неправильний формат даних у рядку:', line)
            continue

    average_salary = total_salary / len(lines)

    return total_salary, average_salary


# Приклад використання функції
path = 'salaries.txt'
total_salary, average_salary = total_salary(path)

print('Загальна сума зарплат:', total_salary)
print('Середня заробітна плата:', average_salary)