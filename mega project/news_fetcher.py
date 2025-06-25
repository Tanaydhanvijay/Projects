import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "5b51815bf86944d6a63d8566ca357d25"

url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5b51815bf86944d6a63d8566ca357d25"

print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
