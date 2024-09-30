import os
import re
import sys
import google.generativeai as geneai
from colorama import Fore, Style
from dotenv import load_dotenv

geneai.configure(api_key=os.environ["API_KEY"])

load_dotenv


def get_user_prompt(save=False):
    user_prompt = input("Enter prompt: ")
    if save:
        get_gemini_response(user_prompt, save=True)
    else:
        get_gemini_response(user_prompt)


def get_gemini_response(user_prompt, save=False):
    model = geneai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{user_prompt}")

    pieces_of_info = [response.text]

    display_ai_response(pieces_of_info, save)

    if save:
        while True:
            cont = input("Enter [S] to save or [C] to continue: ").upper()
            if cont not in {"S", "C"}:
                print(f"\n{Fore.RED}ERROR: Please enter [S] or [C]{Style.RESET_ALL}\n")
            else:
                break

        if cont == "S":
            save_to_file(pieces_of_info)
        else:
            print(f"\n{Fore.GREEN}CONTINUE{Style.RESET_ALL}\n")
            return
    else:
        while True:
            cont = input("Enter [C] to continue or [Q] to quit: ").upper()
            if cont not in {"C", "Q"}:
                print(f"\n{Fore.RED}ERROR: Please enter [C] or [Q]{Style.RESET_ALL}\n")
            else:
                break
        if cont == "C":
            print(f"\n{Fore.GREEN}CONTINUE{Style.RESET_ALL}\n")
            return
        else:
            sys.exit(f"\n{Fore.RED}PROGRAM TERMINATED{Style.RESET_ALL}\n")


def save_to_file(pieces_of_info):
    while True:
        file_name = input(
            "Enter file name to save: "
        ).strip()  # implement regex to check valid file name
        if not validate_file_name(file_name):
            print(
                f"\n{Fore.RED}ERROR: Please enter valid file name{Style.RESET_ALL}{Style.RESET_ALL}\n"
            )
        else:
            break

    folder_path = r"C:\Users\jachy\Documents\Coding\AI Notes"
    save_path = os.path.join(folder_path, f"{file_name}.txt")

    try:
        with open(save_path, "w") as file:
            for info in pieces_of_info:
                file.write(info)

        if os.path.exists(save_path):
            print(
                f"\n{Fore.GREEN}SUCCESS:{Style.RESET_ALL} Notes saved to {file_name}\n"
            )
        else:
            print(f"\n{Fore.RED}ERROR: File failed to save{Style.RESET_ALL}\n")

    except Exception as e:
        print(f"\n{Fore.RED}ERROR: Failed to save file:{Style.RESET_ALL} {e}\n")


def display_ai_response(response, save=False):
    if save:
        for line in response:
            print(f"\n{Fore.GREEN}{line}{Style.RESET_ALL}")
    else:
        for line in response:
            print(f"\n{Fore.YELLOW}{line}{Style.RESET_ALL}")


def validate_file_name(file_name):
    regex = r"^[a-zA-Z0-9_\-]+$"
    return re.match(regex, file_name)
