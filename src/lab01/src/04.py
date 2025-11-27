total_minutes = int(input())
if total_minutes < 0:
    print("Ошибка: Количество минут не может быть отрицательным.")
    exit()
minutes_in_day = 24 * 60
days = total_minutes // minutes_in_day
remaining_minutes_after_days = total_minutes % minutes_in_day
hours = remaining_minutes_after_days // 60
minutes = remaining_minutes_after_days % 60
if days > 0:
    print(f"{days} дней, {hours:02d}:{minutes:02d}")
else:
    print(f"{hours:02d}:{minutes:02d}")
