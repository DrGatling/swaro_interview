from flask import Flask, json, request, render_template
from logic.crawler import findAllTheLinks

api = Flask(__name__)


@api.route('/', methods=['POST', 'GET'])
def index():
    toReturn = True
    if request.method == 'POST':
        toReturn = json.dumps(findAllTheLinks(request.values.get('url_input')))

    return render_template(toReturn=[toReturn])


@api.route('/crawler', methods=['POST', 'GET'])
def crawl():
    return render_template('index.html', json.dumps(findAllTheLinks(request.values.get('url_input'))))


if __name__ == '__main__':
    api.run(debug=True)
