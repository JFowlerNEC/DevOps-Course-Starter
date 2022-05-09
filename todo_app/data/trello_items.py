import requests, json, os

trello_key = os.environ.get('TRELLO_KEY')
trello_token = os.environ.get('TRELLO_TOKEN')
trello_board = os.environ.get('TRELLO_BOARD')

def get_todo_items():

    reqUrl = f"https://api.trello.com/1/boards/{trello_board}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "cards": "all"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    todo_list = response_json[0]

    todo_list_cards = todo_list['cards']

    return todo_list_cards

def get_doing_items():

    reqUrl = f"https://api.trello.com/1/boards/{trello_board}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "cards": "all"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    doing_list = response_json[1]

    doing_list_cards = doing_list['cards']
 
    return doing_list_cards


def get_done_items():

    reqUrl = f"https://api.trello.com/1/boards/{trello_board}/lists"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "cards": "all"
    }

    response = requests.get(reqUrl, params=query_params)

    response_json = response.json()

    done_list = response_json[2]

    done_list_cards = done_list['cards']
 
    return done_list_cards


def update_item(card_id):


    reqUrl = f"https://api.trello.com/1/cards/{card_id}/"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "idList": "626653880ecf1c46be8073f8"
    }

    response = requests.request("PUT", reqUrl, params=query_params)
    
    print(response.text)

def complete_item(card_id):


    reqUrl = f"https://api.trello.com/1/cards/{card_id}/"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "idList": "626653880ecf1c46be8073f9"
    }

    response = requests.request("PUT", reqUrl, params=query_params)
    
    print(response.text)
def doing_item(card_id):


    reqUrl = f"https://api.trello.com/1/cards/{card_id}/"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "idList": "626653880ecf1c46be8073f9"
    }

    response = requests.request("PUT", reqUrl, params=query_params)
    
    print(response.text)

def todo_item(card_id):


    reqUrl = f"https://api.trello.com/1/cards/{card_id}/"

    query_params = {
        "key": trello_key,
        "token": trello_token,
        "idList": "626653880ecf1c46be8073f7"
    }

    response = requests.request("PUT", reqUrl, params=query_params)
    
    print(response.text)