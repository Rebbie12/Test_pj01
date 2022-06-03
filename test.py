import requests
city = 'london'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'xVYFBBO9TV/1vcuKc6QLWQ==i9Uv9nArjjslCtWc'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)






