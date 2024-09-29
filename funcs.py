import os
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

    for info in pieces_of_info:
        print(info)

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
        print("No save")


def save_to_file(pieces_of_info):
    file_name = input(
        "Enter file name to save: "
    ).strip()  # implement regex to check valid file name
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
