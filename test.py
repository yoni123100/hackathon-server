import requests
import pprint
obj = {"title": "Test5", "name": "aviv", "description": "None", "id": "b9fc5f7b-0c75-45c0-9c78-085dfd3cc833", "datetime": "2020-10-08 22:27:27.953080"}
pprint.pprint(obj, indent=4)

# url = 'http://localhost:5000/story'
# response = requests.post(url=url, json=obj)
#
url = 'http://localhost:5000/story'
response = requests.get(url=url, json='')
# print(response.json())

obj = {
        "name": None,
        "email": None,
        "platform": None,
        "facebook": None,
        "linkedin": None,
        "instagram": None,
        "phone": None,
        "description": None
    }