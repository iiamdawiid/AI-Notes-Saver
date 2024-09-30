from colorama import Fore, Style
from funcs import get_user_prompt


def start_menu():
    while True:
        print(" AI Notes ".center(30, "="))
        print(
            f"{Fore.RED}[0] Quit{Style.RESET_ALL}\n{Fore.GREEN}[1] Save Notes{Style.RESET_ALL}\n{Fore.YELLOW}[2] Free-roam{Style.RESET_ALL}"
        )
        while True:
            try:
                menu_choice = int(input("Enter choice: "))
                if menu_choice not in {0, 1, 2}:
                    print(
                        f"\n{Fore.RED}ERROR: Please enter number 1-3{Style.RESET_ALL}\n"
                    )
                else:
                    break
            except ValueError:
                print(f"\n{Fore.RED}ERROR: Please enter a number{Style.RESET_ALL}\n")

        match menu_choice:
            case 0:
                print(f"\n{Fore.RED}PROGRAM QUIT{Style.RESET_ALL}\n")
                break
            case 1:
                save_notes_menu()
            case 2:
                free_roam_menu()


def save_notes_menu():
    print("\n" + " Save Notes ".center(30, "="))
    get_user_prompt(save=True)


def free_roam_menu():
    print("\n" + " Free-Roam ".center(30, "="))
    get_user_prompt()  # TODO: Finish free_roam print function
