def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec, tuple):                    
        raise TypeError
    
    if len(rec) != 3:
        raise ValueError
    
    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):  
        raise TypeError
    
    if not isinstance(gpa, float):
        raise TypeError

    if not fio:                                            
        raise ValueError
    if not group:
        raise ValueError
    
    if not gpa:
        raise ValueError
    
    parts = fio.strip().split()                      
    if len(parts) < 2:
        raise ValueError
    surname = parts[0].title()                                     
    initials = "".join(p[0].upper() + '.' for p in parts[1:])       

    group = group.strip()

    gpa = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01")))
