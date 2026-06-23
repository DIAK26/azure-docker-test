from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    # Wir nutzen CSS direkt im HTML für den Hintergrund
    return (
        """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Azure Docker Test</title>
        <style>
            body {
                /* Ersetze 'hintergrund.jpg' durch deinen Dateinamen */
                background-image: url('LandingRage');
                background-size: cover;       /* Bild füllt den ganzen Screen */
                background-position: center;  /* Zentriert das Bild */
                background-repeat: no-repeat; /* Wiederholt nicht */
                height: 100vh;
                margin: 0;
                color: white;                 /* Textfarbe weiß für besseren Kontrast */
                font-family: Arial, sans-serif;
            }
            .content {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100%;
                text-shadow: 2px 2px 4px #000000; /* Schatten für Lesbarkeit */
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Hallo aus dem Docker-Container!</h1>
            <p>Dies läuft auf: """
        + os.uname().nodename
        + """</p>
            <p>Azure VM mit Hintergrundbild</p>
        </div>
    </body>
    </html>
    """
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
