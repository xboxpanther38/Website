from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def website():
    css_yolu = url_for('static', filename='style.css')
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>67 Website</title>
        <link rel="stylesheet" href="{css_yolu}">
    </head>
    <body>
        <div class="kutu">
            <h1>67!</h1>
            <p>Ronaldo portekizlidir</p>
            <h2>Messi kötüdür</h2>
            <ul>
                <li>Discord botum gif atar</li>
                <li>ve oyun önerir</li>
            </ul>

            <!-- Renk değiştiren alan kendi etiketi içinde kapatıldı -->
            <div class="degisken">
                <h4>67</h4>
            </div>

            <!-- Buton kendi etiketi içinde kapatıldı -->
            <button class="buton">rahatla</button>

            <!-- Tenor GIF alanı butonun dışına çıkarıldı -->
            <div class="gif-alani">
                <div class="tenor-gif-embed" data-postid="10799637110820905144" data-share-method="host" data-aspect-ratio="1" data-width="100%">
                    <a href="https://tenor.com/view/ekoi-ekoi-dancekid-dancekid-gif-10799637110820905144">Ekoi Ekoi-dancekid GIF</a> from <a href="https://tenor.com/search/ekoi-gifs">Ekoi GIFs</a>
                </div>
                <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
