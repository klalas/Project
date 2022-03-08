
#import requests
#import json
#import random
#mport webbrowser as wb


#API_key = '14795746-624081efd179b5bd9be0efe43'

#def open():
#    payload = {'key': API_key, 'q': 'car', 'img_type': 'photo'}
#    r = requests.get('https://pixabay.com/api/', params=payload)
#    result = json.loads(r.text)
#    skaicius= random.randint(1,10)
#    #wb.open_new_tab(result['hits'][skaicius]['largeImageURL'])
#    return (result['hits'][skaicius]['largeImageURL'])
#print(open())