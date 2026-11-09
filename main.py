import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Server is alive and running 24/7!"

if __name__ == "__main__":
    # المنصات السحابية تعطينا بورت خاص بها، وإذا لم توفره فنستخدم البورت 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
