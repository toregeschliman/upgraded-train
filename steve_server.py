from flask import Flask, request, jsonify
from web_scraper import WebScraper
import json

app = Flask(__name__)

@app.route('/steve', methods=['POST'])
def get_contents_from_xpaths():
    json_dict = request.get_json()
    scraper = WebScraper(json_dict)
    return jsonify(**scraper.scrape())

if __name__ == '__main__':
    app.run('0.0.0.0:80')
