from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    birthdays_to_congratulate = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            if birthday_this_year.weekday() == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            birthdays_to_congratulate.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
            })

    return birthdays_to_congratulate


users = [
    {"name": "John Doe", "birthday": "1985.07.10"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
