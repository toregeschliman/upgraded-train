from flask import flask, jsonify

import web-scraper

app = Flask(__name__)

@app_route('/', method=['POST'])
def get_contents_from_xpaths():
    if request.method=='POST':
        json_dict = request.get_json()
        scraper = WebScraper(json_dict)
        return jsonify(scraper.scrape())

if __name__ = '__main__':
    app.run(debug=True)
