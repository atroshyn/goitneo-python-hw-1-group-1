from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Крок 1: Підготовка даних
    birthday_dict = defaultdict(list)

    # Крок 2: Отримання поточної дати
    today = datetime.today().date()

    # Крок 3: Перебір користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Крок 4: Конвертація дати
        birthday_this_year = birthday.replace(year=today.year)

        # Крок 5: Оцінка дати на цей рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Крок 6: Порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # Крок 7: Визначення дня тижня
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
        else:
            continue  # День народження не в наступному тижні

        # Крок 8: Зберігання результату
        birthday_dict[day_of_week].append(name)

    # Виведення результату
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 12, 17)}, # іменинник
    # Додайте інших користувачів за потреби
]

get_birthdays_per_week(users)