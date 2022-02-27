import webbrowser as wb
import requests
import json
import random

API_key = '14795746-624081efd179b5bd9be0efe43'

def open(athing):
    payload = {'key': API_key, 'q': athing, 'img_type': 'photo'}
    r = requests.get('https://pixabay.com/api/', params=payload)
    result = json.loads(r.text)
    skaicius= random.randint(1,10)
    #wb.open_new_tab(result['hits'][ll]['largeImageURL'])
    return(result['hits'][skaicius]['largeImageURL'])
print(open('car'))




