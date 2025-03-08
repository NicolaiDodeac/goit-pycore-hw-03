from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.06"},
    {"name": "Jane jkhith", "birthday": "1990.03.09"},
    {"name": "deab jhygth", "birthday": "1990.03.15"},
    {"name": "Jafgne jhth", "birthday": "1990.03.08"},
    {"name": "kjlne kjhith", "birthday": "1990.03.11"},
    {"name": "nvne kjhkth", "birthday": "1990.04.09"},
    {"name": "Jpoie kjhkth", "birthday": "1990.05.09"}
]


def get_upcoming_birthdays(users):
    today_date = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user_birthday.replace(year=today_date.year)
        
        if birthday_this_year < today_date:
             birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)

        elif 0 <= (birthday_this_year - today_date).days <= 7:
            if birthday_this_year.weekday() in [5,6]:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
            
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

