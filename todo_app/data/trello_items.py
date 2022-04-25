import requests, json, os

trello_key = os.environ.get('TRELLO_KEY')
trello_token = os.environ.get('TRELLO_TOKEN')
trello_board = os.environ.get('TRELLO_BOARD')

def get_items():

    reqUrl = f"https://api.trello.com/1/boards/{trello_board}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "cards": "open"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    first_list = response_json[0]

    first_list_cards = first_list['cards']

    return first_list_cards

# def get_items(id):

    
# def add_item(title,status):

# def save_item(item):

# def complete_item(id):

# def start_item(id):

# def progress_item(id):