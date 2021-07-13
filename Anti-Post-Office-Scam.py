import requests
import os
import string
import random

url = "https://postoffice-reshipment.net/main/card.php"

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

names = ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander", "Mason",
         "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Harvey", "Travis", "Damon", "Derek",
         "Rodney", "Raquel", "Trevor", "Jarvis", "Michael", "Aston", "Martin", "Trayvon", "Snoop", "Terence", "Gary",
         "Raquel", "Cassandra"]
email_domains = ["@yahoo.com", "@google.co.uk", "@yahoo.co.uk", "@gmail.com", "@lycos.net", "@angelfire.com",
                 "@outlook.com", "outlook.co.uk"]

day = random.randint(0, 31)
month = random.randint(0, 13)
year = random.randint(1945, 2010)
dob = day, "/", month, "/", year, "/"
phone = "0800001066" or "07785633966" or "07154223698"
fake_cc = ["6504153357573497", "9136937046726569", "6980837251993255", "0774739659862913", "2997994618219112",
           "8710671003931815"]
fake_towns = ["Newcastle", "Manchester", "Liverpool", "Birmingham", "London", "Cornwall", "Barnsley", "Swansea",
              "Cardiff", "Glasgow", "Edinburgh", "Dundee", "Belfast", "Dublin", "Kilkenny"]
fake_streets = ["St Johns Way", "Gilpin Road", "Belfast Avenue", "Brindley-on-Trent", "Wallaby West Way",
                "East Ham Road", "Cobbling Road", "Oakway Park Avenue"]
fake_countries = ["England", "Scotland", "Wales", "Northern Ireland", "Ireland"]

while True:
    name_extra = ''.join(random.choice(string.digits))
    random_index_names = random.randint(0, len(names) - 1)
    random_index_domains = random.randint(0, len(email_domains) - 1)
    random_index_cc = random.randint(0, len(fake_cc) - 1)
    random_index_towns = random.randint(0, len(fake_towns) - 1)
    random_index_streets = random.randint(0, len(fake_streets) - 1)
    random_index_countries = random.randint(0, len(fake_countries) - 1)
    username = names[random_index_names] + name_extra + email_domains[random_index_domains]
    card_no = random.randint(100, 999)
    account_no = random.randint(10000000, 99999999)
    credit_card = fake_cc[random_index_cc]
    sc1 = random.randint(10, 99)
    fake_town = fake_towns[random_index_towns]
    sc2 = random.randint(10, 99)
    fake_street = fake_streets[random_index_streets]
    sc3 = random.randint(10, 99)
    fake_country = fake_countries[random_index_countries]
    address = str(day) + fake_street

    requests.post(url, allow_redirects=False, data={
        'fullname': username,
        'dob': dob,
        'email': username,
        'phone': phone,
        'address': address,
        'town': fake_town,
        'country': fake_country,
        'postcode': "WA1 1AA",
        'cardname': username,
        'cardnumber': credit_card,
        'cardexpiry': str(day) + str(month),
        'cardsecurity': str(card_no),
        'account': str(account_no),
        'sortcode': str(sc1) + str(sc2) + str(sc3)

    })

    print('sending username %s' % username, "with", credit_card, "number.", "from", address + fake_country, " cc information: ", str(card_no), str(account_no), "sort-code: ", str(sc1) + str(sc2) + str(sc3))
