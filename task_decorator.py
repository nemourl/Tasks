staff = {
    "Петров": "биолог",
    "Сидорова": "физик",
    "Козлов": "уборщик"
}

def require_role(needed_role):
    def decorator(func):
        def wrapper(surname):
            role = staff.get(surname)
            if role is None:
                print(f"'{surname}' не работает в лаборатории.")
                return
            if role != needed_role:
                print(f"'{surname}' ({role}) не имеет доступа. Требуется: {needed_role}.")
                return
            return func(surname)
        return wrapper
    return decorator

@require_role("биолог")
def enter_bio_lab(surname):
    print(f"{surname} вошёл в биологическую лабораторию.")

@require_role("физик")
def enter_phys_lab(surname):
    print(f"{surname} вошёл в физическую лабораторию.")

enter_bio_lab("Петров")
enter_bio_lab("Сидорова")
enter_bio_lab("Иванов")