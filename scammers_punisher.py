import random
import string
import requests
import threading

# Where is the data sent to
url = "" #E.g. random.com/fdfd/api.php
# Random letter generator
let = string.ascii_letters

# Setting up the punishment function
while True:

    # Generate some random data
    firstname = "".join(random.choice(let) for k in range(6))
    lastname = "".join(random.choice(let) for k in range(6))
    domain = "".join(random.choice(let) for k in range(5))
    address = "".join(random.choice(let) for k in range(10))
    email = firstname + lastname + '@' + domain + '.com'
    phone_number = "".join(random.choice(string.digits) for k in range(10))
    card_numb = "5400".join(random.choice(let) for k in range(12))
    cvv = "".join(random.choice(string.digits) for k in range(3))

    # Data parameters
    data = {
        'b_fname': firstname,
        'b_lname': lastname,
        'b_email': email,
        'b_country': 'US',
        'b_zip': '10000',
        'b_address1': address,
        'b_state': 'US-NY',
        'b_mobile': phone_number,
        'b_address2': '',
        'b_city': 'New York',
        'company_name': '',
        'fax_number': '',
        'website_address': '',
        'product': 'WT001*86*28',
        'qty': '1',
        'rate': '86',
        'total': '86',
        'cvv': cvv,
        'cvvexpiry': '0322',
        'cardno': card_numb,
        'campaign': '28',
    }

    # Send the POST request
    database = requests.post(url, data=data)
    if database.status_code == 200:
        print('POST request sent successfully\r')
