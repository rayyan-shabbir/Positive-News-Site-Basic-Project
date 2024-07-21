import requests

api_key = "07a071fd4b394cfca644f81d22ac97c6"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-21&sortBy=publishedAt&apiKey=07a071fd4b394cfca644f81d22ac97c6"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
