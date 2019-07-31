from flask import Flask
from UnleashClient import UnleashClient

client = UnleashClient("http://127.0.0.1:4242/api", "WebProject1")
client.initialize_client()

app = Flask(__name__)

@app.route('/')
@app.route('/hello')

def hello():
    # Render the page
    if(client.is_enabled("123f")):
        str = "Hello Python! "
    else:
        str = "Bye Python! "

    if(client.is_enabled("togglename")):
        str += "Hello Python! "

    else:
        str += "Bye Python! "

    if(client.is_enabled("ref")):
        str += "Hello Python! "
    else:
        str += "Bye Python! "

    return str;

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)