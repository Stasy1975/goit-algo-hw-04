def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()

    if not parts:
        return "", []

    command, *args = parts
    command = command.lower()

    return command, args


def add_contact(
    args: list[str],
    contacts: dict[str, str],
) -> str:
    if len(args) != 2:
        return "Please enter a name and phone number."

    name, phone = args
    name = name.capitalize()

    contacts[name] = phone

    return "Contact added."


def change_contact(
    args: list[str],
    contacts: dict[str, str],
) -> str:
    if len(args) != 2:
        return "Please enter a name and new phone number."

    name, phone = args
    name = name.capitalize()

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone

    return "Contact updated."


def show_phone(
    args: list[str],
    contacts: dict[str, str],
) -> str:
    if len(args) != 1:
        return "Please enter a contact name."

    name = args[0].capitalize()

    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."

    return "\n".join(
        f"{name}: {phone}"
        for name, phone in contacts.items()
    )


def main() -> None:
    contacts: dict[str, str] = {}

    print("Welcome to the assistant bot!")
    print("Доступні команди:")
    print("  hello - привітатися з ботом")
    print("  add [ім'я] [телефон] - додати контакт")
    print("  change [ім'я] [новий телефон] - змінити телефон")
    print("  phone [ім'я] - знайти телефон за ім'ям")
    print("  all - показати всі контакти")
    print("  close або exit - завершити роботу")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()