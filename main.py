result = []

def divider(a, b):
    if a < b:
        raise ValueError("a уступает b.")
    if b > 100:
        raise IndexError("b зашкаливает.")
    return a / b

data = {10: 2, 2: 5, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except ValueError as ve:
        print(f"Неожиданность: {ve}")
        result.append(None)
    except IndexError as ie:
        print(f"Перебор: {ie}")
        result.append(None)
    except ZeroDivisionError:
        print("Деление на ноль, серьёзно?")
        result.append(None)
    except TypeError as te:
        print(f"Не то: {te}")
        result.append(None)

print(result)
