from flask import Flask, request
import json
import uuid
from datetime import datetime
app = Flask(__name__)


def rate_black_person(data_of_person):
    with open('black_people.json') as json_file:
        black_people_dict = json.load(json_file)
    count = 0
    # Todo: Add logic
    return count


@app.route('/', methods=['GET'])
def is_application_app():
    return 'The application is running.'


@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == "GET":
        with open('stories.json') as json_file:
            stories_dict = json.load(json_file)
        return stories_dict
    else:
        response = request.json
        response['id'] = str(uuid.uuid4())
        response['datetime'] = str(datetime.now())

        with open('stories.json') as json_file:
            stories_dict = json.load(json_file)

        stories_dict["items"].append(response)
        with open('stories.json', 'w') as json_file:
            json.dump(stories_dict, json_file)
        return 'Success'


@app.route('/black_list', methods=['POST', 'GET'])
def black_list():
    if request.method == "GET":
        response = request.json

        with open('black_people.json') as json_file:
            black_people_dict = json.load(json_file)
        return rate_black_person(black_people_dict)
    else:
        response = request.json
        response['id'] = str(uuid.uuid4())
        response['datetime'] = str(datetime.now())

        with open('black_people.json') as json_file:
            black_people_dict = json.load(json_file)

        black_people_dict["items"].append(response)
        with open('black_people.json', 'w') as json_file:
            json.dump(black_people_dict, json_file)
        return 'Success'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
