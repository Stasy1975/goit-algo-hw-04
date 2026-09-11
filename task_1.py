def total_salary(path: str) -> tuple[int, float]:
    total = 0
    developers_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                name, salary = line.strip().split(",")

                total += int(salary)
                developers_count += 1

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0.0

    except (ValueError, OSError) as error:
        print(f"Помилка обробки файлу: {error}")
        return 0, 0.0

    average = total / developers_count if developers_count else 0.0

    return total, average

if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")

    print(f"Загальна сума заробітної плати: {total:.2f} €")
    print(f"Середня заробітна плата: {average:.2f} €")