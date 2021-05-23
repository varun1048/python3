import requests
requests.get("http://localhost:5000/")
myobj = {'somekey': 'somevalue'}
requests.post("http://localhost:3000/",data=myobj)