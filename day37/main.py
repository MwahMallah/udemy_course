import requests
import datetime

USERNAME = "mwahmallah"
TOKEN = "kajsfdhasdjkfhdsafj"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Coding time",
    "unit": "hours",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

today_date = datetime.date.today().strftime('%Y%m%d')
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today_date}"

graph_params = {
    "quantity": "4"
}

response = requests.put(url=graph_endpoint, headers=headers, json=graph_params)
print(response)