from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return (
        """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Landing Rage</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                background-image: url('static/LandingRage.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
                color: white;
                font-family: Arial, sans-serif;
            }
            .content {
                position: absolute;
                top: 3vh;
                right: 2vw;
                text-shadow: 2px 2px 6px #000000;
                text-align: left;
            }
            .content h1 {
                font-size: 2rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
                letter-spacing: 1px;
            }
            .content p {
                font-size: 1rem;
                margin-bottom: 0.4rem;
                opacity: 0.9;
            }
            .claim {
                font-size: 1rem;
                margin-top: 1rem;
                margin-bottom: 0.4rem;
                opacity: 0.9;
                font-weight: 600;
            }
            .stack {
                margin-top: 0.8rem;
                font-size: 0.85rem;
                letter-spacing: 2px;
                opacity: 0.75;
                text-transform: uppercase;
            }
            .hostname {
                font-size: 0.75rem;
                opacity: 0.5;
                margin-top: 0.4rem;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Proof of Concept.</h1>
            <p>A containerized Flask app, deployed on an Azure Debian VM,</p>
            <p>proxied through Nginx, automated via GitHub.</p>
            <p class="claim">The rage was temporary. The pipeline is live.</p>
            <div class="stack">Flask &middot; Podman &middot; Nginx &middot; Azure &middot; GitHub</div>
            <div class="hostname">Container: """
        + os.uname().nodename
        + """</div>
        </div>
    </body>
    </html>
    """
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
