from pprint import pprint

def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age,
                }

                cats_info.append(cat)

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []

    except (ValueError, OSError) as error:
        print(f"Помилка обробки файлу: {error}")
        return []

    return cats_info

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    pprint(cats_info, sort_dicts=False)