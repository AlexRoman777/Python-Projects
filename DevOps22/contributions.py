import requests
from bs4 import BeautifulSoup
from time import sleep, time
import csv
import os


top = []

usernames = [
    {"Alex Roman": "AlexRoman777"},
    {"Anton Ottonson": "AntonOttosson"},
    {"Jarl Jakobsson": "JarlJakobsson"},
    {"Fredrik Magnusson": "mindriddler"},
    {"Tomislav Orlovac": "PapaPeskwo"},
    {"Saman Petfat": "SamanPetfat"},
    {"Rickard Lindqvist": "rlinddo22"},
    {"Raffi Avakian": "raffiavakian"},
    {"Pavel Kostyuk": "PavelKostyuk"},
    {"Mira Lee": "miralee94"},
    {"Mario Khalaf": "MarioKhalaf"},
    {"Mandana Jahangosha": "Manibadani"},
    {"Martin Alfredson": "maal2202"},
    {"Alexander Lundgren": "lundgren98"},
    {"Karl Björklund ": "JustOwl"},
    {"Julian Bellotto": "julianbe93"},
    {"Jonathan Friberg": "JonksPanda"},
    {"Isac Grive": "IsacGrive"},
    {"Isabel Valijani": "IsabelValijani"},
    {"Gustav Öberg": "gurraoberg"},
    {"Frida Lundström": "fridalundstroms"},
    {"Hugo Göransson": "Fradop"},
    {"Dennis Lunnelid": "delu2201"},
    {"David Hasenson": "davidhasenson"},
    {"Fabian Lörstad": "Corn1344"},
    {"Charalampos Moutsios": "CharalamposMoutsios"},
    {"Odd Jensen": "Skygfisk"},
    {"David Sundgren": "Sundgren95"},
    {"Timmy Elf": "Telf92"},
    {"Oskar Tölli": "Tolli-txt"},
    {"Daniel Bruno Matzui": "DanielBrunoMatzui"}
]

message = '''   
Welcome to the GitHub contribution counter!
This program will count the number of contributions for each people in the Nackademin DevOps 22.
Please note that the program will take up to 2 minutes to run.
'''
# Clear the scrren for both Windows and Linux/macOS


def clear_terminal():
    '''Clears the terminal for a cleaner look :) '''
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    print(message)
    for user in usernames:
        for name, username in user.items():
            get_contributions(name, username)


def get_contributions(name, username):
    '''Get the number of contributions for a user'''
    page = requests.get(f'https://github.com/{username}')
    soup = BeautifulSoup(page.content, 'html.parser')
    page_body = str(soup.body)
    key = "h2 class=\"f4 text-normal mb-2\">"
    if key in page_body:
        number = (page_body[page_body.index(key) + 37:page_body.index(key) + 44])
        number = int(number.replace(" ", "").replace(",", ""))
        # Add a delay to avoid getting blocked by GitHub again ;)
        sleep(3)
        top.append({name: number})
        print(f"Processed {len(top)} out of {len(usernames)}")

    else:
        print("Not found")


def history(user, contributions):
    with open("DevOps22/data/history.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user:
                if row[1] == str(contributions):
                    return 0
                else:
                    return int(contributions) - int(row[1])


def main():
    start_time = time()
    clear_terminal()
    start()
    top.sort(key=lambda x: list(x.values())[0], reverse=True)
    with open("DevOps22/DevOps22.md", "w") as file:

        file.write("# DevOps 22 - GitHub contributions" + "\n\n")
        file.write("---" + "\n\n")

        file.write("| Place | User | Contributions | ^ |" + "\n")
        file.write("| --- | --- | :---: | :---: |" + "\n")
        for user in top:
            change = history(list(user.keys())[0], list(user.values())[0])
            file.write("| " + str(top.index(user) + 1) + " | " + str(list(user.keys())
                       [0]) + " | " + str(list(user.values())[0]) + " | " + str(change) + " |" + "\n")

        file.write("\n")
        file.write("---" + "\n\n")

        file.write("# Top 5 - Pie chart" + "\n\n")
        file.write("```mermaid" + "\n")
        file.write("pie title Top 5" + "\n")
        file.write('"' + str(list(top[0].keys())[0]) + '"' + ' : ' + str(list(top[0].values())[0]) + '\n')
        file.write('"' + str(list(top[1].keys())[0]) + '"' + ' : ' + str(list(top[1].values())[0]) + '\n')
        file.write('"' + str(list(top[2].keys())[0]) + '"' + ' : ' + str(list(top[2].values())[0]) + '\n')
        file.write('"' + str(list(top[3].keys())[0]) + '"' + ' : ' + str(list(top[3].values())[0]) + '\n')
        file.write('"' + str(list(top[4].keys())[0]) + '"' + ' : ' + str(list(top[4].values())[0]) + '\n')
        file.write("```" + "\n\n")

        file.write("---" + "\n\n")

    end_time = time()
    print(f"Time elapsed: {end_time - start_time} seconds")

    # Save to a history file
    with open("DevOps22/data/history.csv", "w") as file:
        writer = csv.writer(file)
        for user in top:
            writer.writerow([list(user.keys())[0], list(user.values())[0]])


if __name__ == "__main__":
    main()
