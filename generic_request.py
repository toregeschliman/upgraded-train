import requests
import argparse
import json

class TurnJson():
    def __init__(self, json_obj):
        self.json_obj = json_obj

    def IntoCsv(self, filepath='export.csv'):
        result = ''
        for key in self.json_obj:
            for key_2 in self.json_obj[key]:
                result += (self.json_obj[key][key_2]).encode('ascii', 'replace')
                result += (',')
            result += ('\n')
        with open(filepath, 'w') as f:
            f.write(result)

def main():
    parser = argparse.ArgumentParser(description='Pass JSON to an API endpoint for scraping.')
    parser.add_argument('--jsonsource', dest='source',
                        default='sample.json', help='path to config JSON (default= sample.json)')
    parser.add_argument('--server', dest='config_url',
                        default='http://toregesquire.com/steve',
                        help='URL of scraping API endpoint')
    parser.add_argument('--csv', dest='destination',
                        default='export.csv', help='path to write CSV to (default=export.csv)')
    config = parser.parse_args().source
    config_url = parser.parse_args().config_url
    destination = parser.parse_args().destination

    with open(config, 'r') as f:
        data = json.load(f)

    req = requests.post(config_url, json=data)
    TurnJson(req.json()).IntoCsv(destination)

if __name__=='__main__':
    main()
