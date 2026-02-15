import requests

parameters = {
    "amount":10,
    "category": 18,
    "type": "boolean"
}

data =requests.get("https://opentdb.com/api.php", params=parameters)
data.raise_for_status()

question_bank = []

data = data.json()


question_data=data["results"]

