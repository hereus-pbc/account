from bevyframe import *
from dotenv import load_dotenv
import os

load_dotenv('../.env')
app = Frame(
    package="net.hereus.account",
    developer="hereus@hereus.net",
    administrator=False,
    secret=os.environ.get('SECRET'),
    style="https://raw.githubusercontent.com/hereus-pbc/HereUS-UI-3.1/master/HereUS-UI-3.1.json",
    icon="https://www.hereus.net/static/favicon.png",
    keywords=[],
    default_network="hereus.net",
    loginview='Login.py',
    environment={
        'message': 'Hello, World!'
    }
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
            