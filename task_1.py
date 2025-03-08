from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int: # передаємо рядок і повертаємо ціле число
    try:
        normalized_date = dtdt.strptime(date, "%Y-%m-%d") # перетворюємо у datetime в потрібному форматі
        today_date = dtdt.today() # знаходимо согодні
        days_difference = (today_date - normalized_date).days # знаходимо різницю і виводимо лише дні
        return days_difference # повертаємо результат
    except ValueError:
        return "Wrong date format. please use YYYY-mm-dd format" # ловимо помилку формату

print(get_days_from_today('2025-12-25')) # виводимо виклик фунції з датою у майбутньому для перевірки
print(get_days_from_today('2025.12.25')) # виводимо виклик фунції з невірним форматом дати для перевірки
