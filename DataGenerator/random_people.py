import datetime
import random
import string
import json

# A list of first names
firstnames = [
    "Elias",
    "William",
    "Lucas",
    "Oliver",
    "Noah",
    "Oscar",
    "Ella",
    "Alice",
    "Alicia",
    "Astrid",
    "Emilia",
    "Filippa",
    "Freja",
    "Hanna",
    "Ida",
    "Isabella",
    "Jasmine",
    "Lilly",
    "Linnéa",
    "Linn",
    "Lovisa",
    "Maja",
    "Molly",
    "Nellie",
    "Saga",
    "Sofia",
    "Tilda",
    "Vera",
    "Wilma",
    "Albin",
    "Alfred",
    "Alvin",
    "Anton",
    "Axel",
    "Benjamin",
    "Björn",
    "Charlie",
    "David",
    "Erik",
    "Filip",
    "Gustav",
    "Hugo",
    "Isak",
    "Jacob",
    "Jesper",
    "Joel",
    "Jonathan",
    "Josef",
    "Leo",
    "Levi",
    "Liam",
    "Linus",
    "Lucian",
    "Ludvig",
    "Milo",
    "Nils",
    "Olle",
    "Otto",
    "Ove",
    "Pontus",
    "Samuel",
    "Sebastian",
    "Sigge",
    "Simon",
    "Sixten",
    "Theo",
    "Viktor",
    "Ville",
    "Vilmer",
    "William",
    "Wilmer",
    "Adam",
    "Alexander",
]

# A list of last names
lastnames = [
    "Andersson",
    "Johansson",
    "Karlsson",
    "Nilsson",
    "Eriksson",
    "Larsson",
    "Olsson",
    "Persson",
    "Svensson",
    "Gustafsson",
    "Pettersson",
    "Jonsson",
    "Jansson",
    "Hansson",
    "Jönsson",
    "Danielsson",
    "Bengtsson",
    "Ternström",
    "Lindgren",
    "Lindqvist",
    "Lindholm",
    "Lindskog",
    "Lindström",
    "Lindén",
    "Lindberg",
    "Månsson",
    "Rydberg",
    "Rydén",
    "Ryding",
    "Rydman",
    "Vikström",
    "Viklund",
    "Vikberg",
    "Vik",
    "Vikman",
    "Lenegren",
    "Lennartsson",
]


def generate_random_string(length):
    """Generate a random string of fixed length"""
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def generate_random_date():
    """Generate a random date between 1/1/2000 and 1/1/2020"""
    start = datetime.datetime(2000, 1, 1, 00, 00, 00)
    end = datetime.datetime(2020, 1, 1, 00, 00, 00)
    return (start + (end - start) * random.random()).strftime("%Y-%m-%d %H:%M:%S")


def generate_random_int():
    """Generate a random integer between 1000 and 9999"""
    return random.randint(1000, 9999)


def personnummer():
    """Generate a random swedish personnummer in the format YYYYMMDD-XXXX, not valid, just random xxxx"""
    start = datetime.date(1960, 1, 1)
    end = datetime.date(1999, 1, 1)
    return f"{(start + (end - start) * random.random()).strftime('%Y%m%d')}-{generate_random_int()}"


def random_adress():
    """Generate a random swedish adress in the format Väg 1, 12345 Stad"""
    city = ["Stockholm", "Täby"]
    street = ["Sveavägen", "Kungsgatan", "Drottninggatan"]
    street_number = random.randint(1, 100)
    post_code = f"{random.randint(10, 99)}{random.randint(100, 999)}"
    return f"{random.choice(street)} {street_number}, {post_code} {random.choice(city)}"


def generate_random_data():
    """Package all the random data generation functions into one function"""
    return f'"String": {generate_random_string(10)}\n"Date and Time": {generate_random_date()}\n"Integer": {generate_random_int()}\n"Personnummer": {personnummer()}\n"Adress": {random_adress()}'


def save_to_json(data):
    """Save the data to a json file"""
    with open("DataGenerator/generated/list03.json", "a") as f:
        json.dump(data, f, indent=4)


def variant_1():
    """Just some playing around with the data"""
    for i in range(10):
        random_data = generate_random_data()
        separator = "-" * len(random_data)
        print(separator)
        print(f"Row {i+1}")
        print(random_data)
        data_for_json = {f"Data {i+1}": random_data}
        save_to_json(data_for_json)


def tenants():
    """Generate a random tenant choosing a random name from the lists of names, and other functions"""
    first = random.choice(firstnames)
    last = random.choice(lastnames)
    social = personnummer()
    # The phone can be generated in one randint but i wanted every number randomly generated
    phone = f"07{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    email_type = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com"]
    # Replace the special characters for the email
    first_replaced = first.replace("å", "a").replace(
        "ä", "a").replace("ö", "o").replace("é", "e")
    last_replaced = last.replace("å", "a").replace(
        "ä", "a").replace("ö", "o").replace("é", "e")
    email = f"{first_replaced}.{last_replaced}{random.choice(email_type)}".lower(
    )
    # Modify this for your own needs and type of data.
    return f"('{first}', '{last}', '{social}', '{phone}', '{email}')"


def tenants_sorted():  # TODO: Sort the tenants in a better way
    """Put the tenants in a list if there are no duplicates. It needs some love for smarter sorting, maybe later"""
    tenant_sort = []
    while len(tenant_sort) < 20:
        tenant = tenants()
        if tenant not in tenant_sort:
            tenant_sort.append(tenant)
    return tenant_sort


def export_sorted():
    """Export the sorted tenants to a csv file in the format you want"""
    with open("DataGenerator/generated/list01.csv", "w") as f:
        for tenant in tenants_sorted():
            f.write(f"{tenant}\n")


def csv_export():
    """This function skips the sorting and just exports the tenants to a csv file"""
    with open("DataGenerator/generated/list02.csv", "a") as f:
        for i in range(20):
            data = tenants()
            f.write(f"{data}\n")


def main():  # TODO: Bring back the function to export to a database... maybe
    """Just comment out the functions you don't want to use"""
    print(generate_random_data())
    export_sorted()
    csv_export()
    # variant_1()


if __name__ == "__main__":
    main()
