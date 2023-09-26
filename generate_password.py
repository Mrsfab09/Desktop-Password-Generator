import random
import string


def password_generating(
    password_length, lowercase_letters, uppercase_letters, special_characters, digits
):
    characters = []

    # Dodaj małe litery
    characters.extend(random.choices(string.ascii_lowercase, k=lowercase_letters))

    # Dodaj duże litery
    characters.extend(random.choices(string.ascii_uppercase, k=uppercase_letters))

    # Dodaj znaki specjalne
    characters.extend(random.choices(string.punctuation, k=special_characters))

    # Dodaj cyfry
    characters.extend(random.choices(string.digits, k=digits))

    # Wymieszaj znaki
    random.shuffle(characters)

    # Jeśli potrzebujesz więcej znaków, dodaj małe litery, aby uzupełnić
    characters.extend(
        random.choices(string.ascii_lowercase, k=password_length - len(characters))
    )

    # Wymieszaj ponownie
    random.shuffle(characters)

    return "".join(characters)
