import requests
from bs4 import BeautifulSoup
from time import sleep, time


top = []

usernames = ["AlexRoman777",  "AntonOttosson",  "JarlJakobsson", "mindriddler",  "PapaPeskwo",
             "SamanPetfat", "rlinddo22",  "raffiavakian",  "PavelKostyuk", "ossonack",
             "miralee94",  "MarioKhalaf", "Manibadani",  "maal2202",  "lundgren98",
             "JustOwl", "julianbe93",  "JonksPanda",  "IsacGrive",  "IsabelValijani",
             "gurraoberg",  "fridalundstroms",  "Fradop",  "delu2201",  "davidhasenson",
             "DanielBrunoMatzui",  "Corn1344",  "CharalamposMoutsios",  "Skygfisk",
             "Sundgren95",  "Telf92",  "Tolli-txt"]


def start():
    print("Welcome to the GitHub contribution counter!")
    print("This program will count the number of contributions for each user in the list.")
    print("Please wait a few seconds for the results to appear.")
    print("The results will be printed in the terminal and saved in a text file.")
    print("Please note that the program will take a few minutes to run.")

    for name in usernames:
        get_contributions(name)


def get_contributions(name):
    '''Get the number of contributions for a user'''
    page = requests.get(f'https://github.com/{name}')
    soup = BeautifulSoup(page.content, 'html.parser')
    page_body = str(soup.body)
    key = "h2 class=\"f4 text-normal mb-2\">"
    if key in page_body:
        number = (page_body[page_body.index(key) + 37:page_body.index(key) + 44])
        number = int(number.replace(" ", "").replace(",", ""))
        # Add a delay to avoid getting blocked by GitHub
        sleep(5)
        top.append({name: number})
        print(f"{name}: {number}")

    else:
        print("Not found")


def main():
    start()
    top.sort(key=lambda x: list(x.values())[0], reverse=True)
    with open("DevOps22/DevOps22.md", "w") as file:

        file.write("# DevOps 22 - GitHub contributions" + "\n\n")
        file.write("---" + "\n\n")

        file.write("| Place | User | Contributions |" + "\n")
        file.write("| --- | --- | :---: |" + "\n")
        for user in top:
            file.write("| " + str(top.index(user) + 1) + " | " + str(list(user.keys())[0]) + " | " + str(list(user.values())[0]) + " |" + "\n")

            # file.write("| " + str(list(user.keys())[0]) + " | " + str(list(user.values())[0]) + " |" + "\n")


if __name__ == "__main__":
    main()
