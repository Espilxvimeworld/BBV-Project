from colorama import init, Fore, Style

init(autoreset=True)

def shift_char(c, shift):
    # Русский алфавит
    rus_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    rus_lower = rus_upper.lower()

    # Английский алфавит
    eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_lower = eng_upper.lower()

    if c in rus_upper:
        idx = rus_upper.index(c)
        return rus_upper[(idx + shift) % len(rus_upper)]
    elif c in rus_lower:
        idx = rus_lower.index(c)
        return rus_lower[(idx + shift) % len(rus_lower)]
    elif c in eng_upper:
        idx = eng_upper.index(c)
        return eng_upper[(idx + shift) % len(eng_upper)]
    elif c in eng_lower:
        idx = eng_lower.index(c)
        return eng_lower[(idx + shift) % len(eng_lower)]
    else:
        return c  # не буквы не меняем

def encrypt(text):
    return ''.join(shift_char(c, 5) for c in text)

def decrypt(text):
    return ''.join(shift_char(c, -5) for c in text)

def main():
    print(Fore.CYAN + Style.BRIGHT + r"""
 ____  ______      __  _____  _____   ____       _ ______ _____ _______ 
 |  _ \|  _ \ \    / / |  __ \|  __ \ / __ \     | |  ____/ ____|__   __|
 | |_) | |_) \ \  / /  | |__) | |__) | |  | |    | | |__ | |       | |   
 |  _ <|  _ < \ \/ /   |  ___/|  _  /| |  | |_   | |  __|| |       | |   
 | |_) | |_) | \  /    | |    | | \ \| |__| | |__| | |___| |____   | |   
 |____/|____/   \/     |_|    |_|  \_\\____/ \____/|______\_____|  |_|   
                                                                        
    """)

    while True:
        print(Fore.YELLOW + "Добро пожаловать в " + Fore.MAGENTA + Style.BRIGHT + "BBVCode" + Fore.YELLOW + " шифратор!")
        print(Fore.GREEN + "Выберите нужную функцию:")
        print(Fore.GREEN + "1 - Зашифровать текст.")
        print(Fore.GREEN + "2 - Расшифровать текст.")
        print(Fore.RED + "exit - Выйти из программы.")
        choice = input(Fore.CYAN + "Введите 1, 2 или exit: ").strip().lower()

        if choice == "1":
            text = input(Fore.CYAN + "Введите текст для шифровки: ")
            encrypted = encrypt(text)
            print(Fore.MAGENTA + Style.BRIGHT + "Зашифрованный текст:")
            print(Fore.WHITE + encrypted + "\n")
        elif choice == "2":
            text = input(Fore.CYAN + "Введите текст для расшифровки: ")
            decrypted = decrypt(text)
            print(Fore.MAGENTA + Style.BRIGHT + "Расшифрованный текст:")
            print(Fore.WHITE + decrypted + "\n")
        elif choice == "exit":
            print(Fore.RED + "Выход из программы. До скорого!")
            break
        else:
            print(Fore.RED + "Некорректный ввод, попробуйте ещё раз.\n")

if __name__ == "__main__":
    main()
    input(Fore.YELLOW + "Нажмите Enter, чтобы выйти...")
