from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hallo aus dem Docker-Container!</h1>
    <p>Dies läuft auf: ''' + os.uname().nodename + '''</p>
    <p>Azure VM Testseite</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

