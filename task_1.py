from datetime import datetime


def get_days_from_today(date_str) -> int:
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        difference = current_date - input_date
        return difference.days
    except ValueError:
        return "Incorrect date format. Please use the format 'РРРР-ММ-ДД'."


print(get_days_from_today('2021-10-09'))
print(get_days_from_today('202110-09'))
