def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec

    parts = [part for part in fio.strip().split() if part]

    formatted_parts = []
    for part in parts:
        formatted_parts.append(part[0].upper() + part[1:].lower())

    initials = []
    for part in formatted_parts[1:]:
        if part:
            initials.append(part[0].upper() + ".")
    formatted_fio = formatted_parts[0] + " " + "".join(initials)
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
