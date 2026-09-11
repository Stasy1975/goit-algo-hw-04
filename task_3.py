import sys
from pathlib import Path
from colorama import Fore, init


init(autoreset=True)


def display_directory(directory: Path, indent: str = "") -> None:
    for item in sorted(directory.iterdir()):
        if item.is_dir():
            print(Fore.BLUE + f"{indent}{item.name}/")
            display_directory(item, indent + "    ")
        else:
            print(Fore.GREEN + f"{indent}{item.name}")


def main() -> None:
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + f"Шлях не існує: {directory}")
        return

    if not directory.is_dir():
        print(Fore.RED + f"Це не директорія: {directory}")
        return

    print(Fore.BLUE + f"{directory.name}/")

    try:
        display_directory(directory)
    except PermissionError:
        print(Fore.RED + "Немає дозволу на перегляд цієї директорії.")
    except OSError as error:
        print(Fore.RED + f"Помилка читання директорії: {error}")


if __name__ == "__main__":
    main()